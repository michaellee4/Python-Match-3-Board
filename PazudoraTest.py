import pygame
import sys
import os


class Board:

    # def randomize(self):
    #     colors = ['r','g','b','y','d']
    #     self.board = [random.choice(colors) for i in range(self.size)]

    def __init__(self, dimension_of_board, tile_size, margin_size):
        self.tile_size = tile_size
        self.margin_size = margin_size

        self.columns = dimension_of_board[0]
        self.rows = dimension_of_board[1]
        self.size = self.rows*self.columns

        self.tiles = [(x, y) for y in range(self.rows) for x in range(self.columns)]
        self.tilespos = {(x, y):(x*(tile_size+margin_size)+margin_size, y*(tile_size+margin_size)+margin_size)
                         for y in range(self.rows) for x in range(self.columns)}

        #self.font = pygame.font.Font(None,120)

        # if board_layout:
        #     self.board = board_layout
        # else:
        #     self.randomize

    def set_layout(self):
        pass

    def print_board(self):
        for i in range(self.rows):
            for j in range (self.columns):
                print(self.board[i*self.columns+j], end=' ')
            print("\n")

    def swap(self):
        pass

    def update(self,dt):
        pass

    def draw(self,screen):
        for i in range(self.size):
            x, y = self.tilespos[self.tiles[i]]
            pygame.draw.rect(screen, (0,255,0), (x,y, self.tile_size, self.tile_size))
            pygame.draw.ci
            #text = self.font.render(str(i+1),2,(0,0,0))
            #screen.blit(text,(x, y))


def main():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Pazudora')
    screen = pygame.display.set_mode((800,600))
    fpsclock = pygame.time.Clock()
    program = Board((6, 5),70, 5)

    while True:
        dt = fpsclock.tick()/1000
        screen.fill((0, 0, 0))
        program.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        program.update(dt)
main()