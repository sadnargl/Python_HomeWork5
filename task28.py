def zumm (a, b):
    if a == 1:
        return b+1
    return zumm (a-1,b+1)

print ("Сумма чисел:", zumm(int(input ("Введите первое число: ",)), int(input ("Введите второе число: ",))))


