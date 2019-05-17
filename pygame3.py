import pygame
import GIFImage
import time
from TextToSpeech import *
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

c_emoji="улыбка" # current emoji
while progress:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            progress = False

            pygame.quit()
            quit()
            
            
            
        emoji, sound_name, answer = logics()
#        название эмоции, название аудио файла, ответ
        
        print("data resived")
        """
        воспроизведение звука с помощью pygame:
        play_sound(sound_name) 
        
        с помощью tts из логики(TextToSpeech):
        say(answer) произносит фразу
        gtalk(answer) сохраняет строку с ответом в файл
        talk(sound_name) откравает файл в аудио проигрывателе

        
        по идее надо каждую секунду проверять изменилась ли эмоция или нет
        если да то мы ее открываем и воспроизводим аудио
        иначе делаем ничего, идем дальше
        
        не знаю можно так или нет
        но надо сначала открыть изображение потом аудио
        было бы хорошо если они работали вместе 
        переход на новый круг цикла должен быть когда закончится аудио
        или после 10 секунд от начала(это зависит от того что ты сможешь сделать)
        
            в файле logics есть 3 current_question:
                1. command() - это для распознавания голоса
                2. для быстрой проверки сервера
                3. для быстрой проверки вопросов-ответов
            их можно использовать для проверки работоспособности
            по умолчанию там будет и должен стоять 1
            
        
        """
#        if c_emoji!= emoji:
#            c_emoji=emoji
#            change_image("teacher_emoji/"+c_emoji+".gif")
#            say(answer)
#        time.sleep(10)
#        change_image("teacher_emoji/"+c_emoji+".gif")
    image.render(display, (50, 50))

    pygame.display.update()
#    change_image("teacher_emoji/"+c_emoji+".gif")
#    image.render(display, (50, 50))
#    pygame.display.update()

    clock.tick(fps)
