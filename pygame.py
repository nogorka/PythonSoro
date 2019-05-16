import pygame
import GIFImage

display_width = 800
display_height = 600

fps = 60

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Application")

progress = True

clock = pygame.time.Clock()

image = GIFImage.GIFImage("Уточка1.2.gif")


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


while progress:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            progress = False

            pygame.quit()
            quit()

        #
        # Здесь нужно сделать условие и в нем изменить картинку
        # Как написано ниже
        #

        if event.type == pygame.KEYDOWN:
            change_image("Учитель(удивление)1.2.gif")

        #
        # Звук можно добавить так
        #
        # play_sound("sound.mp3")

    image.render(display, (50, 50))

    pygame.display.update()

    clock.tick(fps)
