import pygame
import random
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

pygame.init
pygame.font.init()

game_width = 800
game_height = 600
block_size = 20
apple_size = 30
FPS = 30
img = pygame.image.load('snake_head.png')
img_apple = pygame.image.load('apple.png')

direction = 'up'

clock = pygame.time.Clock()

game_display = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('snake')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)

def create_snake(snake_list): #codes for snake function=====================================================================

    if direction == 'up':
        head = img

    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)

    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)

    elif direction == 'right':
        head = pygame.transform.rotate(img, 270)



    game_display.blit(head, (snake_list[-1][0], snake_list[-1][1]))
 
    for list in snake_list[1:-1]:
        pygame.draw.rect(game_display, green, [list[0], list[1], block_size, block_size])
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# message to screen============================================================================================================
smallfont = pygame.font.SysFont('comicsansms', 15)
medfont = pygame.font.SysFont('comicsansms', 18)
bigfont = pygame.font.SysFont('comicsansms', 50)

def for_score(text, color):
    message_surf = smallfont.render (text, True, color)
    game_display.blit(message_surf, [0,0])

def for_highscore(text, color):
    message_surf = smallfont.render (text, True, color)
    game_display.blit(message_surf, [0, 15])



def text_objects(text, color, size):
    if size == 'small':
        message_surf = smallfont.render(text, True, color)
    elif size == 'medium':
        message_surf = medfont.render(text, True, color)
    elif size == 'big':
        message_surf = bigfont.render(text, True, color)
    return message_surf, message_surf.get_rect()


def message_to_screen(msg, color, y_displace=0, size = 'medium'):
    #message = font.render(msg, True, color)
    #game_display.blit(message, [game_width/2, game_height/2])
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (game_width/2, (game_height/2)+y_displace)
    game_display.blit(text_surf, text_rect)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def game_intro():
    intro = True
    while intro:
        game_display.fill(white)
        message_to_screen('SNAKE',
                              green,
                              -110,
                              'big')
        message_to_screen('eat apples, get bigger',
                              blue,
                              -70,
                              'medium')
        message_to_screen('press "s" to start or "q" to quit the game',
                              green,
                              -30,
                              'medium')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        
def game_loop(): #the game function==============================================================================================
    global direction

    lead_x = game_width/2
    lead_y = game_height/2
    lead_x_change = 0
    lead_y_change = -10
    game_exit = False
    game_over = False
    apple_x = round(random.randrange(0, game_width-(apple_size-1)))#/20.0)*20.0
    apple_y = round(random.randrange(0, game_height-(apple_size-1)))#/20.0)*20.0
    snake_list = [[game_width/2+block_size, game_height/2+block_size],
                  [game_width/2+block_size*2, game_height/2+block_size*2],
                  [game_width/2+block_size*3, game_height/2+block_size*3],
                  [game_width/2+block_size*4, game_height/2+block_size*4],
                  [game_width/2+block_size*5, game_height/2+block_size*5]]
                  
    snake_length = 5
    count = 0
    fhand1 = open('score.txt')
    for q in fhand1:
        w = q

    while not game_exit:

        while game_over == True:
            fhand = open('score.txt')
            for y in fhand:
                if count < int(y):#if your score is lower than current highscore--------------------------------------------------------------
                    game_display.fill(white)
                    message_to_screen('GAMEOVER', red, -100,
                                      'big')
                    message_to_screen('YOUR SCORE: '+str(count)+',    HIGHSCORE: '+y.rstrip('\n')+',    press "C" to continue and "Q" to quit the game',
                                      red)
                    pygame.display.update()

                    #fhand = open('score.txt','a')
                    #fhand.write(str(count)+'\n')
                    #fhand.close()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                           
                            game_exit = True
                            game_over = False
                            
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_exit = True
                                game_over = False

                            if event.key == pygame.K_c:
                                game_loop()
                #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                
                                
                if count > int(y):#if your score is higher than current highscore--------------------------------------------------------------
                    game_display.fill(white)
                    message_to_screen('BRAVO',
                                      red,
                                      -100,
                                      'big')
                    message_to_screen('NEW HIGHSCORE: '+str(count)+', press "C" to continue and "Q" to quit the game', red)
                    pygame.display.update()

                    #fhand = open('score.txt','a')
                    #fhand.write(str(count)+'\n')
                    #fhand.close()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_exit = True
                            game_over = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_exit = True
                                game_over = False
                                #------------------
                                fhand = open('score.txt')
                                for x in fhand:
                                    fhand = open('score.txt','w')
                                    fhand.write(str(count)+'\n')
                                    fhand.close()
                                #--------------------
                            if event.key == pygame.K_c:
                                fhand = open('score.txt')
                                for x in fhand:
                                    fhand = open('score.txt','w')
                                    fhand.write(str(count)+'\n')
                                    fhand.close()
                                game_loop()
                #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                if count == int(y):#if your score is equal to current highscore--------------------------------------------------------------
                    game_display.fill(white)
                    message_to_screen('WELLDONE',
                                      red,
                                      -100,
                                      'big')
                    message_to_screen('YOU HAVE EQUALLED THE HIGHSCORE: '+str(count)+', press "C" to continue and "Q" to quit the game', red)
                    pygame.display.update()

                    #fhand = open('score.txt','a')
                    #fhand.write(str(count)+'\n')
                    #fhand.close()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_exit = True
                            game_over = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_exit = True
                                game_over = False

                            if event.key == pygame.K_c:
                                fhand = open('score.txt')
                                game_loop()
                #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "down":
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != "up":
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = 'down'
                elif event .key == pygame.K_LEFT and direction != "right":
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != "left":
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = 'right'

        lead_x += lead_x_change
        lead_y += lead_y_change

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        for location in snake_list:
            if apple_x == snake_head[0] and apple_y == snake_head[1]:
                apple_x = random.randrange(0, game_width)
                apple_y = random.randrange(0, game_height)



        game_display.fill(white)
        for_score('Your Score: '+str(count), blue)#score display-----------------------------------------------------
        for_highscore('HighScore: '+str(w).rstrip('\n'), blue)#highscore display--------------------------------------------------------

        game_display.blit(img_apple, (apple_x, apple_y)) #apple code================================
        create_snake(snake_list) #calling snake function===========================================================================
        pygame.display.update()
        clock.tick(FPS)

        if lead_x >= game_width or lead_x < 0 or lead_y >= game_height or lead_y < 0:
            game_over = True

        #if apple_x == lead_x and apple_y == lead_y:
        #    apple_x = round(random.randrange(0, game_width)/20.0)*20.0
        #    apple_y = round(random.randrange(0, game_height)/20.0)*20.0
        #    snake_length += 1
        
        # eating an apple=============================================================================================================
        if lead_x > apple_x and lead_x < apple_x+apple_size or lead_x+block_size > apple_x and lead_x+block_size < apple_x+apple_size:
            if lead_y > apple_y and lead_y < apple_y+apple_size or lead_y+block_size > apple_y and lead_y+block_size < apple_y+apple_size:
                apple_x = round(random.randrange(0, game_width-(apple_size-1)))#/10.0)*10.0
                apple_y = round(random.randrange(0, game_height-(apple_size-1)))#/10.0)*10.0
                snake_length += 1
                count += 1
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        #to prevent apples on snakes body==============================================================================================
        for coordinates in snake_list:
            if apple_x == coordinates[0] and apple_y == coordinates[1]:
                    apple_y = round(random.randrange(0, game_height-(apple_size-1)))#/20.0)*20.0
                    apple_y = round(random.randrange(0, game_height-(apple_size-1)))#/20.0)*20.0
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                

        #maintaining the snake's length================================================================================================       
        if len(snake_list) > snake_length:
            del snake_list[0]
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


        #snake eating itself===========================================================================================================
        for list in snake_list[:-2]:
            if list == snake_head:
                game_over = True
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        

    pygame.quit()
    quit()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
game_intro()
