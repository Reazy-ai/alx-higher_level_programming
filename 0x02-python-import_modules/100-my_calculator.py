#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argCount = len(sys.argv) - 1
    if argCount < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        first = int(sys.argv[1])
        second = int(sys.argv[3])
        
        if operator == "+":
            print("{} + {} = {}".format(first, second, add(first, second)))
            sys.exit(0)
        elif operator == "-":
            print("{} - {} = {}".format(first, second, sub(first, second)))
            sys.exit(0)
        elif operator == "*":
            print("{} * {} = {}".format(first, second, mul(first, second)))
            sys.exit(0)
        elif operator == "/":
            print("{} / {} = {}".format(first, second, div(first, second)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
