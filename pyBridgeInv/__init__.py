from os import read
from pathlib import Path
import csv
import pandas as pd
from pyBridgeInv.field import _get_independent_field_classes_dict

CODE_TABLE_DIR = Path('')
CODE_TABLE_DELIM = ','
INDEPENDENT_FIELD_DICT = _get_independent_field_classes_dict()

def read_code_table(table_path):
    # index column should always be the first
    return pd.read_csv(str(table_path), index_col=0)

def create_code_tables():
    code_tables = {}
    for code_table_path in CODE_TABLE_DIR.iterdir():
        if code_table_path.suffix == '.csv':
            code_table_name = code_dict_path.name
            code_tables[code_table_name] = read_code_table(code_table_path)
    return code_tables



