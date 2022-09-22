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
    result = x / y
else:
    print("Error! Invalid command")

print(result)
