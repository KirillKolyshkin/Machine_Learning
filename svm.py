import pygame
import sklearn.svm as svm
import numpy as np

running = True
pygame.init()
screen = pygame.display.set_mode((800, 500))
screen.fill((255, 255, 255))

points = []
clast = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 10)
                points.append(event.pos)
                clast.append(0)
            if event.button == 3:
                pygame.draw.circle(screen, (0, 255, 0), event.pos, 10)
                points.append(event.pos)
                clast.append(1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            clf = svm.SVC(kernel='linear', C=1.0)
            clf.fit(points, clast)

            weights = clf.coef_[0]
            w = weights[0]
            b = weights[1]

            a = -w / b
            xx = np.linspace(0, 800, 2)

            yy = a * xx - (clf.intercept_[0]) / b

            pygame.draw.line(screen, (0, 0, 0),
                             (xx[0], yy[0]),
                             (xx[len(xx) - 1], yy[len(yy) - 1]))
    pygame.display.update()

pygame.quit()
quit()
