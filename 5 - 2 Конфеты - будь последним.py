# 2 Создайте программу для игры с конфетами человек против человека.
#
# 3 Условие задачи: На столе лежит 2022 конфеты.
#         Играют два игрока делая ход друг после друга.
#         Первый ход определяется жеребьёвкой.
#         За один ход можно забрать не более чем 28 конфет.
#         Все конфеты оппонента достаются сделавшему последний ход.
#         Сколько конфет нужно взять первому игроку,
#             чтобы забрать все конфеты у своего конкурента?
from random import randint

player_1 = 'Антон'  # input('Введите имя  1-го игрока: ')
player_2 = 'Борис'  # input('Введите имя  2-го игрока: ')

team = {}

if randint(1, 2) == 1:
    team[1] = player_1
    team[2] = player_2
else:
    team[1] = player_2
    team[2] = player_1
print(team)


bank = 28
print(f'У нас имеется {bank} конфет можно взять до {bank // 9}-х конфет.')


def move(player):
    global team
    global bank
    move_pl = 0
    while ((1 > move_pl) or (move_pl > (bank // 9))) and type(move_pl) == int:
        try:
            move_pl = int(input(f'Ходит {player}\nВведите число от 1 до {bank // 9}: '))
        except:
            print(f'введитечисло от 1 до {bank // 9}:')
    return move_pl


a = move(player_2)
print(a)

def game_host():


