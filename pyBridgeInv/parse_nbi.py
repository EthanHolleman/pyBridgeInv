
class NbiReader():

    def __init__(self, field_dict):
        self.field_dict = field_dict
    
    def _read_line(self, line):
        # turn a line into a dictionary based on other stuff 
        # need to do go along
        line_dict = {}
        for field_name, indices in self.field_dict:
            if len(indices) > 1:
                pass
            else:
            
            line_dict[field_name] = line[start:end]
        return line_dict

    def parse_file(self, filepath):
        with open(filepath) as handle:
            return [self._read_line(line) for line in handle.readlines()]
    
    
    


