from pathlib import Path
import csv
from pyBridgeInv import field
from pyBridgeInv.field import CODE_TABLES, DependentField, Field

def dependent_code_tables(code_tables):
    # get dependent field classes from code tables
    dependent_fields = {}
    for fieldname, code_table in code_table.items():
        if issubclass(Field, code_table) and isinstance(code_table, DependentField):
            dependent_fields[fieldname] = code_table
    return dependent_fields

DEPENDENT_CODE_TABLES = dependent_code_tables()

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
    
    # @property
    # def delim(self):
    #     return self.delim
    
    # @delim.setter
    # def delim(self, new_delim):
    #     if
    def _process_row(self, row):
        if type(row) == dict:
            return self._process_row_dict(row)
        else:
            raise Exception()
    
    
    def _row_dict_to_fields(self, row_dict):
        fields = {}
        row_ind_fields = set(row_dict.keys()) - set(DEPENDENT_CODE_TABLES.keys())
        for ind_field in row_ind_fields:
            field_class = CODE_TABLES[ind_field]
            raw_contents = row_dict[ind_field].strip()
            fields[ind_field] = field_class.init_from_string(raw_contents)
        
        for row in DEPENDENT_CODE_TABLES.keys():
            field_class = CODE_TABLES[ind_field]
            raw_contents = row_dict[ind_field].strip()
            dependent_field = fields[field_class.dependent]
            fields[ind_field] = field_class.init_from_string(raw_contents, dependent_field)
            





        for fieldname in row_dict:
            field_class = CODE_TABLES[fieldname]
            raw_contents = row_dict[fieldname].strip()
            fields[fieldname] = field_class.init_from_string(raw_contents)
        return fields

    
    def _process_row_dict(self, row_dict):
        fields = {}
        return fields
        # have something like all fields which maps field names to other
        # stuff. This also means that there is some dependency in which
        # fields need to get read first because some depend on others
        # do all independent classes then the dependent classes
    
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

