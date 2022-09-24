import pygame
from plane_sprites import *


# ps:导入模块的顺序是，系统自带模块->第三方模块->
# 整体的框架：plane_game_main是主文件，
# plane_sprites是一个创建各种精灵的模块


# 将整个游戏都封装成一个类，
class PlaneGame(object):
    """飞机大战的类"""

    def __init__(self):
        """游戏的初始化"""
        # 1> 创建一个游戏窗口，之后的绘制基于此进行
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2> 创建一个时钟的私有属性和一个定时创建用户事件常量的
        self.__clock = pygame.time.Clock()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 800) # 这个常量的作用是，每隔800ms，该事件就发生一次，而且可以被监听到
        pygame.time.set_timer(CREATE_BULLET_EVENT, 500)
        # 3> 创建精灵组
        self.__create_sprites()

    def __create_sprites(self):
        """创建精灵组"""
        # 精灵组是pygame提供的一个类

        # 1、创建背景精灵组
        self.bg1 = BackGround()
        self.bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(self.bg1, self.bg2)

        # 2、敌机精灵组
        # 敌机的出现是一个定时的事件，所以要设置一个定时事件
        self.enemy_group = pygame.sprite.Group()

        # 3、我方英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 4、子弹组
        # self.bullet_group = pygame.sprite.Group()

    def start_game(self):
        """开始游戏"""
        print("开始游戏...")

        while True:
            # 1> 设置刷新帧率
            self.__clock.tick(60)

            # 2> 事件监听
            self.__event_handle()

            # 3> 碰撞检测
            self.__check_collide()

            # 4> 更新精灵组
            self.__update_sprites()

    def __event_handle(self):
        """事件监听"""
        # 这个可以将键盘的按键以列表的方式进行返回
        for event in pygame.event.get():
            # 这个QUIT就是界面的那个叉叉
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            elif event.type == CREATE_BULLET_EVENT:
                self.hero.fire()


        # 获取用户按键
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed_y = -2
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed_y = 2
        else:
            self.hero.speed = 0
            self.hero.speed_y = 0


    def __check_collide(self):
        """碰撞检测"""
        # TODO 明天一定要找机会把爆炸图贴上去
        # 1、子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 2、敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        for group in [self.back_group, self.enemy_group, self.hero.bullet_group, self.hero_group]:
            group.update()
            group.draw(self.screen)

        # 呜呜呜这行代码一定要加我哭了
        pygame.display.update()

    @staticmethod
    def __game_over():
        """游戏结束"""
        # 静态方法的调用得用类名.的方式去调用
        print("游戏结束...")
        pygame.quit()
        # exit是用来直接退出程序的，方便最后游戏中死亡
        exit()


# 下面是测试代码，如果是本模块运行，则下方代码会执行；
# 如果是将本模块导入其他py文件中，则下方代码不会实现
if __name__ == "__main__":
    # 创建一个玩飞机大战游戏的对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()
