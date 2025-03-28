import pygame
import color_palette
import random
from pygame.locals import *

#Pygame initialization
pygame.init()

#Screen's width and height
w, h = 600, 600

#Creating window and filling it white
screen = pygame.display.set_mode((w, h))
screen.fill(color_palette.colorWHITE)

#Font
font = pygame.font.SysFont("comicsansms", 20)

#Cell size
cell = 30

#FPS
clock = pygame.time.Clock()
FPS = 5

#Variables of score, level, snake's speed
food_cnt = 0
level_cnt = 1
snake_speed = 1

#Function for drawing a gray grid
def draw_grid():
    for i in range(h // cell):
        for j in range(w // cell):
            pygame.draw.rect(screen, color_palette.colorGRAY, (i * cell, j * cell, cell, cell), 1)

#Function for drawing a chess grid
def draw_grid_chess():
    colors = [color_palette.colorGRAY, color_palette.colorWHITE]

    for i in range(h // cell):
        for j in range(w // cell):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * cell, j * cell, cell, cell))

#Class for points 30*30
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    

#Class for randomly generated food
class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    #Generates food 
    def random_pos(self):
        while True:
            #Generates random food coordinates not on a wall
            self.pos.x = random.randint(1, w // cell - 2)
            self.pos.y = random.randint(1, h // cell - 2)
            #Sets food's position only if it does not touch snake's body   
            for segment in snake.body:
                if segment.x == self.pos.x and segment.y == self.pos.y:
                    break
            else:
                break
    
    #Draws green food at generated position
    def draw(self):
        pygame.draw.rect(screen, color_palette.colorGREEN, (self.pos.x * cell, self.pos.y * cell, cell, cell))


#Class for a snake
class Snake:
    #Initial snake's size of three cells
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
    
    #Each cell repeats previous cell's position to move
    def moving(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        #If the snake goes out of the border it appears from the other side
        if self.body[0].x + self.dx < w // cell and self.body[0].x + self.dx >= 0:
            self.body[0].x += self.dx
        elif self.body[0].x + self.dx < 0:
            self.body[0].x = w // cell
        else:
            self.body[0].x = 0

        if self.body[0].y + self.dy < h // cell and self.body[0].y + self.dy >= 0:
            self.body[0].y += self.dy
        elif self.body[0].y + self.dy < 0:
            self.body[0].y = h // cell
        else:
            self.body[0].y = 0

    
    def draw(self):
        head = self.body[0]
        #Draws the head red
        pygame.draw.rect(screen, color_palette.colorRED, (head.x * cell, head.y * cell, cell, cell))
        #Draws body's segments yellow
        for segment in self.body[1:]:
            pygame.draw.rect(screen, color_palette.colorYELLOW, (segment.x * cell, segment.y * cell, cell, cell))

    def food_collision(self, food):
        global food_cnt, level_cnt, snake_speed, FPS
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            #Grows with each eaten piece
            self.body.append(Point(head.x, head.y))
            #Generates new food
            food.random_pos()
            #Food counter
            food_cnt += 1
            if food_cnt % 3 == 0:
                #Level increases each three eaten pieces
                level_cnt += 1
                #snake_speed += 1
                #Speed increases as well
                FPS += 0.5

#Objects of our classes
snake = Snake()
food = Food()
snake.draw()

running = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        #Controlling the snake by the arrow keys
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                snake.dx = snake_speed
                snake.dy = 0
            elif event.key == K_LEFT:
                snake.dx = -snake_speed
                snake.dy = 0
            elif event.key == K_UP:
                snake.dx = 0
                snake.dy = -snake_speed
            elif event.key == K_DOWN:
                snake.dx = 0
                snake.dy = snake_speed

    #We move the snake 
    snake.moving()
    #We check the food collision
    snake.food_collision(food)
    #We fill our screen again
    draw_grid_chess()
    snake.draw()
    #Level and score counters
    level = font.render("LEVEL " + str(level_cnt), True, color_palette.colorBLACK)
    score = font.render("SCORE: " + str(food_cnt), True, color_palette.colorBLACK)
    food.draw()
    screen.blit(level, (5, 5))
    screen.blit(score, (5, 35))
    pygame.display.flip()
    clock.tick(FPS)