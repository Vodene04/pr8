sqr = 10
#Вывод границ
for i in range(sqr):
    if i == 0 or i == sqr - 1:
        print('* ' * sqr)
#Вывод боковых сторон
    else:
        print('*' + ' ' * (sqr - 2) + '*')