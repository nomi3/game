class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 0
        self.defense = False
        self.offense = False

    def charge(self):
        self.defense = False
        self.offense = False
        self.energy += 1
        print(f"{self.name}はエネルギーを1溜めた")

    def attack(self, other):
        self.defense = False
        self.offense = True
        print(f"{self.name}は{other.name}に攻撃した")
        self.energy -= 1

    def defend(self):
        self.defense = True
        self.offense = False
        print(f"{self.name}は防御した")

def play_game(player1, player2):
    while True:
        while True:
            action1 = input(f"{player1.name}のターン。攻撃(a)、防御(d)、チャージ(c)を入力してください")
            if action1 == "a":
                if player1.energy < 1:
                    print(f"{player1.name}はエネルギーが足りないので攻撃できない")
                else:
                    player1.attack(player2)
                    break
            elif action1 == "d":
                player1.defend()
                break
            elif action1 == "c":
                player1.charge()
                break

        while True:
            action2 = input(f"{player2.name}のターン。攻撃(a)、防御(d)、チャージ(c)を入力してください")
            if action2 == "a":
                if player2.energy < 1:
                    print(f"{player2.name}はエネルギーが足りないので攻撃できない")
                else:
                    player2.attack(player1)
                    break
            elif action2 == "d":
                player1.defend()
                break
            elif action2 == "c":
                player2.charge()
                break

        if player1.offense and player2.offense:
            print("相打ち！")
        elif player1.offense and player2.defense:
            print(f"{player1.name}の攻撃を{player2.name}は防いだ！")
        elif player2.offense and player1.defense:
            print(f"{player2.name}の攻撃を{player1.name}は防いだ！")
        elif player1.offense and not player2.defense:
            print(f"{player1.name}の勝利！")
            break
        elif player2.offense and not player1.defense:
            print(f"{player2.name}の勝利！")
            break
# プレイヤーを作成
player1 = Player("プレイヤー1")
player2 = Player("プレイヤー2")

# ゲームを開始
play_game(player1, player2)