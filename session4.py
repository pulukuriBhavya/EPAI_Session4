import random
import math
import decimal
from decimal import Decimal
from decimal import *

class Qualean():


    def __init__(self, x):
        self.x = x
        getcontext().prec = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if (x not in [1, 0, -1]):
            raise ValueError("Number out of range, Qualean accepts only -1, 0, 1 as input")
        else:
            self._x = x

    def __repr__(self):
        return "Qualean('%s')" % (self.x)

    def __str__(self):
        return 'Qualean: Num = %s'% (self.x)

    def __magic_num__(self):
        with decimal.localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = decimal.ROUND_HALF_UP
            #print (ctx)
            self.y = self.x * Decimal(random.uniform(-1, 1))
            #print(self.y)
        return self.y

    def __add__(self, other):
        x1 = self.__magic_num__()
        print(x1)
        x2 = other.__magic_num__()
        print(x2)
        return x1 + x2

    def __eq__(self, other):
        x1 = self.__magic_num__()
        x2 = other.__magic_num__()
        return x1 == x2

    def __ge__(self, other):
        x1 = self.__magic_num__()
        x2 = other.__magic_num__()
        return x1 >= x2

    def __gt__(self, other):
        x1 = self.__magic_num__()
        x2 = other.__magic_num__()
        return x1 > x2

    def __lt__(self, other):
        x1 = self.__magic_num__()
        x2 = other.__magic_num__()
        return x1 < x2

    def __le__(self, other):
        x1 = self.__magic_num__()
        x2 = other.__magic_num__()
        return x1 <= x2

    def __mul__(self, other):
        x1 = self.__magic_num__()
        x2 = other.__magic_num__()
        return x1 * x2

    def __bool__(self):
        x1 = self.__magic_num__()
        if x1 in ['', 0, None]:
            return False
        else:
            return True

    def __invertsign__(self):
        x1 = self.__magic_num__()
        return -x1

    def __sqrt__(self):
        x1 = self.__magic_num__()
        if (x1 < 0):
            raise ValueError("sqrt() works only for positive numbers")
        else:
            return float(x1)**(1/2)

    def __and__(self, other):
        x1 = self.__magic_num__()
        if other.x in ['', None, []]:
            x2 = 0
        else:
            x2 = self.__magic_num__()
        return bool(x1 and x2)

    def __or__(self, other):
        x1 = self.__magic_num__()
        if other.x in ['', None, []]:
            x2 = 0
        else:
            x2 = self.__magic_num__()
        return bool(x1 or x2)

    def __float__(self):
        x1 = self.__magic_num__()
        return float(x1)
