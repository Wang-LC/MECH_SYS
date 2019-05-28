from math import pi
from sys import exit

# code below this point only runs if this file is run directly like "python lab1_grader.py". Also works fine if run from inside Pycharm
if __name__ == "__main__": 

    # test cylinder_volume
    # imports code from your python files (put in same folder for this to work)
    from volumes import cylinder_volume, torus_volume
    test = cylinder_volume(3, 2)
    if abs(test - 18*pi) > 10e-12:
        print('cylinder_volume failed: incorrect value!')
        exit()
    try:
        test = cylinder_volume(-3, 2)
        print('cylinder_volume failed to reject bad input!')
        exit()
    except ValueError:
        print('cylinder_volume passed tests!')

    # test torus_volume
    test = torus_volume(3, 2)
    if (test - pi**2*5/4) > 10e-12:
        print('torus_volume failed: incorrect value!')
        exit()

    try:
        test = torus_volume(-3, 2)
        print('torus_volume failed to reject bad input!')
        exit()
    except ValueError:
        pass

    try:
        test = torus_volume(2, 3)
        print('torus_volume failed: major radius must be larger than minor radius!')
        exit()
    except ValueError:
        print('torus_volume passed tests!')

    # test close
    from close import close
    if close(1, 2, 0.5):
        print('close failed: 1 and 2 are more than 0.5 apart!')
    elif not close(1, 2, 3):
        print('close failed: 1 and 2 are less than 3 apart!')
    else:
        print('close function passed tests!')

    # test letter_count
    from words import letter_count
    test = letter_count('halLway', 'l')
    failed = False
    if test != 2:
        print('letter_count failed: hallway has 2 L\'')
        failed = True
    test = letter_count('halLway', 'L')
    if test != 2:
        print('letter_count failed: hallway has 2 L\'')
        failed = True

    if not failed:
        print('letter_count passed all tests!')

    # test gcd - left as an exercise :)

    from math import gcd as gcdB
    from gcd import gcd
    import random
    passTimes = 0
    testTimes = 10
    for count in range(testTimes):
        (a, b) = random.sample(range(1000), 2)
        if gcd(a, b) == gcdB(a, b):
            passTimes = passTimes + 1

    if passTimes == testTimes:
        print("gcd passed all tests!")
    else:
        print("gcd failed!")
