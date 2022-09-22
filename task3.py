import argparse

parser = argparse.ArgumentParser()
parser.add_argument('str', type=str)
args = parser.parse_args()

strinput = args.str

def istrue(strinput):
    if (strinput[0].isdigit() == False):
        return False
    num = 0
    sum = 0
    for i in range(len(strinput)):
        current = strinput[i]
        if (current == strinput[len(strinput) - 1]):
            next = None
        else:
            next = strinput[i+1]
        #Перевірка на правильність вводу
        if ((current.isdigit() == False and current != '+' and current != '-')
                or ((current == '+' or current == '-') and (next == None or next.isdigit() == False))):
            return False
    return True

def count(strinput):
    num = 0
    sum = 0
    multiplier = 1
    for i in range(len(strinput)):
        current = strinput[i]
        #Записуємо число в змінну num
        if (current.isdigit() == True):
            num = num * 10 + int(current)
        #Додаємо число num до суми, попередньо врахувавши знак перед num
        elif (current == '+' or current == '-'):
            num = multiplier * num
            sum = sum + num
            num = 0
            #Запам'ятовуємо знак наступного доданка
            if (current == '+'):
                multiplier = 1
            elif (current == '-'):
                multiplier = -1
    #Додаємо/віднімаємо останнє число
    num = multiplier * num
    sum = sum + num
    return sum

if (istrue(strinput) == False):
    print(False, None)
else:
    print(True, count(strinput))