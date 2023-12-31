import pygame.font

class Button():
  def __init__(self, ai_settings, screen, msg) -> None:
    self.screen = screen
    self.screen_rect = screen.get_rect()

    # 设置按钮的尺寸和其他属性
    self.width, self.height = 200, 50
    self.font = pygame.font.Font(ai_settings.bold_font, 24)

    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.screen_rect.center

    self.msg = msg
    self.over_out()
    self.prep_msg()

  def prep_msg(self):
    self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
    self.msg_image_rect = self.msg_image.get_rect()
    self.msg_image_rect.center = self.rect.center

  def draw_button(self):
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.msg_image, self.msg_image_rect)
  
  def over_in(self):
    self.button_color = (0, 122, 0)
    self.text_color = (122, 0, 0)
    self.prep_msg()
  
  def over_out(self): 
    self.button_color = (0, 255, 0)
    self.text_color = (255, 255, 255)
    self.prep_msg()