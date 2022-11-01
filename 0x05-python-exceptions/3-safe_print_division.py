#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result: {}".format(division))
<<<<<<< HEAD
=======
    return division
>>>>>>> eec7af1fa307567bcbd76c6d97712eec747630b2
