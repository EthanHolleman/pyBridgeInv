from os import read
from pathlib import Path
import csv
import pandas as pd

CODE_DICT_DIR = Path('')
CODE_TABLE_DELIM = ','


def parse_coding_table(table_path):
    # needs to be able to tables with more than just a - > b mapping
    # Create nested dicts in some cases?
    # Nested dictionary approach is one way to do that
    # Need to handle a n * n table ideally
    # 


    with open(str(table_path)) as handle:
        reader = csv.reader(handle, delimter=CODE_TABLE_DELIM)
        header = next(reader)
        rows = [r for r in reader]
        coding_dict = {}
        #p.loc['N']['Description']  This would be used for the most basic ones
        # where N is the code number
        # pd.read_csv(csv.path, index_col = 0)
        # to do this and if there were extra columns you dont have to worry about weird dictionary
        # structure just overwrite the class lookup when you need to use it
        if len(header) > 2:  # this is a complex table required a nested dict the first item should be the value in the data
            # each additional column becomes its own subdictionary
            # might just be better to read tables as pandas dataframes which would allow
            # for the "2d aspect of some of the tables that arent just basic lookups"

            




def create_code_dicts():
    code_dict = {}
    for code_dict_path in CODE_DICT_DIR.iterdir():
        if code_dict_path.suffix == '.csv':
            with open(str(code_dict_path)) as handle:
                reader = csv.reader(handle)
                next(reader)  # skip the heaser
                code_dict[code_dict_path.name] = {row[0]: row[1] for row in reader}
    
    return code_dict

CODE_DICTS = create_code_dicts()



