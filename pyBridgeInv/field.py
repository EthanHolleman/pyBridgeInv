from pyBridgeInv import code_table_dict

# Another way could be to link functions to specifc ones but then
# would still need to define functions for all these

def parse_lat_long_string(string):
    return f'{string[2:]}.{string[2:]}'
    
    float(string[:2] + '.' + string[2:])




class Field():

    fieldname = None
    page_number = None
    field_counter = 0

    def __init__(self, raw_contents):
        self.raw_contents = raw_contents
        Field.field_counter += 1

    @property
    def parsed_contents(self):
        return self.contents

    @property
    def code_dcit(cls):
        if cls.fieldname in code_table_dict:
            return code_table_dict[cls.fieldname]
        else:
            return {}

    @property
    def field_id(cls):
        return cls.fieldname.split('_')[-1]

    @property
    def definition(self):
        '''If this field has a code dict available, returns the value
        stored in its respective code dict at the key equal to
        the instances raw_contents attribute.
        '''
        if self.code_dict:
            return self.field_dict[type(self).fieldname]
        else:
            return None

    def __str__(self):
        str(self.contents.strip())


class StateCode(Field):

    fieldname = 'STATE_CODE_001'
    page_number = None

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        pass


class StructureNumber(Field):

    fieldname = 'STRUCTURE_NUMBER_008'
    page_number = None

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        pass


class RecordType(Field):

    fieldname = 'RECORD_TYPE_005A'
    page_number = ''

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        pass


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
        return float(self.raw_contents[:2] + '.' + self.raw_contents[2:])


class Longitude(Field):

    fieldname = 'LONG_017'
    page_number = 9

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    def parsed_contents(self):
        return float(self.raw_contents[:2] + '.' + self.raw_contents[2:])


class ServiceLevel(Field):

    fieldname = 'SERVICE_LEVEL_005C'
    page_number = ''

    def __init__(self, raw_contents):
        super().__init__(raw_contents)

    @property
    def parsed_contents(self):
        pass

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



    # need someway that maps the fieldname to
    # a function that does that parsing if needed
    # one option is to have a class for each field
    # that needs are parsing method
    # another option is to have dictionary that maps functions
    # to other big dictionary of functions might be ugly though
    # What other stuff do we need for a field
    # maybe like description or that kind of thing
