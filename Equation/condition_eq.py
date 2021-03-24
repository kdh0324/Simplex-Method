from type import Type
from equation import Equation


class ConditionEq(Equation):

    def __init__(self, coefficients: dict):
        super().__init__(coefficients)
        self.set_type(Type.LEQ)
        self.artificial = None

    def check_phase1(self):
        if self.type != Type.LEQ:
            return True
        return False

    def set_artificial(self):
        if self.type != Type.EQ:
            self.artificial = 1
        else:
            self.artificial = None
