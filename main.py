# крестики нолики без ГУИ
# начало работы: 13.07.18

import random
import time


def menu():
    print("[0] - выход\n[1] - играть против компьютера\n[2] - игра на двоих")
    selection = input()

    return selection


def create_game_field():
    field = ["   ", "   ", "   ",
             "   ", "   ", "   ",
             "   ", "   ", "   "]

    return field


def show_game_field(field):
    showed_field = ("""
    {0}|{1}|{2}
    ---+---+---
    {3}|{4}|{5}
    ---+---+---
    {6}|{7}|{8}""".format(field[0], field[1], field[2],
                          field[3], field[4], field[5],
                          field[6], field[7], field[8]))

    return showed_field


def who_first():
    first_motion = random.choice(["пека", "игрок"])
    print("Монетка брошена, первым ходит:", first_motion)

    return first_motion


def motion_on_field(field, cell_of_number, marker):
    if field[cell_of_number] == "   " and field[cell_of_number] != " X ":
        field[cell_of_number] = " {} ".format(marker)
        return True
    else:
        return False


def check_winner(field):
    if (field[0] == field[1] == field[2] and field[0] != "   ") or \
       (field[3] == field[4] == field[5] and field[3] != "   ") or \
       (field[6] == field[7] == field[8] and field[6] != "   ") or \
       \
       (field[0] == field[3] == field[6] and field[0] != "   ") or \
       (field[1] == field[4] == field[7] and field[1] != "   ") or \
       (field[2] == field[5] == field[8] and field[2] != "   ") or \
       \
       (field[0] == field[4] == field[8] and field[0] != "   ") or \
       (field[2] == field[4] == field[6] and field[2] != "   "):
        return True
    elif "   " not in field:
        return "draw"


def motion_player(field, marker):
    if not check_winner(field):
        while True:
            try:
                motion = int(input("\nВведи поле куда хочешь сходить (0-8): "))
                if motion_on_field(cell_of_number=motion, field=field, marker=marker):
                    last_marker = marker
                # break
                    return last_marker
                else:
                    print("Это поле уже занято.")
            except ValueError:
                # motion = input("Введи ещё раз. Но теперь правильно: ")
                print("Не верно. Поробуй ещё раз.")
            except IndexError:
                # motion = input("Введи ещё раз. Но теперь правильно: ")
                print("Не верно. Поробуй ещё раз.")


def motion_pc(field, marker):
    if not check_winner(field):
        print("\nКомпьютер ходит...")
        time.sleep(1)
        motion = 0
        while True:
            if motion_on_field(cell_of_number=motion, field=field, marker=marker):
                last_marker = marker
                # break
                return last_marker
            else:
                motion += 1


if __name__ == "__main__":
    print("Крестики Нолики")
    while True:
        selection = menu()
        field = create_game_field()
        if selection == "0":
            print("До встречи")
            exit()
        elif selection == "1":
            first_motion = who_first()

            if first_motion == "пека":
                pc_marker = "X"
                player_marker = "0"
                first_marker = "пека"
            else:
                pc_marker = "0"
                player_marker = "X"
                first_marker = "игрок"
            while not check_winner(field):
                if first_marker == "пека":
                    motion_pc(field, marker=pc_marker)
                    last_marker = pc_marker
                    print(show_game_field(field))
                    motion_player(field, marker=player_marker)
                    last_marker = player_marker
                else:
                    motion_player(field, player_marker)
                    last_marker = player_marker
                    print(show_game_field(field))
                    motion_pc(field, pc_marker)
                    last_marker = pc_marker
                if not check_winner(field):
                    print(show_game_field(field))
            if check_winner(field) != "draw":
                print("\nВыиграл: ", last_marker)
            else:
                print("\nничья")
            break
        elif selection == "2":
            print("В разработке")
            break
