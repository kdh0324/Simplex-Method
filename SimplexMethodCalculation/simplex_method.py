from Equation.condition_eq import ConditionEq
from Equation.equation import Equation
from Equation.object_eq import ObjectEq
from phase1 import Phase1
from phase2 import Phase2


class SimplexMethod:

    def __init__(self, _problem):
        self.equations = []
        self.problem = _problem

    def set_problem(self):
        is_object = True
        for eq in self.problem:
            if is_object:
                self.equations.append(ObjectEq(eq))
                is_object = False
            else:
                self.equations.append(ConditionEq(eq))

    def calculate(self):
        self.set_problem()
        if self.check_phase1():
            ph1 = Phase1(self.equations)
            self.equations = ph1.calculate()
        ph2 = Phase2(self.equations)
        ph2.calculate()

    def add_equation(self, eq: Equation):
        self.equations.append(eq)

    def check_phase1(self):
        for eq in self.equations:
            if eq.check_phase1:
                return True
        return False
