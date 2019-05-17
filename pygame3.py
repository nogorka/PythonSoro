import pygame
import GIFImage
import time
from TextToSpeech import say
from logic import logics

display_width = 800
display_height = 600

fps = 60

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Application")

progress = True

clock = pygame.time.Clock()

image = GIFImage.GIFImage("teacher_emoji/улыбка.gif")


def change_image(new_image):
    """
    :param new_image - filename of new image:
    """
    global image
    image = GIFImage.GIFImage(new_image)


def play_sound(filename):
    """
    :param sound - sound filename:
    """
    sound = pygame.mixer.Sound(filename)
    sound.play()


image.running = True
display.fill((255, 255, 255))

c_emoji="улыбка"
while progress:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            progress = False

            pygame.quit()
            quit()


#        play_sound(sound_name)  #from pygame
#        say(answer)#from tts
            
        emoji, sound_name, answer= logics()
        if c_emoji!= emoji:
            c_emoji=emoji
            change_image("teacher_emoji/"+c_emoji+".gif")

        time.sleep(5)
    image.render(display, (50, 50))

    pygame.display.update()

    clock.tick(fps)
