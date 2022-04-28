#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    c = int(argv[1])
    e = int(argv[3]) 
    if argv[2] == chr(45):
        d = chr(45)
        f = c - e
    if argv[2] == chr(47):
        d = chr(47)
        f = c / e
    if argv[2] == chr(42):
        d = chr(42)
        f = c + e
    if argv[2] == chr(43):
        d = chr(43)
        f = c + e
    print(f"{c} {d} {e} = {f}")
    
