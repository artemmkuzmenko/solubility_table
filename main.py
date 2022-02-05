import sys

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1022, 600))
    pygame.display.set_caption('Таблица растворимости')
    running = True
    table = pygame.image.load('Pictures/table.jpg')
    screen.blit(table, (0, 0))
    while running:
        for event in pygame.event.get():
            print(event)
            if event == pygame.QUIT:
                running = False
            elif event == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                column = (x - 95) // 40 + 1
                string = (y - 37) // 40 + 1
                print(column, string)
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
