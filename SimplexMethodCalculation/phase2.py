from collections import defaultdict

from Equation.object_eq import ObjectEq
from Equation.type import Type
from util import *


class Phase1:

    def __init__(self, _equations: list):
        self.equations = _equations
        self.new_variable_index = max(equation.get_len() for equation in self.equations) + 1
        for eq in self.equations:
            if eq is ObjectEq:
                self.ob_eq = eq

    def calculate(self):
        self.first_step()
        while self.step_condition():
            variable = self.find_variable()
            i = self.find_eq(variable)
            if i == -1:
                return None
            make_identify(self.equations[i])
            subtract(self.ob_eq, self.equations[i])

        for i in range(len(self.equations)):
            if self.equations[i] is ObjectEq:
                self.equations[i] = self.ob_eq
        return self.equations

    def first_step(self):
        basic_list = [eq.get_basic() for eq in self.equations if eq is ObjectEq]
        for b, v in self.ob_eq.variables.items():
            if b in basic_list and v < 0:
                i = self.find_eq(b)
                if i == -1:
                    return None
                subtract(self.ob_eq, self.equations[i])

    def step_condition(self):
        for _, v in self.ob_eq.variables.items():
            if v < 0:
                return True
        return False

    def find_variable(self):
        variable = -1
        for i, v in self.ob_eq.variables.items():
            if v < 0 and (variable == -1 or self.ob_eq.variables[variable] > v):
                variable = i
        return variable

    def find_eq(self, variable):
        temp = -1
        fraction = float('inf')
        for eq in self.equations:
            if eq.variables[variable] > 0 and fraction > eq.rhs / eq.variables[variable]:
                temp = self.equations.index(eq)
                fraction = eq.rhs / eq.variables[variable]

        return temp
