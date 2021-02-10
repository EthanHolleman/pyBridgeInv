import sys
import pytest
import os
import csv
import pandas as pd
sys.path.append('../pyBridgeInv')
from pyBridgeInv import *
from pyBridgeInv.field import Field

def test_code_table_paths():
    for path in CODE_TABLES_PATHS:
        assert path.is_file()
        assert os.stat(str(path)).st_size > 0  # not empty

def test_code_table_dir_existence():
    assert CODE_TABLE_DIR.is_dir()

def test_delimiter():
    '''Test to make sure the delimiter specified by CODE_TABLE_DELIM
    actually makes sense and occurs in a way that would be expected
    in the coding table files.
    '''
    for path in CODE_TABLES_PATHS:
        with open(str(path)) as handle:
            assert CODE_TABLE_DELIM in handle.readline()

def test_get_all_field_classes_dict():
    assert FIELDS
    for fieldname, class_ in FIELDS.items():
        assert class_.fieldname == fieldname
        assert issubclass(class_, Field)


def test_get_dependent_field_classes_dict():
    assert DEP_FIELDS
    for fieldname, class_ in DEP_FIELDS.items():
        assert class_.fieldname == fieldname
        assert issubclass(class_, DependentField)
        assert class_.dependent_class.fieldname in FIELDS

        
        



        
















