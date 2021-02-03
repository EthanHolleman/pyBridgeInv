from pathlib import Path
import csv

CODE_DICT_DIR = Path('')

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



