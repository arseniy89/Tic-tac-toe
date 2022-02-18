from itertools import product


def cout():
    print(s:='\n●━━━●━━━●━━━●')
    [print(f'┃ {b[i]} ┃ {b[i+1]} ┃ {b[i+2]} ┃{s}') for i in range(0, 7, 3)]


def reading(s):
    while 1:
        try:
            p = int(input(('2nd: ' if (s%2) else '1st: '))) - 1
            if b[p] == ' ' and p >= 0:
                b[p] = 'o' if (s%2) else 'x'
                cout(); return
        except: pass


def check():
    for i, v in product(range(3), [c, z]):
        if b[i::3]==v or b[i*3:i*3+3]==v or b[::4]==v or b[2:7:2]==v:
            return '1st' if (v[0] == 'x') else '2nd'
    return 'Friendship'


def main():
    print('\nTic-tac-toe game:')
    while input('Play? (y) ') == 'y': 
        global b, c, z; b, c, z = [' ']*9, ['x']*3, ['o']*3; cout()
        [reading(s) for s in range(9) if (a:=check()) == 'Friendship']
        print(f'{a} won')


main()
