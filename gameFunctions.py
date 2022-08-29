
import sys, os, random, pygame
import time
import gameVariables

def initialize_pygame():
    pygame.init()
    pygame.mixer.init()

    #Opening the window in the center of the screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((gameVariables.screenResolution.current_w - gameVariables.gameWidth) / 2, (gameVariables.screenResolution.current_h - gameVariables.gameHeight) / 2)
    screen = pygame.display.set_mode([gameVariables.gameWidth, gameVariables.gameHeight], pygame.DOUBLEBUF, 32)
    pygame.display.set_icon(pygame.image.load('images/icon.ico'))
    pygame.display.set_caption("Flappy Bird : The Way To Infinity")
    
    return screen

def load_images():
    #- Loading all the images required for the game from the images folder
    #and returning a dictionary of them as following:
       
    #'background_1' : day background
    #'bird' : the bird
    #'bird2' : the bird with the wings down
    #'pipe-up' : the pipe for the upper part
    #'pipe-down' : the pipe for the lower part
    #'ground' : the ground

    def load_image(img_file_name):
        #- Looking for images in the game's images folder (./images/)
        #- Loading the image and then converts it, because it speeds up
        #blitting; returning then the image to the dictionary
        #- For the background image, we load a random one, since we
        #have a day background a night background
        
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background_' + str(random.randint(1, 2)) + '.png'),
            'bird': load_image('bird.png'),
            'bird2': load_image('bird2.png'),    
            'pipe-up2': load_image('pipe-up2.png'),
            'pipe-up1': load_image('pipe-up1.png'), 
            'pipe-down2': load_image('pipe-down2.png'),
            'pipe-down1': load_image('pipe-down1.png'),
            'ground': load_image('ground.png'),
            'point':load_image('points.png')}

def draw_text(screen, text, y_pos, size):
    #Drawing a black text (bigger) and then a white text, smaller
    #over it to get the desired gameScore effect
    font = pygame.font.Font("data/font.TTF", size)
    score_text_b = font.render(str(text), 1, (0, 0, 0))
    score_text_w = font.render(str(text), 1, (255, 255, 255))

    x_pos_b = (gameVariables.gameWidth - score_text_b.get_width()) / 2
    x_pos_w = (gameVariables.gameWidth - score_text_w.get_width()) / 2
    screen.blit(score_text_b, (x_pos_b + 2, y_pos - 1))
    screen.blit(score_text_w, (x_pos_w, y_pos))

def pause(screen,clock):
    loop = 1
    draw_text(screen,"PAUSED", 250, 20)
    draw_text(screen,"Press Space to continue", 300, 20)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        # screen.fill((0, 0, 0))
        clock.tick(60)
        
def end_the_game(screen, gameScore):
    #Draws a rectangle & shows the gameScore & updates the highscore
    pygame.draw.rect(screen, (0, 0, 0), (23, gameVariables.gameHeight / 2 - 77, 254, 154))
    pygame.draw.rect(screen, (239, 228, 150), (25, gameVariables.gameHeight / 2 - 75, 250, 150))
    #draw_text(screen, "Your Score: " + str(gameScore), 200, 20)
    
    f = open("data/highscore", "r+")
    hs = int(f.readline())
    if(gameVariables.gameScores > hs):
       hs = gameVariables.gameScores
       f.seek(0)
       f.truncate()
       f.write(str(hs))
    f.close()
    
    X = 1200
    Y = 700
    display_surface = pygame.display.set_mode((X, Y ))
    image = pygame.image.load(r'images/devil.png')
    display_surface.blit(image, (8, 50))
    

    image2 = pygame.image.load(r'images/devil2.png')
    display_surface.blit(image2, (30, 35))
    image3 = pygame.image.load(r'images/devil2.png')
    display_surface.blit(image3, (970, 35))
    draw_text(screen, "Your Score: " + str(gameVariables.gameScores), 200, 20)
    draw_text(screen, "Highscore: " + str(hs), 250, 20)
    draw_text(screen, "Press enter to replay", 365, 20)
    draw_text(screen, "Press esc to exit", 400, 20)
    
    #Updates the entire screen for the last time
    pygame.display.update()

    #Gets the keyboard events to se if the user wants to restart the game
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == gameVariables.K_KP_ENTER:
                    return 0
                elif e.key == gameVariables.K_ESCAPE:
                    return 1
                
