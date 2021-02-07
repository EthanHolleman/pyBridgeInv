import sys
import pytest
import random
import csv
from pathlib import Path
sys.path.append('../pyBridgeInv')
from pyBridgeInv.field import *

here = ''

@pytest.fixture
def nbi_2019_delim_state_files():
    # return path to includes nbi datafile
    return list(here.joinpath('test_data/delim/2019').iterdir())


@pytest.fixture
def random_2019_delim_dict(nbi_2019_delim_state_files):
    max_line = 1000
    nbi_file = random.choice(nbi_2019_delim_state_files)
    line_number = random.randint(0, max_line)
    with open(str(nbi_file)) as handle:
        reader = csv.DictReader(handle)
        for i in range(0, line_number):
            next(reader)
        return next(reader)


@pytest.fixture
def field_classes():
    return get_all_field_classes_dict()


def test_init_from_string(random_2019_delim_dict):
    for fieldname, raw_content in random_2019_delim_dict.items():
        field_class = field_classes  # update this
        obj = field_class.init_from_string(raw_content)
        assert obj
        assert obj.raw_contents
        assert obj.parsed_contents
        assert obj.field_id


def test_get_all_field_classes_dict(field_classes):
    assert isinstance(field_classes, dict)
    for fieldname, class_ in field_classes.items():
        assert issubclass(class_, Field)
        assert class_.fieldname == fieldname


def test_coding_dict_availability(field_classes):
    for fieldname, class_ in field_classes.items():
        if fieldname in CODE_TABLES:
            assert class_.code_table == CODE_TABLES[fieldname]