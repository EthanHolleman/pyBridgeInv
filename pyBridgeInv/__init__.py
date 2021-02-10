from os import read
from pathlib import Path
import csv
import pandas as pd
import sys
import inspect
from pyBridgeInv.code_tables import create_code_tables

CODE_TABLE_DIR = Path(__file__).parent.absolute().joinpath('coding_tables')
CODE_TABLES_PATHS = [t for t in CODE_TABLE_DIR.iterdir() if t.suffix == '.csv']
CODE_TABLE_DELIM = ';'
CODE_TABLES = create_code_tables(CODE_TABLES_PATHS, CODE_TABLE_DELIM)


import pyBridgeInv.field
from pyBridgeInv.field import Field, DependentField


def _get_all_field_classes_dict():
    clsmembers = inspect.getmembers(pyBridgeInv.field, inspect.isclass)
    classes = []
    for name, obj in clsmembers:
        if issubclass(obj, Field):
            classes.append(obj)

    return {c.fieldname: c for c in classes}

def _get_dependent_field_classes_dict(all_fields_dict):
    dependent_fields = {}
    for fieldname, class_ in all_fields_dict.items():
        if issubclass(class_, DependentField) and DependentField in class_.__bases__:
            dependent_fields[fieldname] = class_
    return dependent_fields


FIELDS = _get_all_field_classes_dict()
DEP_FIELDS = _get_dependent_field_classes_dict(FIELDS)





