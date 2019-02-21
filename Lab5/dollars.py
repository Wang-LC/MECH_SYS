#!/usr/bin/env python3


from numpy import round


class Dollars:
    """A simple currency class for US Dollars"""
    def __init__(self, dollars=0, cents=0):
        # This conversion is not perfect.  It errs on the side of losing money rather than creating it.
        self.pennies = int(dollars * 100) + cents

    def __str__(self):
        # This makes sure that we don't have any problems with division errors
        return'{0}${1}.{2:02}'.format('-' if self.pennies < 0 else '', abs(self.pennies // 100), self.pennies % 100)

    def __add__(self, other):
        retval = Dollars(cents=self.pennies + other.pennies)
        return retval

    def __add__(self, other):
        d = Dollars()

        try:
            d.pennies = self.pennies + other.pennies
        except:
            return self + Dollars(other)

        return d

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        d = Dollars()

        try:
            d.pennies = self.pennies - other.pennies
        except:
            return self - Dollars(other)

        return d

    def __rsub__(self, other):
        return -self + other

    def __neg__(self):
        return Dollars(cents=-self.pennies)

    # def __lt__(self, other):
    #     try:
    #         return self.pennies < other.pennies
    #     except:
    #         return self < Dollars(other)


if __name__ == '__main__':
    a = Dollars(1.23)
    b = Dollars(2.34)

    print(a + 1)

