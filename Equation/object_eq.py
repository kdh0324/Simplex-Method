from type import Type
from equation import Equation


class ObjectEq(Equation):

    def __init__(self, coefficients):
        super().__init__(coefficients)
        self.set_type(Type.EQ)
        self.type_can_changed = False
