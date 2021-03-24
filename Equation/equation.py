class Equation:

    def __init__(self):
        self.variables = dict()
        self.rhs = 0
        self.type_can_changed = True

    def add_variable(self):
        self.variables[len(self.variables)] = 0

    def set_type(self, _type):
        self.type = _type

    def set_coefficient(self, variable_index, coefficient):
        self.variables[variable_index] = coefficient

    def set_rhs(self, _rhs):
        self.rhs = _rhs

    def check_phase1(self):
        return False
