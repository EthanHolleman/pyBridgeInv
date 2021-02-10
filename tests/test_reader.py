import pytest 
import sys
from pathlib import Path
sys.path.append('../pyBridgeInv')
from pyBridgeInv.reader import *

@pytest.fixture
def test_data_dir():
    return Path(__file__).parent.absolute().joinpath('test_data')


@pytest.fixture
def test_filepaths(test_data_dir):
    return list(test_data_dir.iterdir())


@pytest.fixture
def reader(test_filepaths):
    return NciReader(test_filepaths.pop())

def test_reader_creation(reader):
    assert isinstance(reader, NciReader)

def test_reader_iteration(reader):
    for row in reader:
        assert row
        assert isinstance(row, dict)
        for fieldname, field in row.items():
            try:
                parsed_contents = field.parsed_contents
            except Exception as e:
                raise Exception(f'''
            Failed to parse contents from {field}. Raw contents were
            {field.raw_contents}. Raised exception: {e}
            ''')





