from Equation.type import Type
from Equation.object_eq import ObjectEq


class Phase1:

    def __init__(self, _equations):
        self.equations = _equations
        self.new_variable_index = max(self.equations.get_len()) + 1
        self.add_slack()

    def add_slack(self):
        for eq in self.equations:
            if eq is ObjectEq:
                continue
            if eq.type != Type.EQ:
                eq.add_variable(self.new_variable_index)
                self.new_variable_index += 1

    def calculate(self):
