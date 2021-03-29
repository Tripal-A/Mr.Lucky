import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Mr.Lucky')

#in pygame all colors are RGB (Red, green, blue,) and can be ranged from 0-255. WIN.fill((255,255,255)) would make the screen white
#OR you can just create a variable for white like below and use WIN.fill(WHITE) in line 22
WHITE = (255,255,255)

FPS=60


#loads the image from OS, arguments are folder name, image name
CHARACTER = pygame.image.load(os.path.join('Assets','images.png'))
CHARACTER = pygame.transform.scale(CHARACTER,(255,255)) #resizing the image, can also put a variable like CHARACTER_WIDTH, CHARACTER_HEIGHT = 255,255 AND INPUT ARGUMENTS

BACKGROUND = pygame.image.load(os.path.join('Assets','background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND,(900,500))

#creating a function that will hold all your drawings
#drawing an image ONTO the screen is done with win.blit() an image that is on top of a surface is a blit
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(CHARACTER,(0,250))
    pygame.display.update()  # ALL DISPLAY CHANGES MUST BE UPDATED AFTER THE COMMAND



#creating a loop to keep game running and not close out immediately after opened, this is the main loop for the game
def main():
    clock = pygame.time.Clock() #THIS WILL CONTROL THE SPEED OF THE WHILE LOOP BUT MUST BE PUT INTO THE LOOP SEE LINE 26

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False#if the game is quit, run is set to False which will close

        draw_window()




    pygame.quit()

#this is making sure the game is ONLY ran if we run it from this file direction. If this was not here the game
#could get automatically run if imported
if __name__ == "__main__":
    main()