from pathlib import Path
import csv
from pyBridgeInv import FIELDS, DEP_FIELDS
from pyBridgeInv.field import DependentField, Field

class NciReader():

    def __init__(self, path, delim=',', header=True):
        self.path = Path(path)
        self.delim = delim
        self.header = header
        self._handle = None
        self._reader = self._open_reader(path)
    
    def _open_reader(self, filepath):
        return csv.DictReader(
            open(str(filepath)), delimiter=self.delim
            )

    def _process_row(self, row):
        if type(row) == dict:
            return self._row_dict_to_fields(row)
        else:
            raise Exception()
    
    def _process_field(self, row_dict, field_class):
        return field_class.init_from_string(row_dict[field_class.fieldname])
    
    def _row_dict_to_fields(self, row_dict):
        fields = {}
        for fieldname, raw_content in row_dict.items():
            if fieldname in FIELDS:
                if fieldname in DEP_FIELDS:
                    dep_class = DEP_FIELDS[fieldname].dependent_class
                    if dep_class.fieldname not in fields:  # has not been read yet
                        dep_field = self._process_field(row_dict, dep_class)
                    else:
                        dep_field = fields[dep_class.fieldname]
                    
                    field_class = DEP_FIELDS[fieldname]
                    
                    fields[fieldname] = field_class.init_from_string(raw_content, dep_field)
                else:
                    field_class = FIELDS[fieldname]
                    fields[fieldname] = self._process_field(row_dict, field_class)
        
        return fields
      
    def __iter__(self):
        return self

    def __next__(self):
        next_row = next(self._reader)
        return self._process_row(next_row)
    
    # def __enter__(self):
    #     self._handle = open(str(self.path))
    #     if self.header:
    #         self._reader = csv.DictReader(self._handle)
    #     else:
    #         self._reader = csv.reader(self._handle)
        
    #     return self._handle

    # def __exit__(self, exc_type, exc_value, exc_traceback):
    #     self._handle.close()

