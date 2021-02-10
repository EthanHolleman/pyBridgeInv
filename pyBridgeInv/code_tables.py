import pandas as pd


def read_code_table(table_path, delimiter):
    # index column should always be the first
    df = pd.read_csv(
        str(table_path), index_col=0,
        delimiter=delimiter,
        skipinitialspace=True)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    df.index.name = df.index.name.strip()
    return df


def create_code_tables(code_table_paths, delimiter=';'):
    code_tables = {}
    for code_table_path in code_table_paths:
        if (code_table_path.suffix == '.csv' 
        and 'META' not in code_table_path.name 
        and 'README' not in code_table_path.name):
            code_table_name = code_table_path.stem
            code_tables[code_table_name] = read_code_table(code_table_path, delimiter)
    return code_tables