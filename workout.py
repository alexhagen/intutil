from pym import func as pym

class workout(object):
    ''' An object to holding details about an entire workout
    '''
    def __init__(self):
        self.path_length = pym.curve()
        self.hr = pym.curve()
