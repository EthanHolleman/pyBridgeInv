# from pyBridgeInv import code_table_dict
from datetime import datetime
import pandas as pd
import sys, inspect
from pyBridgeInv import CODE_TABLES
# from pyBridgeInv.code_tables import create_code_tables
# Another way could be to link functions to specifc ones but then
# would still need to define functions for all these

class Field():

    fieldname = None
    page_number = None
    field_counter = 0

    def __init__(self, raw_contents):
        self.raw_contents = raw_contents.strip()
        Field.field_counter += 1

    @classmethod
    def init_from_string(cls, string):
        return cls(string)

    @property
    def parsed_contents(self):
        if self.definition:
            return self.definition
        return self.raw_contents

    @property
    def fieldname(cls):
        return cls.fieldname

    @property
    def code_table(cls):
        if cls.fieldname in CODE_TABLES:
            return CODE_TABLES[cls.fieldname]
        else:
            return pd.DataFrame()

    @property
    def field_id(cls):
        return cls.fieldname.split('_')[-1]

    @property
    def definition(self):
        '''If this field has a code dict available, returns the value
        stored in its respective code dict at the key equal to
        the instances raw_contents attribute.
        '''
        # in theory by default all tables should have codes as the index
        # names and then a Description column. If the coding table
        # is more complex (more than 2 columns) the definition property
        # willl have to be overwritten to reflect the coding table
        # for this reason coding tables should be transcribed with this
        # kind og lookup structure in mind
        if not self.code_table.empty:
            return self.code_table.loc[self.raw_contents]['Description']
        else:
            return None

class DependentField(Field):

    fieldname = None  # these should have values in a child class
    page_number = 0
    dependent_class = None

    def __init__(self, raw_contents, dependent=None):
        super().__init__(raw_contents)
        self.dependent = dependent

    @classmethod
    def init_from_string(cls, string, dependent):
        return cls(string, dependent)

    @property
    def dependent(self):
        return self._dependent

    @dependent.setter
    def dependent(self, new_depend):
        required_type = self.dependent_class
        if type(new_depend) != required_type:
            raise ValueError(
                f'''
                Attempted to assign an object of type {type(new_depend)} to
                the dependent attribute when an object of type
                {required_type} is required. 
                '''
            )
        self._dependent = new_depend

    @property
    def definition(self):
        return self.code_table.loc[self.raw_contents][self.dependent.raw_contents]



class StateCode(Field):

    fieldname = 'STATE_CODE_001'
    page_number = None

    def __init__(self, raw_contents):
        super().__init__(raw_contents)


class StructureNumber(Field):

    fieldname = 'STRUCTURE_NUMBER_008'
    page_number = None

    def __init__(self, raw_contents):
        super().__init__(raw_contents)


class RecordType(Field):

    fieldname = 'RECORD_TYPE_005A'
    page_number = ''

    def __init__(self, raw_contents):
        super().__init__(raw_contents)


class Kilometerpoint(Field):

    fieldname = 'KILOPOINT_011'
    page_number = 18

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return float(self.raw_contents)


class Latitude(Field):

    fieldname = 'LAT_016'
    page_number = 8

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    def parsed_contents(self):
        return parse_lat_long_string(self.raw_contents)


class Longitude(Field):

    fieldname = 'LONG_017'
    page_number = 9

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    def parsed_contents(self):
        return parse_lat_long_string(self.raw_contents)


class ServiceLevel(Field):

    fieldname = 'SERVICE_LEVEL_005C'
    page_number = ''

    def __init__(self, raw_contents):
        super().__init__(raw_contents)


class DetorKilos(Field):

    fieldname = 'DETOUR_KILOS_019'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return float(self.raw_contents)


class YearBuild(Field):

    fieldname = 'YEAR_BUILT_027'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return int(self.raw_contents)


class TrafficLanesUnder(Field):

    fieldname = 'TRAFFIC_LANES_UND_028B'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return int(self.raw_contents)


class InspectFreqMonths(Field):

    fieldname = 'INSPECT_FREQ_MONTHS_091'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return int(self.raw_contents)


class FractureFreq(Field):

    fieldname = 'FRACTURE_092A'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return parse_qualified_mm(self.raw_contents)


class UnderwaterInspecFreq(Field):
    fieldname = 'UNDWATER_LOOK_SEE_092B'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        return parse_qualified_mm(self.raw_contents)


class FunctionalClass(Field):
    fieldname = 'FUNCTIONAL_CLASS_026'
    page_number = 0

    def __init__(self, raw_contents):
        super().__init__(raw_contents)


class UnderClearanceEval(DependentField):
    fieldname = 'UNDCLRENCE_EVAL_069'
    dependent_class = FunctionalClass
    page_number = 0

    def __init__(self, raw_contents, dependent):
        super().__init__(raw_contents, dependent)

    # need someway that maps the fieldname to
    # a function that does that parsing if needed
    # one option is to have a class for each field
    # that needs are parsing method
    # another option is to have dictionary that maps functions
    # to other big dictionary of functions might be ugly though
    # What other stuff do we need for a field
    # maybe like description or that kind of thing

def get_all_field_classes_dict():
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    classes = []
    for name, obj in clsmembers:
        if issubclass(obj, Field):
            classes.append(obj)

    return {c.fieldname: c for c in classes}

def get_independent_field_classes_dict():
    # classes = [ for _, obj in clsmembers if isinstance(obj, Field)]
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    classes = []
    for name, obj in clsmembers:
        if issubclass(obj, Field) and not issubclass(obj, DependentField):
            classes.append(obj)

    return {c.fieldname: c for c in classes}


def parse_lat_long_string(string):
    return f'{string[2:]}.{string[2:]}'

    float(string[:2] + '.' + string[2:])


def parse_yyyy_string(string):
    return datetime(year=string, month=1, day=1)


def parse_mmyy_string(string):

    month, year = int(string[:2]), int(string[2:])
    # need to determine when to add 20 and when to add 19

    return datetime(year=year, month=month, day=1)


def parse_qualified_mm(string):
    if string == 'N':
        return None
    return int(string[1:])

