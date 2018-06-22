import pygame
import random
from pygame.locals import *

class Snake():
    def __init__(self):
        self.body = [[50, 10], [70, 10], [90, 10]]
        self.head = self.body[-1]
        self.dir = "Right"
        self.score = 0

    def change_dir(self, new_dir):
        if new_dir == "Right" and self.dir != "Left":
            self.dir = "Right"
        elif new_dir == "Left" and self.dir != "Right":
            self.dir = "Left"
        elif new_dir == "Up" and self.dir != "Down":
            self.dir = "Up"
        elif new_dir == "Down" and self.dir != "Up":
            self.dir = "Down"

    def move(self, food):
        if self.dir == "Right":
            self.head[0] += 20
        elif self.dir == "Left":
            self.head[0] -= 20
        elif self.dir == "Up":
            self.head[1] -= 20
        elif self.dir == "Down":
            self.head[1] += 20
        self.body.append(list(self.head))
        if food == self.head:
            self.score += 1
            return True
        else:
            self.body.pop(0)
        return False

    def Body(self):
        return self.body

class Food:
    def __init__(self):
        self.pos = [random.randint(0, 39) * 20 + 10, random.randint(0, 29) * 20 + 10]
        self.food_exist = True
    def draw(self):
        pygame.draw.circle(window, blue , (self.pos[0], self.pos[1]), 10)
    def food_pos(self):
        return self.pos
    def hit_snake(self, snake):
        if self.pos == snake:
            self.pos = [random.randint(0, 39) * 20 + 10, random.randint(0, 29) * 20 + 10]
        return self.pos

def Through_Wall(snake_head):
    if 0 > snake_head[0]:
        snake_head[0] = 810
    elif 800 < snake_head[0]:
        snake_head[0] = -10
    elif 0 > snake_head[1]:
        snake_head[1] = 610
    elif 600 < snake_head[1]:
        snake_head[1] = -10

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
snake = Snake()
food = Food()

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Arial", 20)
    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_dir("Right")
                elif event.key == pygame.K_LEFT:
                    snake.change_dir("Left")
                elif event.key == pygame.K_UP:
                    snake.change_dir("Up")
                elif event.key == pygame.K_DOWN:
                    snake.change_dir("Down")

        snake.move(food.food_pos())
        window.fill(black)
        the_text = my_font.render("This's just a demo, so basically you can't lose. Score: " + str(snake.score), True, red)
        window.blit(the_text, (10, 10))
        for ball in snake.Body():
            pygame.draw.circle(window, white, (ball[0], ball[1]), 10)
        pygame.draw.circle(window, green, (snake.body[-1][0], snake.body[-1][1]), 10)
        food.draw()
        food.hit_snake(snake.head)
        Through_Wall(snake.head)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()

main()
