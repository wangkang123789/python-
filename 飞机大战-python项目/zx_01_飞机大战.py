import pygame

# 初始化
import pygame.display

pygame.init()

# 开始游戏
# 创建游戏主窗口，这个是你的控制界面，后续的加载图片全部是在这个界面的基础上进行的
screen = pygame.display.set_mode((480, 700))

# 绘制背景
# 1>加载背景图片
bg = pygame.image.load("C:/Users/wangk/Desktop/飞机大战/images/background.png")  # python的路径名是反着来的

# 2>将背景图绘制在屏幕上 
screen.blit(bg, (0, 0))

# 创建一个时钟对象
clock = pygame.time.Clock()

# 将我方战机的图片导入，并且定义一个初始位置
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (189, 574))

hero_rect = pygame.Rect(189, 574, 106, 126)

# 3>更新整个屏幕
pygame.display.update()

# 游戏循环
while True:

    # 这个是循环内代码执行的频率，每秒执行60次
    clock.tick(60)

    # 我方战机每次向上移动一个像素
    hero_rect.y -= 1

    # 判断是否战机移出游戏窗口
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700

    """根据之前虚拟出的矩形块，得到了目前我方战机的移动位置，
    重新将我方战机的图片写到窗口上"""

    # 重新将我方战机和窗口写到屏幕上
    # 窗口的重写是用来遮住之前我方战机的移动轨迹的
    screen.blit(bg, (0, 0))
    screen.blit(hero, (hero_rect.x, hero_rect.y))

    # 最后更新一下屏幕
    pygame.display.update()


# 结束并卸载所有模块
pygame.quit()