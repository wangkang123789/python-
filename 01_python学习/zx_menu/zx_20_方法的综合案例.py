import random


class Game:
    # 类属性 历史最高分
    top_score = 0

    # 类方法就是专门针对类属性的一个方法，专门来服务类属性的
    @classmethod
    def show_top_score(cls):
        print("当前游戏的历史最高分是 %d" % cls.top_score)

    @staticmethod
    def show_help():
        print("let me help you")

    def __init__(self, player_name):
        self.player_name = player_name


    def start_game(self):
        print("%s 要开始玩游戏啦..." % self.player_name)
        score = random.randint(60, 100)
        print("游戏结束，%s 的得分是 %d" % (self.player_name, score))
        if score > Game.top_score:
            Game.top_score = score


ming = Game("小明")
ming.start_game()
Game.show_top_score()

fang = Game("小芳")
fang.start_game()
Game.show_top_score()

wei = Game("阿伟")
wei.start_game()
Game.show_top_score()