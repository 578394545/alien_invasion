import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一艘飞船，一个用于存储子弹的编组，一个外星人编组
    ship = Ship(screen,ai_settings)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens,ship)
    
    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship,ai_settings,screen,bullets,stats,play_button,aliens,sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens,bullets,ai_settings,screen, ship,stats,sb)
            gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets,sb)

        #每次循环时都重绘屏幕,让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb)

run_game()