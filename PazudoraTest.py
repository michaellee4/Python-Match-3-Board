import pygame
import sys
import os
import random


class Board:

    def __init__(self, dimension_of_board, tile_size, margin_size, board_pattern):
        self.board_pattern = board_pattern

        self.tile_size = tile_size
        self.margin_size = margin_size

        self.columns = dimension_of_board[0]
        self.rows = dimension_of_board[1]
        self.size = self.rows * self.columns

        self.orbkey = {'g': pygame.image.load('Green.png'),
                       'r': pygame.image.load('Red.png'),
                       'b': pygame.image.load('Blue.png'),
                       'l': pygame.image.load('Light.png'),
                       'd': pygame.image.load('Dark.png'),
                       'h': pygame.image.load('Heart.png'),
                       'x': pygame.image.load('Poison.png'),
                       '*': pygame.image.load('Jammer.png')}

        self.tiles = [(x, y) for y in range(self.rows) for x in range(self.columns)]
        self.tilespos = {
        (x, y): (x * (tile_size + margin_size) + margin_size, y * (tile_size + margin_size) + margin_size)
        for y in range(self.rows) for x in range(self.columns)}

        self.orb_pattern = []
        for i in range(self.size):
            self.orb_pattern.append(self.orbkey.get(self.board_pattern[i]))


    def set_layout(self):
        pass

    def print_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i * self.columns + j], end=' ')
            print("\n")

    # "Blank" - should be the orb you're holding
    def get_start_orb(self):
        return self.tiles[-1]

    # Constantly update the current orb that is being held
    def set_start_orb(self,pos):
        self.tiles[-1] = pos
        # opentile = property(get_start_orb,set_start_orb)

    def swap(self):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):

        for i in range(self.size):
            x, y = self.tilespos[self.tiles[i]]
            screen.blit(self.orb_pattern[i], (x - 8, y - 8))



def generate_random_board():
    orbs = ['r', 'g', 'b', 'l', 'd', 'h']
    board = [random.choice(orbs) for i in range(30)]
    return board


x = generate_random_board()


def main():
    bg = pygame.image.load("bg.png")

    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Pazudora')
    screen = pygame.display.set_mode((720, 600))
    fpsclock = pygame.time.Clock()
    program = Board((6, 5), 104, 16, x)

    while True:
        dt = fpsclock.tick() / 1000
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        program.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        program.update(dt)


main()
