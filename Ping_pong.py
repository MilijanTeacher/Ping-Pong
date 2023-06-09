from pygame import *

class GameSprite(sprite.Sprite):
#class constructor
  def __init__(self, player_image, player_x, player_y, width, height, player_speed):
      #call for the class (Sprite) constructor:
      sprite.Sprite.__init__(self)
      #every sprite must store the image property
      self.image = transform.scale(image.load(player_image), (width, height))
      self.speed = player_speed
      #every sprite must have the rect property that represents the rectangle it is fitted in
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#method drawing the character on the window
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#main player class
class Player(GameSprite):
  #method to control the sprite with arrow keys
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < window_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_w] and self.rect.y < window_height - 80:
           self.rect.y += self.speed

back = (200,255,255)
window_width = 600
window_height = 500
mw = display.set_mode((window_width,window_height))
mw.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
