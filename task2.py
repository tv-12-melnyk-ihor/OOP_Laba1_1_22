import argparse

parser = argparse.ArgumentParser()
parser.add_argument('func', type=str)
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
args = parser.parse_args()

func = args.func
x = args.x
y = args.y

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error! Can't divide by 0")

if (func == 'add'):
    print(add(x, y))
elif (func == 'subtract'):
    print(subtract(x, y))
elif (func == 'multiply'):
    print(multiply(x, y))
elif (func == 'divide'):
    print(divide(x, y))
else:
    print('Error! Invalid command')
