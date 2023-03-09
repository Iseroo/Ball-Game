from graph import *
from block import *
import pygame as pg
from pygame.locals import *
from random import randint
from ball import *

from map import Map




class MainGame:
    def __init__(self):
        # init pygame
        pg.init()
        # set window size
        self.width = 800
        self.height = 800
        # set window
        self.screen = pg.display.set_mode((self.width, self.height))
        # set title
        pg.display.set_caption('Map')
        # set clock
        self.clock = pg.time.Clock()
        # set fps
        self.fps = 60
        # set map
        self.map = None
        self.setup_map()

        # set ball
        x,y = self.map.get_coords_by_id(11)
        self.ball = Ball(x,y, 40, (0, 0, 207))

        self.path = self.map.find_path()

    
        self.buttonPos = None
        self.startBall = False

        self.editMode = False

    
    def run(self):
        # set running
        running = True
        # set map
        waiter = 0
        next_move = self.find_next_move()


        while running:
            self.screen.fill((255, 255, 255))
            mouse_pos = pg.mouse.get_pos()
            self.start_button()
            # set fps
            self.clock.tick(self.fps)
            # set events

            
            for event in pg.event.get():
                
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                       
                        # if not self.startBall:
                        id = self.map.get_block_clicked(*mouse_pos)
                        
                        if id != None and not self.startBall and not self.editMode:
                            self.ball.move(*self.map.get_coords_by_id(id.id))
                            self.map.start = id.id
                            self.path = self.map.find_path()
                            print('path', self.path)
                        
                        if self.editMode and id != None:
                            id.block.rotate()
                            self.map.setup_directions()
                        
                        # click start button
                        if self.buttonPos[0] <= mouse_pos[0] <= self.buttonPos[0] + 100 and self.buttonPos[1] <= mouse_pos[1] <= self.buttonPos[1] +50:
                            self.editMode = False
                            self.startBall = not self.startBall
                            if self.startBall:
                                self.path = self.map.find_path()
                               
                                next_move = self.find_next_move()
                                waiter = 0
                    if event.button == 3:
                        if not self.startBall:
                            id = self.map.get_block_clicked(*mouse_pos)
                            if id != None:
                                self.map.end = id.id
                                self.path = self.map.find_path()
                            
                if event.type == KEYDOWN:
                    if event.key == K_e:
                        self.editMode = not self.editMode


                
            # set background
            
            # draw map
            self.draw_map()
            

            if not len(self.path):
                self.write_text_center('No Path From Here', (255, 0, 0), 50)

            # print('a')
            
            # draw ball
            self.draw_cross_end()
            self.draw_ball()

            # print(self.startBall, len(self.path), waiter)
            if waiter == 30 and self.startBall and len(self.path):
                
                # print('next', next_move)
                try:
                     id = next(next_move)
                     
                     self.ball.move(*self.map.get_coords_by_id(id))
                except StopIteration:
                    # print('stop iteration')
                    pass
                
                waiter = 0

            waiter += 1



            # update display
            pg.display.update()
        pg.quit()

    def setup_map(self):
        self.map = Map('map.json', 11, 37)
        self.map.readmap()
    
    def draw_map(self):
        for x in self.map.map:
           for x2 in x:
                x2.draw(self.screen)
        
    def draw_ball(self):
        self.ball.draw(self.screen)
        # self.ball.move()

    def find_next_move(self):
        for x in self.path:
            yield x

    def write_text_center(self, text, color=(255,0,0), size=24):
        font = pg.font.SysFont('comicsans', size)
        text = font.render(text, 1, color)
        self.screen.blit(text, (self.width/2 - text.get_width()/2, self.height/2 - text.get_height()/2))

    def start_button(self):
        # make a start button on the top of the screen

        # make a rect
        rect = pg.Rect(0, 0, 100, 50)
        # make a surface
        surface = pg.Surface((100, 50))
        # set color
        surface.fill((255, 255, 255))
        # draw rect
        pg.draw.rect(surface, (0, 0, 0), rect, 2)
        # draw text
        font = pg.font.SysFont('comicsans', 24)
        text = font.render('Start' if not self.startBall else 'Stop', 1, (0, 0, 0))
        surface.blit(text, (50 - text.get_width()/2, 25 - text.get_height()/2))
        self.buttonPos = (self.width/2 - 50, 0)
        # blit surface
        self.screen.blit(surface, self.buttonPos)
        # return rect
        # return rect

    def draw_cross_end(self):
        # draw a red cross on the end of the path
        x, y = self.map.get_coords_by_id(self.map.end)

        line1_start, line1_end = (x - 30, y -30), (x + 30, y + 30)
        line2_start, line2_end = (x - 30, y + 30), (x + 30, y - 30)

        pg.draw.line(self.screen, (255, 0, 0), line1_start, line1_end, 5)
        pg.draw.line(self.screen, (255, 0, 0), line2_start, line2_end, 5)







if __name__ == '__main__':
    game = MainGame()
    game.run()
