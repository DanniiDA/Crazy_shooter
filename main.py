from pygame import *
from random import randint
import time as time_module

lost = 0
killed = 0

start_time = 0

num_fire = 0
rel_time = False

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if key_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed

    def fire_sus(self):
        bullet = Bullet('b.png',  self.rect.centerx - 7, self.rect.top, 5, 60, 60)
        pyli.add(bullet)

class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = randint(0,10)
            self.rect.x = randint(20,680)
            global lost
            lost += 1




class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 1:
            self.kill()






clock = time.Clock()
window = display.set_mode((700,500))
background = transform.scale(image.load('fon.webp'), (700, 500))

player = Player('sus.png', 200, 450, 10, 50, 50)

karambit = Bullet('b.png',  200, 300, 5, 15, 20)

enemy = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
enemy2 = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
enemy3 = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
enemy4 = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
enemy5 = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
enemy6 = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,2), 70, 70)

vragi = sprite.Group()
vragi.add(enemy)
vragi.add(enemy2)
vragi.add(enemy3)
vragi.add(enemy4)
vragi.add(enemy5)
vragi.add(enemy6)

pyli = sprite.Group()

asteroid = Enemy('asteroid.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
asteroid2 = Enemy('asteroid.png', randint(0, 700-65), 0, randint(1,2), 70, 70)
asteroid3 = Enemy('asteroid.png', randint(0, 700-65), 0, randint(1,2), 70, 70)

abobus = sprite.Group()
abobus.add(asteroid)
abobus.add(asteroid2)
abobus.add(asteroid3)


game = True

finish = False

font.init()
mixer.init()
mixer.music.load('inecraft_excuse.ogg')
mixer.music.play(-1)


font = font.SysFont('Arial', 25)

bot = font.render('You are  проиграли', True, (255, 0, 255))
xarosh = font.render('You are  выиграли', True, (255, 0, 255))
text_reload = font.render('перезарядка', True, (255, 0, 255))

while game:
    if finish == False:
        window.blit(background, (0,0))
        player.reset()
        player.update()

        vragi.draw(window)
        vragi.update()
        abobus.draw(window)
        abobus.update()

        text_loser = font.render('пропущенно:'+str(lost),True, (255, 0, 255))
        text_winner = font.render('зарезано:' + str(killed), True, (255, 0, 255))
        window.blit(text_loser,(0,0))
        window.blit(text_winner, (0, 20))
        pyli.draw(window)
        pyli.update()

        spisok_enemies = sprite.groupcollide(vragi, pyli, True, True)
        for enemy in spisok_enemies:
            killed += 1
            enemy228 = Enemy('enemy.png', randint(0, 700-65), 0, randint(1,7), 120, 120)
            vragi.add(enemy228)


        if sprite.spritecollide(player, vragi, False):
            finish = True
            window.blit(bot, (200, 200))

        if killed >= 10:
            finish = True
            window.blit(xarosh, (200, 200))

        if lost >= 3:
            finish = True
            window.blit(bot, (200, 200))

    end_time = time_module.time()
    if int(end_time - start_time) < 3:
        window.blit(text_reload, (200, 400))
    else:
        rel_time = False

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 30 and rel_time == False:
                    player.fire_sus()
                    num_fire += 1
                if num_fire >= 100 and rel_time == False:
                    rel_time = True
                    start_time = time_module.time()
                    num_fire = 0







    display.update()
    clock.tick(60)
