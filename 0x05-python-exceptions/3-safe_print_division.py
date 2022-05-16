#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except (ZeroDivisionError):
        c = None
    finally:
        if c is not None:
            print("Inside result: {:.1f}".format(c))
        else:
            print("Inside result: None")

        return c
