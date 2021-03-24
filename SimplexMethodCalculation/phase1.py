from collections import defaultdict

from Equation.object_eq import ObjectEq
from Equation.type import Type
from util import *


class Phase1:

    def __init__(self, _equations: list):
        self.equations = _equations
        self.new_variable_index = max(equation.get_len() for equation in self.equations) + 1
        self.add_slack()
        self.set_artificial_variables()

    def add_slack(self):
        for eq in self.equations:
            if eq is ObjectEq:
                continue
            if eq.type != Type.EQ:
                eq.add_variable(self.new_variable_index)
                eq.set_basic(self.new_variable_index)
                self.new_variable_index += 1

    def set_artificial_variables(self):
        for eq in self.equations:
            if eq is ConditionEq:
                eq.set_artificial()

        w_eq = defaultdict(int)
        w_eq['a'] = 1
        w_eq['-w'] = 1
        self.w_equation = ConditionEq(w_eq)
        self.w_equation.set_basic('-w')
        self.w_equation.set_type(Type.EQ)
        self.equations.append(self.w_equation)

    def calculate(self):
        self.first_step()
        while self.step_condition():
            variable = self.find_variable()
            i = self.find_eq(variable)
            if i == -1:
                return None
            make_identify(self.equations[i])
            subtract(self.w_equation, self.equations[i])
        return self.equations

    def first_step(self):
        for eq in self.equations:
            if eq is ConditionEq and eq.get_basic() == 'a':
                subtract(self.w_equation, eq)
                break

    def step_condition(self):
        for _, v in self.w_equation.variables.items():
            if v < 0:
                return True
        return False

    def find_variable(self):
        variable = -1
        for i, v in self.w_equation.variables.items():
            if i < 0 and (variable == -1 or self.w_equation.variables[variable] > v):
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
