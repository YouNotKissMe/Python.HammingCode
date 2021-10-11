''' Ошибка при дллине строки 3, 6 ,8,10  '''
a = input('Введите комбинацию 0 и 1: ')
mda = [i for i in a]
r = 0
while 2 ** r < len(a) + r + 1:
    r += 1
print(f'число контролных разрядов {r}')
massive = []
q = ''
c = 0
for i in range(r):

    while len(q) < (len(a) + r):
        q += ('0' * (2 ** c))
        q += ('1' * (2 ** c))
    massive.append(q)
    q = ''
    c += 1
q = ''
realvassive = []
for i in range(len(a) + r + 1):   # на этом участке кода
    for z in range(r):
        q += massive[z][i]    # вот тут конкретнее
    realvassive.append(q)
    q = ''
realvassive.pop(0)
print(realvassive, '\n', len(realvassive))

for i in realvassive:
    print(i, ' ', end='')
'''создали таблицу '''
massivestepeney = []
m=0
while 2**m < len(realvassive)+1:
    massivestepeney.append(2**m)
    m += 1
m=0
massiveQ = [x for x in range(len(realvassive))]
# print(len(massiveQ))
for i in massiveQ:
    if i + 1 in massivestepeney:
        massiveQ[i] = 'None'
    else:
        massiveQ[i] = int(mda[m])
        m += 1
index = []
for i in range(len(massiveQ)):
    if massiveQ[i] != 'None':
        index.append(i)
# print(index)
m1 = []
m = 0
for i in range(len(massivestepeney)):
    for b in index:

        m += massiveQ[b] * int(realvassive[b][i])
    m1.append(m % 2)
    m = 0
for i in range(len(m1)):
    massiveQ[massiveQ.index('None')] = m1[i]
# print(f'\n итоговое число с контрольными разрядами: {massiveQ}')
a = int(input(f'\n итоговое число с контрольными разрядами - {massiveQ} \n'
            f'напишите порядковый номер числа в котором нашкодить: '))
if massiveQ[a-1] == 1:
    massiveQ[a-1] = 0
else:
    massiveQ[a-1] = 1
mz = 0
m23 = []
for i in range(len(massivestepeney)):
    for b in range(len(massiveQ)):
        mz += massiveQ[b]*int(realvassive[b][i])
    m23.append(mz % 2)
    mz=0
print('контрольные разряды в нашкоденом варианте: ',m23)
qzq=0
for i in range(len(m23)):
    if m23[i] != 0:
        qzq += 2 ** i
print(f'ошибка в {qzq} , нашкодиный вариант {massiveQ}')
if massiveQ[qzq - 1] == 1:
    massiveQ[qzq - 1] = 0
else:
    massiveQ[qzq - 1] = 1
print('исправленный вариант: ', massiveQ)



