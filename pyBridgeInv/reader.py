from pathlib import Path
import csv

class NciReader():

    def __init__(self, path, delim=',', header=True):
        self.path = Path(path)
        self.delim = delim
        self.header = header
        self._handle = None
        self._reader = None
    
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
    
    def _process_row_dict(self, row_dict):
        fields = {}
        # have something like all fields which maps field names to other
        # stuff. This also means that there is some dependency in which
        # fields need to get read first because some depend on others
        for fieldname in row_dict:
            field_class = FIELD_CLASSES[fieldname]
            raw_contents = row_dict[fieldname]
            fields[fieldname] = field_class.init_from_string(raw_contents)
        
        for fieldname in dependent_rows:
            field_class = FIELD_CLASSES[fieldname]
            raw_contents = row_dict[fieldname]
            dependent = fields[field_class.dependent_class.fieldname]
            fields[fieldname] = field_class.init_from_string(raw_contents, dependent)
        return fields
        # do all independent classes then the dependent classes

    def __iter__(self):
        next_row = next(self._reader)
        return self._process_row(next_row)
    
    def __enter__(self):
        self._handle = open(str(self.path))
        if self.header:
            self._reader = csv.DictReader(self._handle)
        else:
            self._reader = csv.reader(self._handle)
        
        return self._handle

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._handle.close()

