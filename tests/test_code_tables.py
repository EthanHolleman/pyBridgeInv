import sys
import pytest
import pandas as pd
sys.path.append('../pyBridgeInv')
from pyBridgeInv.code_tables import *
from pyBridgeInv import *
from pyBridgeInv.field import Field, DependentField

@pytest.fixture
def code_tables():
    return create_code_tables()

def test_df_creation(code_tables):
    '''Test pandas dataframes were created and stored in CODE_TABLE_DICT
    correctly.
    '''
    assert code_tables
    assert isinstance(code_tables, dict)


def test_coding_table_column_count(code_tables):
    '''Test that coding tables have at least 1 column and that index name
    if Code.
    '''
    for coding_table_name, code_table in code_tables.items():
        assert len(code_table.columns) >= 1
        assert code_table.index.name == 'Code'