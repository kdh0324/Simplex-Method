from type import Type
from equation import Equation


class ObjectEq(Equation):

    def __init__(self, _equation):
        super().__init__(_equation)
        self.set_type(Type.EQ)
        self.type_can_changed = False
