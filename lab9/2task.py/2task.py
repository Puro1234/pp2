import pygame
import color_palette
import random
import time
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

#Game Over picture
gameover_img = pygame.image.load("gameover.jpg")
gameover_img = pygame.transform.scale(gameover_img, (450, 361))

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
        #Initial food's position and weight
        self.pos = Point(9, 9)
        self.weight = 2
        #Time stamp to track time
        self.timestamp = time.time()

    #Generates food 
    def random_pos(self):
        while True:
            #Generates random food coordinates
            self.pos.x = random.randint(0, w // cell - 1)
            self.pos.y = random.randint(0, h // cell - 1)
            #Generates food's weight
            self.weight = random.randint(1, 3)
            #Sets food's position only if it does not touch snake's body and walls  
            for segment in snake.body:
                if segment.x == self.pos.x and segment.y == self.pos.y:
                    break
            for wall in walls.walls:
                if wall.x == self.pos.x and wall.y == self.pos.y:
                    break
            else:
                break
        #Reset the timestamp whenever a new food is created
        food.timestamp = time.time()
            
    
    #Draws green food at generated position
    def draw(self):
        #Food's color is based on its weight
        colors = [color_palette.colorLIGHTGREEN, color_palette.colorGREEN, color_palette.colorDARKGREEN]
        pygame.draw.rect(screen, colors[self.weight-1], (self.pos.x * cell, self.pos.y * cell, cell, cell))


#Class for walls
class Wall:
    def __init__(self):
        #Walls' coordinates
        self.walls = {
            Point(6, 0),
            Point(7, 0),
            Point(8, 0),
            Point(9, 0),

            Point(2, 5),
            Point(3, 5),
            Point(2, 6),
            Point(3, 6),

            Point(13, 2),
            Point(13, 3),
            Point(13, 4),
            Point(13, 5),

            Point(15, 9),
            Point(16, 9),

            Point(0, 13),
            Point(1, 13),
            Point(2, 13),

            Point(9, 13),
            Point(9, 14),
            Point(9, 15),
            Point(10, 15),
            Point(11, 15),

            Point(19, 13),

            Point(6, 19),
            Point(7, 19),
            Point(8, 19),
            Point(9, 19),
        }

    #Painting the walls black
    def draw(self):
        for wall in self.walls:
            pygame.draw.rect(screen, color_palette.colorBLACK, (wall.x * cell, wall.y * cell, cell-0.5, cell-0.5))

#Class for a snake
class Snake:
    #Initial snake's size of three cells
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.collision = False
    
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
            for i in range (0, food.weight):
                self.body.append(Point(head.x, head.y))
            #Food counter
            food_cnt += food.weight
            if food_cnt % 5 == 0:
                #Level increases each three eaten pieces
                level_cnt += 1
                #snake_speed += 1
                #Speed increases as well
                FPS += 0.5
            #Generates new food
            food.random_pos()


    def walls_collision(self, walls):
        global running
        head = self.body[0]
        #Game is over if snake's head and walls collide
        for wall in walls.walls:
            if head.x == wall.x and head.y == wall.y:
                time.sleep(1.5)
                
                screen.fill(color_palette.colorWHITE)
                screen.blit(gameover_img, (75, 120))

                pygame.display.flip()

                time.sleep(2)

                self.collision = True

#Objects of our classes
snake = Snake()
food = Food()
walls = Wall()
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
                
    #Generates new food every 7 seconds
    if time.time() - food.timestamp > 7:
            food.random_pos()
            

    #We move the snake 
    snake.moving()

    #We check the food and walls collision
    snake.food_collision(food)
    snake.walls_collision(walls)

    #Game ends if the snake collides with a wall
    if snake.collision:
        pygame.quit()

    #We fill our screen again
    draw_grid_chess()
    walls.draw()
    snake.draw()

    #Level and score counters
    level = font.render("LEVEL " + str(level_cnt), True, color_palette.colorBLACK)
    score = font.render("SCORE: " + str(food_cnt), True, color_palette.colorBLACK)

    #Printing the food, current level and score
    food.draw()
    screen.blit(level, (5, 5))
    screen.blit(score, (5, 35))
    pygame.display.flip()
    clock.tick(FPS)