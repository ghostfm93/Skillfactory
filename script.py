table = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']] #обозначим двумерный массив в глобальном неймспейсе
move_counter = 0


def field():                                                #отрисовка игрового поля
    print('_______')
    print(f'  0 1 2')
    for i in range(3):
        print(i, *table[i])
    print('_______')


def who_move(move_counter):                                 #определение того, кто ходит
    if move_counter % 2 == 0:
        return 'X'
    elif move_counter % 2 != 0:
        return '0'


def can_move(a, b):                                         #определение возможности хода в клетку по координатам
    if a < 0 or a > 2 or not str(a).isdigit() or a == None or b < 0 or b > 2 or not str(b).isdigit() or b == None:
        return True
    if table[a][b] == 'X' or table[a][b] == '0':
        return True
    else:
        return False


def win_check():                                            #проверка на победу
    win_lines = ([(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
                 [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 2)])
    for i in range(len(win_lines)):
        winstring = ''
        for j in win_lines[i]:
            winstring += table[j[0]][j[1]]
            if winstring == 'XXX':
                return 'X'
            elif winstring == '000':
                return '0'


def game():                                                 #непосредственно игра
    move_counter = 0
    while True:
        field()
        a, b = map(int, input(f'Сейчас ходит "{who_move(move_counter)}". Введите координаты хода через пробел.\n').split(' '))
        while can_move(a, b):
            a, b = map(int, input(f'Координаты неверны или заняты. Введите верные координаты хода через пробел.\n').split(' '))
        table[a][b] = who_move(move_counter)
        move_counter += 1
        if win_check() == 'X':
            field()
            print('Победили крестики')
            break
        elif win_check() == '0':
            field()
            print('Победили нолики')
            break
        if move_counter > 8:
            field()
            print('Ничья')
            break


game()
