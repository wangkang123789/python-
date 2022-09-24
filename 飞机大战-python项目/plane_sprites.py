import random
import pygame
# 关于模块的导入顺序：官方标准模块->第三方模块->应用程序模块

# 游戏主窗口的大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 设置一个创建敌机的事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 设置一个创建子弹的事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT+1


# 创建游戏精灵的基类
class GameSprite(pygame.sprite.Sprite):
    """精灵的基类"""

    def __init__(self, image_name, speed=1):
        """扩展父类的初始化方法"""
        # 调用父类的初始化方法，不需要传参
        super().__init__()

        # 加载图像
        self.image = pygame.image.load(image_name)

        # 设置图像尺寸，这种方法会自动根据载入的图像识别出大小，得到的数据是(0,0,width,height)
        # 默认从左上角出发
        self.rect = self.image.get_rect()

        # 记录速度
        self.speed = speed

    def update(self, *args):
        # 默认在垂直方向进行移动
        self.rect.y += self.speed


# 创建背景精灵
class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        image_name = "C:/Users/wangk/Desktop/python的coding/飞机大战/images/background.png"
        # 调用父类GameSprite的初始化方法
        super().__init__(image_name)

        # 判断是否是交替图片，是，则将修改图片的坐标
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1、调用父类的update方法，因为背景是向下移动的，所以是不用调整speed的
        super().update()
        # 2、判断bg是否出了主窗口
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


# 创建英雄类
class Hero(GameSprite):
    """英雄类"""
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__("./images/me1.png", 0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 120
        self.speed_y = 0
        # 创建子弹组
        self.bullet_group = pygame.sprite.Group()

    def fire(self):
        for i in (1, 2, 3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y-i*20
            bullet.rect.centerx = self.rect.centerx
            # 将子弹加入组里
            self.bullet_group.add(bullet)

    def update(self):
        # 由于飞机是水平方向移动，所以这里就不调用父类的update方法了
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        # TODO 这里我想把飞机的移动不止弄成水平方向的，垂直方向的速度也想加起来

        # 控制英雄运动边界情况
        # 判断左右的运动情况
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        # 判断上下的运动情况
        if self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0


# 敌机类
class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__("./images/enemy1.png")
        # 设置敌机的初始位置
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)
        # 设置敌机的speed
        self.speed = random.randint(1, 3)

    def update(self):
        # 调用父类的update方法，不用对齐进行扩展啥的
        super().update()

        # 判断是否飞出屏幕外
        if self.rect.y > SCREEN_RECT.height:
            self.kill()


# 子弹类
class Bullet(GameSprite):
    """创建子弹"""
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__("./images/bullet1.png", -2)

        # 初始位置,为什么现在设置不了？，因为子弹的初始位置需要依靠英雄的位置作为参考

    def update(self):
        super().update()
        if self.rect.y < -self.rect.height:
            self.kill()
