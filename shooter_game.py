#Создай собственный Шутер!

from pygame import *
from random import randint
from time import sleep
mixer.init()
font.init()
font_1 = font.SysFont("Times New Roman",36)
window = display.set_mode ((700, 500))
display.set_caption ("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700,500))
game = True
clock = time.Clock()
FPS = 100
clock.tick(FPS)
speed = 5
mixer.music.load("Fon.mp3")
mixer.music.play()
kick = mixer.Sound("fire.ogg")
font.init()
font = font.SysFont("Times New Roman",70)
finish = False
run = True
propusk = 0
balli = 0
Bullet = sprite.Group()
soul = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x,y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x = x
        self.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def Update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and a.rect.x>5:
            a.rect.x -= speed
        if keys_pressed[K_RIGHT] and a.rect.x<625:
            a.rect.x += speed
        if keys_pressed[K_SPACE]:
            self.fire()
    keys_pressed = key.get_pressed()
    global Bullet
    def fire(self):
        sprite_center_x = self.rect.centerx
        Sprite_top = self.rect.top
        bul = bullet('bullet.png', sprite_center_x, Sprite_top, 1,20,30)
        Bullet.add(bul)

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__(player_image, player_x, player_y, player_speed,x,y)
    def update(self):
        global propusk
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(25,650)
            self.speed = randint(1,2)
            self.rect.y = 10
            propusk += 1
            self.rect.y += self.speed
class Ast(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__(player_image, player_x, player_y, player_speed,x,y)
    def update(self):
        global propusk
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(25,650)
            self.speed = randint(1,2)
            self.rect.y = 10
            self.rect.y += self.speed
class bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__(player_image, player_x, player_y, player_speed,x,y)
        self.x = x
        self.y = y
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.kill()
a = Player('rocket.png', 10, 430, speed,70,80)
b_1 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_2 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_3 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_4 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_5 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
monsters = sprite.Group()
monsters.add(b_1,b_2,b_3,b_4,b_5)
b_1_1 = Ast("asteroid.png", randint(35,620), 10, randint(1,2),70,50)
b_2_1= Ast("asteroid.png", randint(35,620), 10, randint(1,2),70,50)
b_3_1 = Ast("asteroid.png", randint(35,620), 10, randint(1,2),70,50)
asteroids = sprite.Group()
asteroids.add(b_1_1,b_2_1,b_3_1)
while game:
    text_win_ = font_1.render("You win",1,(255,255,255))
    text_lose_ = font_1.render("You lose",1,(255,255,255))  
    if balli >= 30:
        window.blit(text_win_,(100,100))
        sleep(5)
        game = False
    if propusk >= 20:
        window.blit(text_lose_,(100,100)) 
        sleep(5) 
        game = False
    sprites_list_1 = sprite.spritecollide(a, monsters, False)
    sprites_list_2 = sprite.groupcollide(Bullet, monsters, True, True)
    sprites_list_3 = sprite.spritecollide(a, asteroids, True)
    for i in sprites_list_3:
        soul-=1
    if soul <=0:
        window.blit(text_lose_,(50,50)) 
        sleep(5) 
        finish = True   
        game = False
    for i in sprites_list_2:
        balli += 1
        monsters_ =  Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
        monsters.add(monsters_)
    text_soul = font_1.render("Жизни: "+ str(soul),1,(255,255,255))
    text_lose = font_1.render("Пропущено: "+ str(propusk),1,(255,255,255))
    text_win = font_1.render("Подбито: "+ str(balli),1,(255,255,255))
    window.blit(background, (0,0))
    window.blit(a.image,(a.rect.x,a.rect.y))
    window.blit(text_soul,(10,430))
    window.blit(text_lose,(10,10))
    window.blit(text_win,(10,40))
    monsters.draw(window)
    asteroids.draw(window)
    Bullet.draw(window)
    a.Update()
    monsters.update()
    asteroids.update()
    Bullet.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
























#from pygame import *
#mixer.init()
#window = display.set_mode ((700, 500))
#display.set_caption ("Лабиринт")
#background = transform.scale(image.load("background.jpg"), (700,500))
#game = True
#clock = time.Clock()
#FPS = 100
#clock.tick(FPS)
#speed = 1
#mixer.music.load("jungles.ogg")
#mixer.music.play()
#kick = mixer.Sound("kick.ogg")
#money = mixer.Sound("money.ogg")
#direction = "left"
#font.init()
#font = font.Font(None,70)
#finish = False
#class GameSprite(sprite.Sprite):
    #def __init__(self, player_image, player_x, player_y, player_speed):
        #super().__init__()
        #self.image = transform.scale(image.load(player_image), (65,65))
        #self.speed = player_speed
        #self.rect = self.image.get_rect()
        #self.rect.x = player_x
        #self.rect.y = player_y
    #def reset(self):
        #window.blit(self.image,(self.rect.x,self.rect.y))
#class Player(GameSprite):
    #def __init__(self, player_image, player_x, player_y, player_speed):
        #self.image = transform.scale(image.load(player_image), (65,65))
        #self.speed = player_speed
        #self.rect = self.image.get_rect()
        #self.rect.x = player_x
        #self.rect.y = player_y
    #def Update(self):
        #keys_pressed = key.get_pressed()
        #if keys_pressed[K_LEFT] and a.rect.x>5:
            #a.rect.x -= speed
        #if keys_pressed[K_RIGHT] and a.rect.x<625:
            #a.rect.x += speed
        #if keys_pressed[K_UP] and a.rect.y>4:
            #a.rect.y -= speed
        #if keys_pressed[K_DOWN] and a.rect.y<430:
            #a.rect.y += speed
#class Enemy(GameSprite):
    #def __init__(self, player_image, player_x, player_y, player_speed):
        #super().__init__(player_image, player_x, player_y, player_speed)
    #def Update(self):
        #global direction
        #if self.rect.x <= 150 :
            #direction = "right"
        #if self.rect.x >= 470:
            #direction = "left"
        #if direction == "left":
            #self.rect.x -= self.speed
        #else:
            #self.rect.x += self.speed
#class Wall(sprite.Sprite):
    #def __init__(self,color_1,color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        #super().__init__()
        #self.color_1 = color_1
        #self.color_2 = color_2
        #self.color_3 = color_3
        #self.width = wall_width
        #self.height = wall_height
        #self.image = Surface((self.width,self.height))
        #self.image.fill((color_1,color_2,color_3))
        #self.rect = self.image.get_rect()
        #self.rect.x = wall_x
       # self.rect.y = wall_y  
    #def draw_wall(self):
        #window.blit(self.image,(self.rect.x, self.rect.y))          
#a = Player('hero.png', 20, 300, speed)
#b = Enemy("cyborg.png", 150, 350, speed)
#d = GameSprite("treasure.png", 600, 400, speed)
#s_1 = Wall(255,0,102,100,100,30,600)
#s_2 = Wall(255,0,102,350,0,30,350)
#s_3 = Wall(255,0,102,550,100,30,600)
#while game:
    #if finish != True:
        #window.blit(background, (0,0))
        #window.blit(a.image,(a.rect.x,a.rect.y))
        #window.blit(b.image,(b.rect.x,b.rect.y))
       # window.blit(d.image,(d.rect.x,d.rect.y))
        #s_1.draw_wall()
        #s_2.draw_wall()
       # s_3.draw_wall()
       # a.Update()
       # b.Update()
        #if sprite.collide_rect(a, d):
           # finish = True
            #money.play()
           # win = font.render("YOU WIN!",True,(255,215,0))
            #window.blit(win,(200,200))
        #if sprite.collide_rect(a, b) or sprite.collide_rect(a, s_1) or sprite.collide_rect(a, s_2) or sprite.collide_rect(a, s_3):
            #finish = True
            #kick.play()
            #win = font.render("YOU LOSE!", True,(255,215,0))
           # window.blit(win,(200,200))
    #for e in event.get():
        #if e.type == QUIT:
           # game = False
    #display.update()