import pygame
from multiprocessing import Process, Queue
import xlrd
import mmap

from SpeechRecognition import command
from Answer import cheak
from GIFsearch import search
from TextToSpeech import gtalk

from GIFImage import GIFImage


#
# Functions performed in threads
#
def listen(q):
    q.put(command())


def correct(q, current_question):
    rb = xlrd.open_workbook('схема.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    questions = [vals[rownum][0] for rownum in range(14)]
    answers = [vals[rownum][1] for rownum in range(14)]
    q.put(cheak(current_question, questions, answers))


def emoji(q, answer):
    q.put(search(answer))


def talk(q, answer):
    q.put(gtalk(answer))


#
# Default variables for pygame
#
pygame.init()
WIDTH = 800
HEIGHT = 600
APPLICATION_NAME = "Application"
FPS = 60

BACKGROUND = (255, 255, 255)


# Character params
DEFAULT_EMOJI = "улыбка"


if __name__ == '__main__':

    #
    # Multiprocessing threads
    #
    q = Queue()
    threads = [lambda queue, data: Process(target=listen, args=(queue,)), lambda queue, c_q: Process(target=correct, args=(queue, c_q)),
               lambda queue, answer: Process(target=emoji, args=(queue, answer)), lambda queue, answer: Process(target=talk, args=(queue, answer,))]
    # For choosing current thread (listen, talk and etc.)
    stage = 1
    stages_n = len(threads)

    #
    # Initializing pygame application
    #
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    display.fill(BACKGROUND)
    pygame.display.set_caption(APPLICATION_NAME)
    progress = True
    clock = pygame.time.Clock()

    # Display elements
    IMAGE_FILE = "teacher_emoji/%s.gif"
    image = GIFImage(IMAGE_FILE % DEFAULT_EMOJI)
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Слушаю', True, (255, 0, 0), (0, 255, 0))

    # Starting the first thread
    thread = threads[0](q, None)
    thread.start()

    # Character params
    new_character_params = [None]

    #
    # Main application loop
    #
    while progress:

        # Answer, Emoji, Sound

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE)):
                thread.terminate()
                progress = False
                pygame.quit()
                quit()

        #
        # Performing threads
        #
        if not q.empty():
            data = q.get()
            new_character_params.append(data)
            thread.terminate()
            if stage == 0:
                textSurfaceObj = fontObj.render('Слушаю', True, (255, 0, 0), (0, 255, 0))
                display.fill(BACKGROUND)
                image = GIFImage(IMAGE_FILE % DEFAULT_EMOJI)
                thread = threads[0](q, data)
            if stage == 1:
                textSurfaceObj = fontObj.render('Надеюсь понял', True, (255, 0, 0), (0, 255, 0))
                display.fill(BACKGROUND)
                thread = threads[1](q, data)
            if stage == 2:
                thread = threads[2](q, new_character_params[2])
            if stage == 3:
                thread = threads[3](q, " ".join(new_character_params[2].split(" ")[:-1:]))
                display.fill(BACKGROUND)
                textSurfaceObj = fontObj.render('Отвечаю', True, (255, 0, 0), (0, 255, 0))
            if stage != stages_n:
                thread.start()
            stage = stage + 1

        if stage == stages_n:
            new_character_params.append(q.get())
            stage = -1
            pygame.mixer.music.load(new_character_params[4])
            pygame.mixer.music.play()
            current_emoji = new_character_params[3]
            display.fill(BACKGROUND)
            image = GIFImage(IMAGE_FILE % current_emoji)
            new_character_params = []

        if stage == -1 and pygame.mixer.music.get_pos() == -1:
            q.put(None)
            pygame.mixer.music.stop()
            stage = 0

        # Updating elements
        image.render(display, (0, 0))
        display.blit(textSurfaceObj, (350, 50))

        pygame.display.update()
        clock.tick(FPS)
