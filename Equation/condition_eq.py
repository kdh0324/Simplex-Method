from type import Type
from equation import Equation


class ConditionEq(Equation):

    def __init__(self):
        super().__init__()
        self.set_type(Type.LEQ)

    def check_phase1(self):
        if self.type is not Type.LEQ:
            return True
        return False
