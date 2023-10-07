from Game import Game


def test_step():
    test_game = Game("Курица", "Андрей", "Никита", "Александр")
    assert test_game.step(0) == "0"
    assert test_game.step(2) == "200"
    assert test_game.step(4) == "400"
    assert test_game.step(11) == "П"
    assert test_game.step(12) == "+"
    assert test_game.step(13) == "Б"
    assert test_game.step(14) == "->"
    assert test_game.step(15) == "x2"


def test_prise():
    test_game = Game("Курица", "Андрей", "Никита", "Александр")
    assert test_game.prise("приз") == "Вы выиграли солому"
    assert test_game.prise("деньги") == "Подавитесь 30 серебрянниками"
    assert test_game.prise("денЬгИ") == "Подавитесь 30 серебрянниками"
    assert test_game.prise("ыуыу") == "Мутный вы, держите рубль"
