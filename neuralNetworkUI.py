import pygame
import heapq
from PIL import Image
from keras.models import load_model
import numpy as np
from pandas import datetime


model = load_model('mnist.h5')


def predict_digit(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0
    res = model.predict([img])[0]
    t = heapq.nlargest(3, res)
    t2 = res.argsort()[-3:][::-1]
    # 3 самые большие вероятности
    print(t)
    # числа к которым они относятся
    print(t2)


def getImage(path):
    im = Image.open(path)
    predict_digit(im)


def savePicture(screen):
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    path = './{}.png'.format(now_str)
    pygame.image.save(screen, path)
    getImage(path)


screen = pygame.display.set_mode((200, 200))
line_start = None

while True:
    mouse_pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            break
        if e.type == pygame.MOUSEBUTTONUP:
            line_start = None if line_start else mouse_pos
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            savePicture(screen)
    else:
        if line_start:
            pygame.draw.line(screen, pygame.color.Color('White'), line_start, mouse_pos, 10)
            line_start = mouse_pos
        pygame.display.flip()
        continue
    break
