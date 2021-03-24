from equation import Equation
from type import Type


class ConditionEq(Equation):

    def __init__(self, _equation: dict):
        super().__init__(_equation)
        self.set_type(Type.LEQ)
        self.artificial = None
        self.basic = -1

    def check_phase1(self):
        if self.type != Type.LEQ:
            return True
        return False

    def set_artificial(self):
        if self.type != Type.EQ:
            self.artificial = 1
            self.basic = None
        else:
            self.artificial = None

    def set_basic(self, i):
        self.basic = i

    def get_basic(self):
        return self.basic
