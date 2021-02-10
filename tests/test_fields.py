import sys
import pytest
import random
import csv
from pathlib import Path
sys.path.append('../pyBridgeInv')
from pyBridgeInv.field import *
from pyBridgeInv import CODE_TABLES, FIELDS
from pyBridgeInv.reader import NciReader

@pytest.fixture
def test_data_dir():
    return Path(__file__).parent.absolute().joinpath('test_data')


@pytest.fixture
def test_filepaths(test_data_dir):
    return list(test_data_dir.iterdir())


@pytest.fixture
def reader(test_filepaths):
    return NciReader(test_filepaths.pop())


@pytest.fixture
def field_list():
    return list(FIELDS.values())

def test_parsed_contents(reader):
    for row in reader:
        for fieldname, field in row.items():
            if field.raw_contents:
                try:
                    parsed_contents = field.parsed_contents
                except Exception as e:
                    message = f'''
                    Unable to parse contents of {field}. Raw contents were
                    {field.raw_contents}. Raised {e} {type(field)} {field.code_table}.
                    '''
                    if issubclass(type(field), DependentField):
                        message += f'{field.code_table}'
                    raise Exception(message)
                # state codes given in documentation do not appear to be correct
                # using the NBI given table codes are all 3 digits but one digit
                # code is used for many states

                assert type(parsed_contents) != None
                


