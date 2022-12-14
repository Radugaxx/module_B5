def greeting():
    print("-------------------------------")
    print("--- Приветствуем вас в игре ---")
    print("------ крестики - нолики ------")
    print("-------------------------------")
    print("Введите 2 числа      'x' и 'y' ")
    print("Где:")
    print("--- x --- номер строки")
    print("--- y --- номер столбца")


def show_table():
    print()
    print("    | 0 | 1 | 2 |")
    print('  ---------------')
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print('  ---------------')
        print()


def ask():
    while True:
        coord = input('          ваш ход: ').split()

        if len(coord) != 2:
            print('Введите 2 координаты! ')
            continue
        x, y = coord

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа! ')
            continue
        x, y = int(x), int(y)

        if 0 > x > 2 or 0 > y > 2:
            print("Координаты вне диапазона! ")
            continue
        if field[x][y] != ' ':
            print("Клетка занята! ")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greeting()
num = 0
field = [[' '] * 3 for i in range(3)]
while True:
    num += 1
    show_table()
    if num % 2 == 1:
        print("Ходит крестик! ")
    else:
        print('Ходит нолик! ')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'x'
    else:
        field[x][y] = '0'
    if check_win():
        break
    if num == 9:
        print("Ничья! ")
        break
