import pygame
import sys
import os
import random


#TO DO: Add Moving Animation
#Lift start orb
#Connect to monkeyrunner somehow (Might be really hard)



class Board:

    def __init__(self, dimension_of_board, tile_size, margin_size, board_pattern):
        self.board_pattern = board_pattern
        self.moves = []

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

        self.tilespos = {(x, y): (x * (tile_size + margin_size) + margin_size,
                                  y * (tile_size + margin_size) + margin_size)
                        for y in range(self.rows) for x in range(self.columns)}

        # purely for monkeyRunner, if i can make that work
        self.orb_pattern = []
        for i in range(self.size):
            self.orb_pattern.append(self.orbkey.get(self.board_pattern[i]))

    # "Blank" - should be the orb you're holding
    def get_start_orb(self):
        # Currently always sets the start orb as the bottom right tile
        return self.tiles[-1]

    # Constantly update the current orb that is being held
    def set_start_orb(self, pos):
        self.tiles[-1] = pos

    opentile = property(get_start_orb, set_start_orb)

    def swap(self, tile):
        index = self.tiles.index(tile)
        self.tiles[index], self.opentile = self.opentile, self.tiles[index]

    def in_grid(self, tile):
        return tile[1] >= 0 and tile[1] < self.rows and tile[0] >= 0 and tile[0] <self.columns

    def adjacent(self):
        x,y = self.opentile
        return (x-1,y),(x+1,y),(x,y-1),(x,y+1)

    def update(self, dt):
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        if mouse[0]:
            ##
            tile = mpos[0] // (self.tile_size+self.margin_size), mpos[1] // (self.tile_size+self.margin_size)

            if self.in_grid(tile):
                if tile in self.adjacent():
                    self.swap(tile)
                    self.moves.append(tile)

    def draw(self, screen):

        for i in range(self.size):
            x, y = self.tilespos[self.tiles[i]]
            screen.blit(self.orb_pattern[i], (x -self.margin_size, y - self.margin_size))

    def print_moves(self):
        print( self.moves)

def generate_random_board():
    orbs = ['r', 'g', 'b', 'l', 'd', 'h']
    board = [random.choice(orbs) for i in range(30)]
    return board


x = ['g', 'r', 'l', 'g', 'r', 'h', 'g', 'r', 'r', 'l', 'l', 'r', 'd', 'g', 'g', 'h', 'r', 'b', 'b', 'd', 'r', 'b', 'r',
     'g', 'r', 'd', 'r', 'b', 'g', 'l']


def main():
    global x
    bg = pygame.image.load("bg.png")

    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Pazudora')
    screen = pygame.display.set_mode((720, 600))
    fpsclock = pygame.time.Clock()
    ##tile size and margin size should add up to 120
    program = Board((6, 5), 118, 2, generate_random_board())

    while True:
        dt = fpsclock.tick() / 1000
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        program.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: program.print_moves();pygame.quit(); sys.exit()
        program.update(dt)

main()
