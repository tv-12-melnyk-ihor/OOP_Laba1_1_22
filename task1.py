import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
parser.add_argument('op', type=str)
parser.add_argument('y', type=int)
args = parser.parse_args()

x = args.x
op = args.op
y = args.y
result = None

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error! Can't divide by 0")
else:
    print("Error! Invalid command")

print(result)
