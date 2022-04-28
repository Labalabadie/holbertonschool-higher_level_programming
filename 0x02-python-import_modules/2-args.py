#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import argparse
    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif len(argv) - 1 == 1:
        print(len(argv) - 1, "argument:")
        print(f"1: {argv[1]}")
    else:
        print(len(argv) - 1, "arguments:")
        for i in range(len(argv) - 1):
            print(f"{i + 1}: {argv[i + 1]}")
