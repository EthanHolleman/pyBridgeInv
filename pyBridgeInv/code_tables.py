from pyBridgeInv import *


def read_code_table(table_path):
    # index column should always be the first
    df = pd.read_csv(
        str(table_path), index_col=0,
        delimiter=CODE_TABLE_DELIM,
        skipinitialspace=True)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df


def create_code_tables():
    code_tables = {}
    for code_table_path in CODE_TABLES_PATHS:
        if code_table_path.suffix == '.csv':
            code_table_name = code_table_path.name
            code_tables[code_table_name] = read_code_table(code_table_path)
    return code_tables