
class Game:
    currentPlayer = None

    def __init__(self, word, name1, name2, name3):
        self.word = word  # загаданное слова
        self.hidden_word = "-" * len(word)  # спрятанное слово

        # картежи вида: имя, поинты
        self.users = [[name1, 0], [name2, 0], [name3, 0]]

        self.currentPlayer = 0

    def step(self, r):
        # ссылка на правила https://tvfan.fandom.com/wiki/%D0%9F%D0%BE%D0%BB%D0%B5_%D1%87%D1%83%D0%B4%D0%B5%D1%81
        # BDD сценарий: при использовании барабана,
        # должно возращаться кол-во очков (1-10), П(сектор приз, 11), +(открыть любую букву, 12), Б(очки сгорают,
        # ход переходит следующему игроку, 13), ->(переход, 14), 0(пропуск хода, 0), x2 (удвоение, 15)
        if r == 0:
            return "0"
        elif r <= 10:
            return str(r * 100)
        elif r == 11:
            return "П"
        elif r == 12:
            return "+"
        elif r == 13:
            return "Б"
        elif r == 14:
            return "->"
        else:
            return "x2"
        # переход хода

    def prise(self, ans):
        #Сценарий: Когда выпадает сектор приз, я выбираю приз или деньги, получаю приз или деньги
        if ans.lower() == "приз":
            return "Вы выиграли солому"
        elif ans.lower() == "деньги":
            return "Подавитесь 30 серебрянниками"
        else:
            return "Мутный вы, держите рубль"

    def change_player(self):
        self.currentPlayer = (self.currentPlayer + 1) % 3

    def guess_letter(self, s):
        # заглушка, допишите логику. Возращает кол-во совпадений, изменяет self.hidden_word
        return True

    def giveletter(self, ans):
        # выводит букву под номером ans у загаданного слова
        print("ывыыууууыыыыууы")

    def X2(self):
        self.users[self.currentPlayer][1] *= 2
        print("Очки: ", self.users[self.currentPlayer][1])