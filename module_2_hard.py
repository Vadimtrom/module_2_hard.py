n = int(input('Введите целое число от 3 до 20: '))
def password(n):
    summa = []
    for i in range(1,n):

        for j in range(i + 1,n):

            if n % (i + j) == 0:

                summa.append(f'{i} {j}')
    return summa


print(n,'-',*password(n))




