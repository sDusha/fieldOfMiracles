import random

from Game import Game

game = Game("Курица", "Андрей", "Никита", "Александр")


while True:
    field = game.step(random.randint(1, 1024) % 16)
    print("На барабане сектор:", field)
    if field == "П":
        game.prise(input("Приз или деньги? "))
    elif field == "x2":
        game.X2()
    #сюда свои функции
    game.change_player()
