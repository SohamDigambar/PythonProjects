'''
Created on Jul 13, 2021

@author: sohamdigambar
'''

import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.SysFont('arial', 25)

Point = namedtuple('Point', 'x, y')     #this is basically a lightweight class that makes it easier to read coordinates

BLOCK_SIZE = 20     #20 pixels represents 1 snake "block"
SPEED = 15

#RGB colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGame:
    
    def __init__(self, width = 640, height = 480):
        self.width = width
        self.height = height
        
        #initialize display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        
        #initialize game state
        self.direction = Direction.RIGHT
        self.head = Point(self.width / 2, self.height / 2) #starts in the center
        self.snake = [self.head, 
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]   #creates the snake based on the head position
        self.score = 0
        self.food = None
        self._place_food()
        
        
        
    def _place_food(self):
        x = random.randint(0,  (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food == self.snake:
            self.place_food()   #uses recursion to ensure food is NOT spawned in the snake 
        
        
        
    def play_step(self):
        #collects user input (direction)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                    
        #moves snake
        self._move(self.direction) #updates the head
        self.snake.insert(0, self.head)
        
        #checks if game is over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        
        #places new food or move the snake
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        
        #updates ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        
        #returns game over and score 
        game_over = False
        return game_over, self.score



    def _update_ui(self):
        self.display.fill(BLACK)
        
        for point in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(point.x, point.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(point.x + 4, point.y + 4, 12, 12))   #spaces between each snake block
            
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()    #allows us to see the changes when we run the update method



    def _is_collision(self):
        #if snake hits boundary
        if self.head.x > self.width - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.height - BLOCK_SIZE or self.head.y < 0:
            return True
        
        #if snake hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
            
        self.head = Point(x, y)
        

if __name__ == '__main__':
    game = SnakeGame()
    
    #game loop
    while True:
        game_over, score = game.play_step()
        
        #break if game over
        if game_over == True:
            break
        
    print('Final Score: ', score)
    
    pygame.quit()