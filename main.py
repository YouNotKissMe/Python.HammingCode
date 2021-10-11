def PobitovoeYmnogenie(a1, b1, c1, c2):
    mz = 0
    m23 = []
    for i in range(c1):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        for b in c2:
            mz += a1[b] * int(b1[b][i])

        m23.append(mz % 2)
        mz = 0
    return m23


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

    while len(q) < (len(a) + r + 1):
        q += ('0' * (2 ** c))
        q += ('1' * (2 ** c))
    massive.append(q)
    q = ''
    c += 1
q = ''

realvassive = []
for i in range(len(a) + r + 1):

    for z in range(r):
        q += massive[z][i]

    realvassive.append(q)
    q = ''
realvassive.pop(0)
print('Битовыая Таблица: ',end='')
for i in realvassive:
    print(i, ' ', end='')
massivestepeney = []
m = 0
while 2 ** m < len(realvassive) + 1:

    massivestepeney.append(2 ** m)
    m += 1

m = 0
massiveQ = [x for x in range(len(realvassive))]
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

m1=PobitovoeYmnogenie(massiveQ, realvassive, len(massivestepeney), index)
for i in range(len(m1)):
    massiveQ[massiveQ.index('None')] = m1[i]
print(f'\nКонтрольные разряды: {m1}')
print(f'итоговое число с контрольными разрядами - ',end='')
for i in massiveQ:
    print(i,end='')
a = int(input(f'\nнапишите порядковый номер числа в котором нашкодить: '))
if massiveQ[a - 1] == 1:
    massiveQ[a - 1] = 0
else:
    massiveQ[a - 1] = 1
mz = 0
m23 = PobitovoeYmnogenie(massiveQ, realvassive, len(massivestepeney), range(len(massiveQ)))
print('контрольные разряды в нашкоденом варианте: ', m23)
qzq = 0
for i in range(len(m23)):
    if m23[i] != 0:
        qzq += 2 ** i
print(f'ошибка в {qzq} , нашкодиный вариант {massiveQ}')
if massiveQ[qzq - 1] == 1:
    massiveQ[qzq - 1] = 0
else:
    massiveQ[qzq - 1] = 1
print('исправленный вариант: ', massiveQ)
