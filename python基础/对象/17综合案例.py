# 类属性 top_score 记录游戏最高分
# 实例属性 player_name 记录当前游戏玩家的玩家姓名
# 静态方法 show_help 显示游戏的帮助信息
# 类方法 show_top_score 显示历史最高分
# 实例方法 start_game 开始当前玩家的游戏

class Game(object):
    # 类属性
    top_score = 0
    # 类方法
    @classmethod
    def show_top_score(cls):
        print('历史记录 %d ' % cls.top_score)


    def __init__(self,player_name):
        self.player_name = player_name

    def start_game(self):
        print('%s 开始游戏啦' % self.player_name)

    # 静态方法
    @staticmethod
    def show_help():
        print('帮助信息')
# 查看帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象

game = Game('小明')
game.start_game()
