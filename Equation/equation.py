from type import Type


class Equation:

    def __init__(self, _equation: dict):
        self.variables = dict()
        self.rhs = 0
        self.type_can_changed = True
        is_rhs = False
        for i, v in _equation.items():
            if is_rhs:
                self.rhs = v
            else:
                self.variables[i] = v

    def add_variable(self, variable_index):
        if self.type == Type.LEQ:
            self.variables[variable_index] = 1
        else:
            self.variables[variable_index] = -1

    def set_type(self, _type):
        self.type = _type

    def set_coefficient(self, variable_index, coefficient):
        self.variables[variable_index] = coefficient

    def set_rhs(self, _rhs):
        self.rhs = _rhs

    def check_phase1(self):
        return False

    def get_len(self):
        return len(self.variables)
