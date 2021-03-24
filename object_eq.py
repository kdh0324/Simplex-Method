from type import Type
from equation import Equation


class ObjectEq(Equation):

    def __init__(self):
        super().__init__()
        self.set_type(Type.EQ)
