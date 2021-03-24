from Equation.condition_eq import ConditionEq
from Equation.equation import Equation


def make_identify(eq: ConditionEq):
    basic = eq.get_basic()
    if basic == 1:
        return

    temp = 1 / basic
    for i, v in eq.variables.items():
        eq.variables[i] = v * temp
    eq.rhs *= temp


def subtract(eq1: Equation, eq2: Equation):
    """
    :param eq1: target equation which is subtracted
    :param eq2: equation to subtract
    """
    for i, v in eq2.variables.items():
        eq1.variables[i] -= v
    eq1.rhs -= eq2.rhs
