__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"

from calculatorFunctions.commonFunctions import commonFunctions

def squareroot( value):

    error = 0.0000000001
    squareRootVal = value/2
    if value == 0:
        return 0

    if value == 1:
        return 1


    while True:
        dif = commonFunctions.power(squareRootVal,2) - value

        if commonFunctions.my_abs(dif) <= error:
            break

        squareRootVal = (squareRootVal + value / squareRootVal) / 2.0
    return squareRootVal


def main():
    pass

if __name__ == "__main__":
    main()
else:
    pass