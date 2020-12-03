def travel(chain):

    NDT = ['H', 'S', 'SE', 'ER']
    CS = NDT[0]

    print('CS: {0}'.format(CS))

    for i in chain:

        if CS == NDT[0]:
            if i == 'a':
                print('CS: {0} -> {1}'.format(CS, NDT[1]))
                CS = NDT[1]
                continue
            elif i == 'b':
                print('CS: {0} -> {1}'.format(CS, NDT[2]))
                CS = NDT[2]
                continue
            else:
                print('CS: {0} -> {1}'.format(CS, NDT[-1]))
                CS = NDT[-1]
                print('Цепочка не принадлежит языку!')
                return

        if CS == NDT[1]:
            if i == 'b':
                print('CS: {0} -> {1}'.format(CS, NDT[2]))
                CS = NDT[2]
                continue
            else:
                print('CS: {0} -> {1}'.format(CS, NDT[-1]))
                CS = NDT[-1]
                print('Цепочка не принадлежит языку!')
                return

        if CS == NDT[2]:
            if i == 'a':
                print('CS: {0} -> {1}'.format(CS, NDT[2]))
                CS = NDT[2]
                continue
            elif i == 'b':
                print('CS: {0} -> {1}'.format(CS, NDT[2]))
                CS = NDT[2]
                continue
            else:
                print('CS: {0} -> {1}'.format(CS, NDT[-1]))
                CS = NDT[-1]
                print('Цепочка не принадлежит языку!')
                return

    print('Цепочка принадлежит языку!')

chain = input('Введите цепочку последовательности {a, b}: ')

travel(chain)

