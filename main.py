import pygame

substances = {}


def main():
    pygame.init()
    screen = pygame.display.set_mode((1022, 600))
    pygame.display.set_caption('Таблица растворимости')
    running = True
    table = pygame.image.load('Pictures/table.jpg')
    screen.blit(table, (0, 0))
    picture = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not picture:
                    x, y = event.pos
                    column = (x - 95) // 40 + 1
                    string = (y - 37) // 40 + 1
                    print(column, string)
                    #  screen.blit(substances[(column, string)], (250, 150))
                    picture = True
                else:
                    screen.blit(table, (0, 0))
                    picture = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
