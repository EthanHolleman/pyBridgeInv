import sys
import pytest
sys.path.append('../pyBridgeInv')
from pyBridgeInv.field import *


@pytest.fixture
def field_classes():
    return get_all_field_classes_dict()


def test_get_all_field_classes_dict(field_classes):
    assert isinstance(field_classes, dict)
    for fieldname, class_ in field_classes.items():
        assert issubclass(class_, Field)
        assert class_.fieldname == fieldname


def test_coding_dict_availability(field_classes):
    for fieldname, class_ in field_classes.items():
        if fieldname in CODE_TABLES:
            assert class_.code_table == CODE_TABLES[fieldname]