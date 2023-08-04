import pygame as pg
import firebaseRW as fiba
import os, sys
from pathlib import Path
import colors as clr
os.chdir(Path(__file__).parent)

pg.init()

monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]

# set the path for the text file to be saved
file_path = os.path.join(os.path.expanduser('~'), 'Pentis', 'username.txt')

# check if the file exists, if not create it
if not os.path.exists(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    print(file_path)
    with open(file_path, 'w') as f:
        f.write('Norbert Noname')


if getattr(sys, 'frozen', False):

    base_path = sys._MEIPASS
else:

    base_path = os.path.abspath(".")


 

def fileRead():
    datei=open(file_path,"r",encoding='utf-8')
    str = datei.read()
    print("username in fileRead(): " + str)
    return str

def fileWrite(username):
    data=open("username.txt","w")
    data.write(username)

def fileWrite2(username_path, username):
    data=open(username_path,"w")
    data.write(username)

def inputBox():
    # Set up the screen
    screen_width = monitor_size[0] * 0.3            # 320
    screen_height = monitor_size[1] * 0.1          # 240

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Input Username")

    strOut = "Please type your username  (->Enter):"
    # Set up the font
    font = pg.font.Font(None, 32)

    # Set up the text input box
    input_box = pg.Rect(screen_width * 0.1, screen_height * 0.4, 200, 32)
    input_text = ''

    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Store the user's input when they press enter
                    
                    username = input_text
                    fileWrite(username)
                    input_text = ''
                    
                    print("Username changed: " + username)
                    running = False
                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                else:
                    # Add the character to the input text
                    input_text += event.unicode
        
        # Draw the screen
        screen.fill((255, 255, 255))
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.1, screen_height * 0.1))
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
    return username

def inputBox2():
    # Set up the screen
    screen_width = monitor_size[0] * 0.3            # 320
    screen_height = monitor_size[1] * 0.1          # 240

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Input Username")

    strOut = "Please type your own username  (->Enter):"
    # Set up the font
    font = pg.font.Font(None, 32)

    # Set up the text input box
    input_box = pg.Rect(screen_width * 0.1, screen_height * 0.4, 200, 32)
    input_text = ''

    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Store the user's input when they press enter
                    
                    username = input_text
                    #username_path = os.path.join(file_path, "username.txt")
                    fileWrite2(file_path, username)
                    input_text = ''
                    
                    print("Username changed: " + username)
                    print("Userpath changed: " + file_path)
                    running = False
                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character when the user presses backspace
                    input_text = input_text[:-1]
                else:
                    # Add the character to the input text
                    input_text += event.unicode
        
        # Draw the screen
        screen.fill((255, 255, 255))
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.1, screen_height * 0.1))
        pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)
    return username
    
def highscoreBox():
    # Set up the screen
    
    screen_width = monitor_size[0] * 0.5
    screen_height = monitor_size[1] * 0.45
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Pentis Scoreboard")
    scores = fiba.getHighscores()

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(None, 45)
    font2 = pg.font.Font(None, 32)
    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        #scores = fiba.getHighscores()
        nameTitle = "Name"
        text_surface = font.render(nameTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.2, screen_height * 0.05))
        scoreTitle = "Score"
        text_surface = font.render(scoreTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.7, screen_height * 0.05))
        
        for i in range(len(scores)):
            
            text_surface = font2.render(str(i+1), True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.05, screen_height * 0.15 + screen_height * 0.08*i))
            
            strOut = scores[i]["name"]
            text_surface = font2.render(strOut, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.2, screen_height * 0.15 + screen_height * 0.08*i))

            strOut2 = str(scores[i]["score"])
            text_surface = font2.render(strOut2, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.7, screen_height * 0.15 + screen_height * 0.08*i))    
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)

def highscoreBox20():
    # Set up the screen
    
    screen_width = monitor_size[0] * 0.5
    screen_height = monitor_size[1] * 0.7
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Pentis Scoreboard")
    scores = fiba.getHighscores20()

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(None, 45)
    font2 = pg.font.Font(None, 32)
    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        #scores = fiba.getHighscores()
        nameTitle = "Name"
        text_surface = font.render(nameTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.2, screen_height * 0.03))
        scoreTitle = "Score"
        text_surface = font.render(scoreTitle, True, (0, 0, 0))
        screen.blit(text_surface, (screen_width * 0.7, screen_height * 0.03))
        
        for i in range(len(scores)):
            
            text_surface = font2.render(str(i+1), True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.05, screen_height * 0.1 + screen_height * 0.042*i))
            
            strOut = scores[i]["name"]
            text_surface = font2.render(strOut, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.2, screen_height * 0.1 + screen_height * 0.042*i))

            strOut2 = str(scores[i]["score"])
            text_surface = font2.render(strOut2, True, (0, 0, 0))
            screen.blit(text_surface, (screen_width * 0.7, screen_height * 0.1 + screen_height * 0.042*i))    
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)

def infoBox(strOut):
    # Set up the screen

    screen_width = 800
    screen_height = 600
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Show Highscores")

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)
    font = pg.font.Font(None, 32)

    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(strOut, True, (0, 0, 0))
        screen.blit(text_surface, (50, 50))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)  

def keyBox():
    
    pg.init()

    # Set up the screen
    screen_width = monitor_size[0] * 0.5
    screen_height = monitor_size[1] * 0.45
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Info Box")

    #strOut = "Please type your online username for the highscore list"
    # Set up the font
    
    #input_box = pg.Rect(50, 50, 200, 32)

    #font = pg.font.Font(None, 32)

    
    # Set up the loop variables
    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
                if event.key == pg.K_ESCAPE:
                    running = False                    
        
        # Draw the screen
        screen.fill((255, 255, 255))
        #pg.draw.rect(screen, (0, 0, 0), input_box, 2)
        
        textSurface_update = pg.font.SysFont('Consolas', 35).render(f'There has been a Pentis update', False, (clr.blk))
        textSurface_update_bg = pg.font.SysFont('Consolas', 35).render(f'There has been a Pentis update', False, (clr.gry1))        
        
        textSurface_score = pg.font.SysFont('Consolas', 35).render(f'Please download the new version of Pentis', False, (clr.blk))
        textSurface_score_bg = pg.font.SysFont('Consolas', 35).render(f'Please download the new version of Pentis', False, (clr.gry1))
        textSurface_url = pg.font.SysFont('Consolas', 33).render(f'https://grapefruit256.itch.io/pentis', False, (clr.blk))
        textSurface_url_bg = pg.font.SysFont('Consolas', 33).render(f'https://grapefruit256.itch.io/pentis', False, (clr.gry2))
        textSurface_enter = pg.font.SysFont('Consolas', 30).render(f'Press Enter to quit', False, (clr.blk))
        textSurface_enter_bg = pg.font.SysFont('Consolas', 30).render(f'Press Enter to quit', False, (clr.gry3))

        screen.blit(textSurface_update_bg,((screen_width - textSurface_update_bg.get_width())//2, screen_height//3+1))
        screen.blit(textSurface_update,((screen_width - textSurface_update.get_width()) //2, screen_height//3))

        screen.blit(textSurface_score_bg,((screen_width - textSurface_score_bg.get_width())//2, screen_height//3+51))
        screen.blit(textSurface_score,((screen_width - textSurface_score.get_width()) //2, screen_height//3 + 50))
        screen.blit(textSurface_url_bg,((screen_width - textSurface_url_bg.get_width()) //2, screen_height//3 +121))
        screen.blit(textSurface_url,((screen_width - textSurface_url.get_width()) //2, screen_height//3 +120))
        screen.blit(textSurface_enter_bg,((screen_width - textSurface_enter_bg.get_width()) //2, screen_height//3 +191))
        screen.blit(textSurface_enter,((screen_width - textSurface_enter.get_width()) //2, screen_height//3 +190))
        pg.display.update()
        
        # Limit the frame rate
        clock.tick(30)  

#highscoreBox()
#keyBox()


pg.quit()