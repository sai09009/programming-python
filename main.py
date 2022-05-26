!pip install pygame 
import pygame
from pygame.locals import *
import random
import json
# file = 'Fluffing-a-Duck.mp3'
file = 'Fluffing-a-Duck.mp3'
name = input("Enter your Name: ")
if name != "":
    pygame.init()
    pygame.mixer.init()


    clock = pygame.time.Clock()
    fps = 60

    screen_width = 864
    screen_height = 936

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Flappy Bird')

    #define font
    font = pygame.font.SysFont('Bauhaus 93', 60)

    #define colours
    white = (255, 255, 255)

    #define game variables
    ground_scroll = 0
    scroll_speed = 4
    flying = False
    game_over = False
    pipe_gap = 150
    pipe_frequency = 1500 #milliseconds
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    score = 0
    pass_pipe = False
    high_scores = []



        
        


    #load images
    bg = pygame.image.load('img/bg.png')
    ground_img = pygame.image.load('img/ground.png')
    button_img = pygame.image.load('img/restart.png')
    cancel_img = pygame.image.load('img/cancel.png')


    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))


    def reset_game():
        pipe_group.empty()
        flappy.rect.x = 100
        flappy.rect.y = int(screen_height / 2)
        score = 0
        highscores_visible = True
        return score





    class Bird(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            self.index = 0
            self.counter = 0
            for num in range(1, 4):
                img = pygame.image.load(f'img/bird{num}.png')
                self.images.append(img)
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.clicked = False

        def update(self):

            if flying == True:
                #gravity
                self.vel += 0.5
                if self.vel > 8:
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)

            if game_over == False:
                #jump
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                #handle the animation
                self.counter += 1
                flap_cooldown = 5

                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                self.image = self.images[self.index]

                #rotate the bird
                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
            else:
                self.image = pygame.transform.rotate(self.images[self.index], -90)



    class Pipe(pygame.sprite.Sprite):
        def __init__(self, x, y, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('img/pipe.png')
            self.rect = self.image.get_rect()
            #position 1 is from the top, -1 is from the bottom
            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
            if position == -1:
                self.rect.topleft = [x, y + int(pipe_gap / 2)]

        def update(self):
            self.rect.x -= scroll_speed
            if self.rect.right < 0:
                self.kill()


    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):

            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #check if mouse is over the button
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    action = True

            #draw button
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action
    class Button2():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):

            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #check if mouse is over the button
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:

                    pygame.quit()

            #draw button
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action

    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()

    flappy = Bird(100, int(screen_height / 2))

    bird_group.add(flappy)

    #create restart button instance
    button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)
    button2 = Button2(screen_width // 2 - 50, screen_height // 2 - 50, cancel_img)

    #highscore display

    text_file = open("score.txt", "r")
    whole_thing = text_file.readlines()
    print(type(whole_thing))
    print(whole_thing)



    background_color = (220, 247, 247)

    highscore_surface = pygame.Surface((300, 400))
    highscore_surface.fill((90, 100, 120))

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    def scorelist():
        # Screen caption
        pygame.display.set_caption("")
        font_color=(0,150,250)
        font_obj=pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf",20)
        # Render the objects
        count = 0
        
        for i in whole_thing:
            i.split('\n')
            text_obj=font_obj.render(str(i),True,font_color)
            count+=1

            screen.blit(text_obj,(300,30*count+5))


    highscores_visible = True
    def highscoredisplay():
        if highscores_visible:
            highscore_surface.fill((200, 100, 120))
            for i, (key, value) in enumerate(high_scores):
                    text = myfont.render('{} {}'.format(name, score), True, (0, 0, 0))
                    
                    # highscore_surface.blit(text, (50, 30*i+5))
                    
                

        
            if highscores_visible:
                screen.blit(highscore_surface, (290, 250))
                scorelist()
                
               

    text_file.close()

    dialogue = font.render('Do you want to play again?', True, green, blue)
    
        # create a rectangular object for the
        # text surface object
    textRect = dialogue.get_rect()
        
        # set the center of the rectangular object.
    textRect.center = (screen_width // 2, screen_height // 1.5)
    # scorelist


    run = True
    while run:
        clock.tick(fps)

    
        #draw background
        screen.blit(bg, (0,0))

        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)

        #draw the ground
        screen.blit(ground_img, (ground_scroll, 768))

        
        
        #display highscore
        highscoredisplay()

        #check the score
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False


        draw_text("         score: " + str(score), font, white, int(screen_width / 2), 20)

        #look for collision
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            game_over = True

        #check if bird has hit the ground
        if flappy.rect.bottom >= 768:
            game_over = True
            flying = False


        if game_over == False and flying == True:

            #generate new pipes
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
                top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now


            #draw and scroll the ground
            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0

            pipe_group.update()


        #check for game over and reset
        if game_over == True:
            

            highscores_visible = True
            highscoredisplay()
            

            
        
            if button.draw() == True:
                # Append-adds at last
                high_scores = [(name, score)]
                # scorefile = open("score.txt", "a")  # append mode
                # scorefile.write(str(high_scores))
                # scorefile.write("\n")
                # scorefile.close()
                
                
                game_over = False
                score = reset_game()
            button2.draw()
            screen.blit(dialogue, textRect)
            
       

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                flying = True
                highscores_visible = False
                pygame.mixer.music.load(file)
                pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
            
        
    
    

        pygame.display.update()

    def savescore():
           # open file in write mode
        save_name = name.title()
        save_score = score

        last_high_score = 0

        #look for highscore
        try:
            text_file = open("highscores.txt", "r")
            for line in text_file.readlines():
                #you can use regular expressions here to simplify the lookup

                #get the las part of the score assuming the pattern:
                #"text[ has a score of] score"

                line_parts = line.split(" has a score of ")
                if len(line_parts) > 1:
                    #removing the end \n character
                    line_parts = line_parts[-1].split("\n")
                    score = line_parts[0]
                    #compare the last high score with the newest
                    if score.isdigit() and int(score) > last_high_score:
                        last_high_score = int(score)
        except Exception:
            #the first time trows an exception because the high score file           
            pass
        #unban user14762509 moderator fags


        #check if there is a new high score
        if int(save_score) > last_high_score:
            text_file = open("score.txt", "a")
            text_file.write("\n"+save_name+' has '+str(save_score))
            text_file.close()

    
    savescore()
    pygame.quit()
else:
    print("please enter your name")