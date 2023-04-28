def faktorial (n):
    if n <=2:
        return n
    return (n * faktorial (n-1))

def zumm (n):
    if n <=1:
        return n
    return (n+zumm (n-1))

f= int(input ("Введите число для вычисления факториала и суммы: ",))
print ("Факториал числа:", faktorial(f))
print ("Последовательная сумма числа:", zumm(f))


