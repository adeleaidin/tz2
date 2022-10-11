from datetime import datetime
from functions import _max, _min, _mult, _razmah, _sum

n = int(input('Какой файл выбрать? (1/2/3/4)  '))
if n == 1:
    f = open('file').readline().split()
if n == 2:
    f = open('file2').readline().split()
if n==3:
    f = open('file3').readline().split()
if n == 4:
    f = open('file4').readline().split()
a = [int(i) for i in f]
print('В файле:', *a)
start = datetime.now()

print('Минимальное: ', _min(a))
print('Максимальное:', _max(a))
print('Сумма:',_sum(a))
print('Произведение:', _mult(a) )
print('Рвзмах: ', _razmah(a))

finish_time = datetime.now()
print(finish_time-start)



