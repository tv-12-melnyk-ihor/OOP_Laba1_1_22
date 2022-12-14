import argparse

p = argparse.ArgumentParser()
p.add_argument('-W', type=int)
p.add_argument('-w', nargs="+", type=int)
p.add_argument('-n', type=int)
args = p.parse_args()

capacity = args.W
weights = (args.w)
bars_number = args.n

def maxweight(capacity, weights, bars_number):
    table = [[0 for _ in range(capacity + 2)] for _ in range(bars_number + 2)]
    for i in range(bars_number+1):
        for j in range(capacity+1):
            if (i == 0 or j == 0):
                table[i][j] = 0
            elif(int(weights[i - 1] <= j)):
                table[i][j] = max(int(weights[i - 1]) + table[i-1][j - int(weights[i - 1])], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[i][j]

#Перевірка правильності вводу
if (bars_number != len(weights)):
    raise Exception("Error! Entered number of bars is incorrect")
if (capacity <= 0):
    raise Exception("Error! Capacity cannot be 0 or less")
for bar in weights:
    if (bar <= 0):
        raise Exception("Error! Bar weight cannot be 0 or less")
print(maxweight(capacity, weights, bars_number))
