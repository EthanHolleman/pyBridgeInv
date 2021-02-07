from os import read
from pathlib import Path
import csv
import pandas as pd

CODE_TABLE_DIR = Path(__file__).parent.absolute().joinpath('coding_tables')
CODE_TABLES_PATHS = [t for t in CODE_TABLE_DIR.iterdir() if t.suffix == '.csv']
CODE_TABLE_DELIM = ';'





