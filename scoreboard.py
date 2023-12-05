import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard():
  """显示得分信息的类"""
  def __init__(self, ai_settings, screen, stats) -> None:
    """初始化显示得分涉及的属性"""
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.ai_settings = ai_settings
    self.stats = stats

    # 字体设置
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont("youyuan", 48)

    # 初始得分图像
    self.prep_score()
    self.prep_high_score()
    self.prep_level()
    self.prep_ships()

  def prep_score(self) -> None:
    """将得分转换成渲染图像"""
    rounded_score = round(self.stats.score, -1)
    score_str = f"当前得分: {rounded_score:,}"
    self.score_image = self.font.render(score_str, True,self.text_color,self.ai_settings.bg_color)

    # 右上角显示得分数据
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def prep_high_score(self) -> None:
    """将最高分转换成渲染图像"""
    hight_score = round(self.stats.high_score, -1)
    hight_score_str = f"最高得分: {hight_score:,}"
    self.high_score_image = self.font.render(hight_score_str, True,self.text_color,self.ai_settings.bg_color)

    # 右上角显示得分数据
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = 20

  def prep_level(self) -> None:
    """将等级转换成渲染图像"""
    level_str = f"等级: {self.stats.level:,}"
    self.level_image = self.font.render(level_str, True,self.text_color,self.ai_settings.bg_color)

    # 右上角显示得分数据
    self.level_rect = self.level_image.get_rect()
    self.level_rect.right = self.screen_rect.right - 20
    self.level_rect.top = self.score_rect.bottom + 10

  def prep_ships(self) -> None:
    """将飞船量转换成渲染图像"""
    self.ships = Group()
    for ship_number in range(self.stats.ships_left):
      ship = Ship(self.ai_settings, self.screen)
      ship.rect.x = 10 + ship_number * ship.rect.width
      ship.rect.y = 10
      self.ships.add(ship)

  def show_score(self) -> None:
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    self.screen.blit(self.level_image, self.level_rect)
    # 绘制飞船
    self.ships.draw(self.screen)
