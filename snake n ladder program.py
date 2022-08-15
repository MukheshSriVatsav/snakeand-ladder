import pygame as py
import random
import time

py.init()

screen = py.display.set_mode((812, 612))
py.display.set_caption("Snakes And Ladders")

pygame_icon = py.image.load('logo.jpg')
py.display.set_icon(pygame_icon)

background_img = py.image.load("SnakesAndLadders.jpg")
stg = py.image.load("playground.jpeg")
go_img = py.image.load("go_button.png")



first_player = py.image.load("player1.png")
second_player = py.image.load("player2.png")

fx = 100
fy = 251

sx = 100
sy = 362

button = py.Rect(5, 70, 100, 100)

score_font = py.font.SysFont('Ariel', 35)

font1 = py.font.SysFont('Ariel', 30)

font2 = py.font.SysFont('Ariel', 25)

clock = py.time.Clock()

def background():
    screen.blit(stg, (0, 0))
    screen.blit(background_img, (200, 0))
    screen.blit(go_img, (5, 70))

def firstPlayer(x, y):
    screen.blit(first_player,(x, y))

def secondPlayer(x, y):
    screen.blit(second_player,(x, y))

def pickNumber():
    dice_roll = random.randint(1, 6)
    if dice_roll == 1:
        dice = py.image.load("Alea_1.png")
    elif dice_roll == 2:
        dice = py.image.load("Alea_2.png")
    elif dice_roll == 3:
        dice = py.image.load("Alea_3.png")
    elif dice_roll == 4:
        dice = py.image.load("Alea_4.png")
    elif dice_roll == 5:
        dice = py.image.load("Alea_5.png")
    elif dice_roll == 6:
        dice = py.image.load("Alea_6.png")
    return (dice, dice_roll)
        
def players():
    msg1 = font1.render("Player 1", True, (255, 0, 0))
    screen.blit(msg1, [10, 251])
    msg2 = font1.render("Player 2", True, (255, 0, 0))
    screen.blit(msg2, [10, 362])

def roll1():
    msg3 = font2.render("Your Turn", True, (255, 255, 255))
    screen.blit(msg3, [25, 290])

def roll2():
    msg4 = font2.render("Your Turn", True, (255, 255, 255))
    screen.blit(msg4, [25, 400])


running = True

turn = 'red'
while running:
    screen.fill((0, 255, 195))
    background()
    players()

    if turn == 'red':
        roll1()
    else:
        roll2()
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            mouse_pos = py.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice, dice_roll = pickNumber()
                screen.blit(dice, (100, 60))
                print(dice_roll)

            # for Player 1  
            if pickNumber() and turn == 'red':  
                turn = 'blue'       
                if dice_roll == 6 and fx == 100 and fy == 251:
                    fx = 200
                    fy = 547
                    turn = 'red'
                elif fx in range(200, 440) and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * dice_roll)
                elif fx in range(200, 440) and dice_roll == 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * dice_roll)
                    turn = 'red'
                elif fx == 440 and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                     fx = fx + (60 * dice_roll)
                elif fx == 440 and dice_roll == 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 5)
                    fy = fy - 60
                    turn = 'red'
                elif fx == 500 and dice_roll <= 4 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * dice_roll)
                elif fx == 500 and dice_roll > 4 and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 4)
                    fy = fy - 60
                elif fx == 500 and dice_roll == 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 4) - (60 * (dice_roll - 5))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 560 and dice_roll <= 3 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * dice_roll)

                elif fx == 560 and dice_roll > 3 and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 3) - (60 * (dice_roll - 4))
                    fy = fy - 60
                elif fx == 560 and dice_roll == 6 and  (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 3) - (60 * (dice_roll - 4))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 620 and dice_roll <= 2 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * dice_roll)

                elif fx == 620 and dice_roll > 2 and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 2) - (60 * (dice_roll - 3))
                    fy = fy - 60
                elif fx == 620 and dice_roll == 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 2) - (60 * (dice_roll - 3))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 680 and dice_roll == 1 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * dice_roll)

                elif fx == 680 and dice_roll > 1 and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 1) - (60 * (dice_roll - 2))
                    fy = fy - 60
                elif fx == 680 and dice_roll == 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx + (60 * 1) - (60 * (dice_roll - 2))
                    fy = fy - 60
                    turn = 'red'
                elif fx >= 740 and dice_roll != 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx - (60 * (dice_roll - 1))
                    fy = fy - 60
                elif fx == 740 and dice_roll == 6 and (fy == 547 or fy == 427 or fy == 307 or fy == 187 or fy == 67):
                    fx = fx - (60 * (dice_roll - 1))
                    fy = fy - 60
                    turn = 'red'
                



                elif fx > 440 and fx <= 740 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll != 6:
                    fx = fx - (60 * dice_roll)
                elif fx > 440 and fx <= 740 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx - (60 * 5)
                    fy = fy - 60
                elif fx > 500 and fx <= 740 and dice_roll != 6 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7):
                    fx = fx - (60 * dice_roll)
                elif fx > 500 and fx <= 740 and dice_roll == 6 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7):
                    fx = fx - (60 * dice_roll)
                    turn = 'red'
                elif fx == 500 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll != 6:
                    fx = fx - (60 * dice_roll)
                elif fx == 500 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx - (60 * dice_roll)
                    fy = fy - 60
                    turn = 'red'
                elif fx == 440 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll < 5:
                    fx = fx - (60 * dice_roll)
                elif fx == 440 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 5:
                    fx = fx - (60 * 4) + (60 * (dice_roll - 5))
                    fy = fy - 60
                    
                elif fx == 440 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx - (60 * 4) + (60 * (dice_roll - 5))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 380 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll < 4:
                    fx = fx - (60 * dice_roll)
                elif fx == 380 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll >= 4 and dice_roll != 6:
                    fx = fx - (60 * 3) + (60 * (dice_roll - 4))
                    fy = fy - 60
                elif fx == 380 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx - (60 * 3) + (60 * (dice_roll - 4))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 320 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll < 3:
                    fx = fx - (60 * dice_roll)
                elif fx == 320 and fy == 487 and dice_roll >= 3 and dice_roll != 6:
                    fx = fx - (60 * 2) + (60 * (dice_roll - 3))
                    fy = fy - 60
                elif fx == 320 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx - (60 * 2) + (60 * (dice_roll - 3))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 260 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll < 2:
                    fx = fx - (60 * dice_roll)
                elif fx == 260 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll >= 2 and dice_roll != 6:
                    fx = fx - 60  + (60 * (dice_roll - 2))
                    fy = fy - 60
                elif fx == 260 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx - 60 + (60 * (dice_roll - 2))
                    fy = fy - 60
                    turn = 'red'
                elif fx == 200 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll != 6:
                    fx = fx + (60 * (dice_roll - 1))
                    fy = fy - 60
                elif fx == 200 and (fy == 487 or fy == 367 or fy == 247 or fy == 127 or fy == 7) and dice_roll == 6:
                    fx = fx + (60 * (dice_roll - 1))
                    fy = fy - 60
                    turn = 'red'

                if (fx, fy) == (200, 547):
                    fx, fy = 320, 367
                elif (fx, fy) == (380, 547):
                    fx, fy = 560, 487
                elif (fx, fy) == (680, 547):
                    fx, fy = 740, 367
                elif (fx, fy) == (200, 427):
                    fx, fy = 260, 307
                elif (fx, fy) == (620, 427):
                    fx, fy = 380, 67
                elif (fx, fy) == (740, 247):
                    fx, fy = 560, 187
                elif (fx, fy) == (740, 127):
                    fx, fy = 740, 7
                elif (fx, fy) == (200, 127):
                    fx, fy = 200, 7


                elif (fx, fy) == (380, 487):
                    fx, fy = 560, 547 
                elif (fx, fy) == (560, 247):
                    fx, fy = 560, 367
                elif (fx, fy) == (560, 67):
                    fx, fy = 380, 427
                elif (fx, fy) == (620, 7):
                    fx, fy = 620, 127
                elif (fx, fy) == (500, 7):
                    fx, fy = 500, 127
                elif (fx, fy) == (320, 7):
                    fx, fy = 260, 127 

        
                    
            # for Player 2
            
            elif pickNumber() and turn == 'blue':
                turn = 'red'
                if dice_roll == 6 and sx == 100 and sy == 362:
                    sx = 200
                    sy = 547
                    turn = 'blue'
                elif sx in range(200, 440) and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * dice_roll)
                elif sx in range(200, 440) and dice_roll == 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * dice_roll)
                    turn = 'blue'
                elif sx == 440 and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                     sx = sx + (60 * dice_roll)
                elif sx == 440 and dice_roll == 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 5)
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 500 and dice_roll <= 4 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * dice_roll)
                elif sx == 500 and dice_roll > 4 and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 4)
                    sy = sy - 60
                elif sx == 500 and dice_roll == 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 4) - (60 * (dice_roll - 5))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 560 and dice_roll <= 3 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * dice_roll)

                elif sx == 560 and dice_roll > 3 and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 3) - (60 * (dice_roll - 4))
                    sy = sy - 60
                elif sx == 560 and dice_roll == 6 and  (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 3) - (60 * (dice_roll - 4))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 620 and dice_roll <= 2 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * dice_roll)

                elif sx == 620 and dice_roll > 2 and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 2) - (60 * (dice_roll - 3))
                    sy = sy - 60
                elif sx == 620 and dice_roll == 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 2) - (60 * (dice_roll - 3))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 680 and dice_roll == 1 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * dice_roll)

                elif sx == 680 and dice_roll > 1 and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 1) - (60 * (dice_roll - 2))
                    sy = sy - 60
                elif sx == 680 and dice_roll == 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx + (60 * 1) - (60 * (dice_roll - 2))
                    sy = sy - 60
                    turn = 'blue'
                elif sx >= 740 and dice_roll != 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx - (60 * (dice_roll - 1))
                    sy = sy - 60
                elif sx == 740 and dice_roll == 6 and (sy == 547 or sy == 427 or sy == 307 or sy == 187 or sy == 67):
                    sx = sx - (60 * (dice_roll - 1))
                    sy = sy - 60
                    turn = 'blue'
                



                elif sx > 440 and sx <= 740 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll != 6:
                    sx = sx - (60 * dice_roll)
                elif sx > 440 and sx <= 740 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx - (60 * 5)
                    sy = sy - 60
                elif sx > 500 and sx <= 740 and dice_roll != 6 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7):
                    sx = sx - (60 * dice_roll)
                elif sx > 500 and sx <= 740 and dice_roll == 6 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7):
                    sx = sx - (60 * dice_roll)
                    turn = 'blue'
                elif sx == 500 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll != 6:
                    sx = sx - (60 * dice_roll)
                elif sx == 500 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx - (60 * dice_roll)
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 440 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll < 5:
                    sx = sx - (60 * dice_roll)
                elif sx == 440 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 5:
                    sx = sx - (60 * 4) + (60 * (dice_roll - 5))
                    sy = sy - 60
                    
                elif sx == 440 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx - (60 * 4) + (60 * (dice_roll - 5))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 380 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll < 4:
                    sx = sx - (60 * dice_roll)
                elif sx == 380 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll >= 4 and dice_roll != 6:
                    sx = sx - (60 * 3) + (60 * (dice_roll - 4))
                    sy = sy - 60
                elif sx == 380 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx - (60 * 3) + (60 * (dice_roll - 4))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 320 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll < 3:
                    sx = sx - (60 * dice_roll)
                elif sx == 320 and sy == 487 and dice_roll >= 3 and dice_roll != 6:
                    sx = sx - (60 * 2) + (60 * (dice_roll - 3))
                    sy = sy - 60
                elif sx == 320 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx - (60 * 2) + (60 * (dice_roll - 3))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 260 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll < 2:
                    sx = sx - (60 * dice_roll)
                elif sx == 260 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll >= 2 and dice_roll != 6:
                    sx = sx - 60  + (60 * (dice_roll - 2))
                    sy = sy - 60
                elif sx == 260 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx - 60 + (60 * (dice_roll - 2))
                    sy = sy - 60
                    turn = 'blue'
                elif sx == 200 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll != 6:
                    sx = sx + (60 * (dice_roll - 1))
                    sy = sy - 60
                elif sx == 200 and (sy == 487 or sy == 367 or sy == 247 or sy == 127 or sy == 7) and dice_roll == 6:
                    sx = sx + (60 * (dice_roll - 1))
                    sy = sy - 60 
                    turn = 'blue'


                if (sx, sy) == (200, 547):
                    sx, sy = 320, 367
                elif (sx, sy) == (380, 547):
                    sx, sy = 560, 487
                elif (sx, sy) == (680, 547):
                    sx, sy = 740, 367
                elif (sx, sy) == (200, 427):
                    sx, sy = 260, 307
                elif (sx, sy) == (620, 427):
                    sx, sy = 380, 67
                elif (sx, sy) == (740, 247):
                    sx, sy = 560, 187
                elif (sx, sy) == (740, 127):
                    sx, sy = 740, 7
                elif (sx, sy) == (200, 127):
                    sx, sy = 200, 7


                elif (sx, sy) == (380, 487):
                    sx, sy = 560, 547 
                elif (sx, sy) == (560, 247):
                    sx, sy = 560, 367
                elif (sx, sy) == (560, 67):
                    sx, sy = 380, 427
                elif (sx, sy) == (620, 7):
                    sx, sy = 620, 127
                elif (sx, sy) == (500, 7):
                    sx, sy = 500, 127


                





    
    firstPlayer(fx, fy)
    secondPlayer(sx, sy)
    py.display.update()
    time.sleep(1.3)

    if fx == 200 and fy == 7:
        screen.fill((50, 153, 213))
        value = score_font.render("Player 1 Won", True, (255, 255, 102))
        screen.blit(value, [250, 200])
        running = False
    if sx == 200 and sy == 7:
        screen.fill((50, 153, 213))
        value = score_font.render("Player 2 Won", True, (255, 255, 102))
        screen.blit(value, [250, 200])
        running = False
        
py.quit()
clock.tick(40)
quit()
