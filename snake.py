import pygame
import random

class SnakeGame:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.snake_block = 10
        self.snake_speed = 15

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont(None, 50)
        self.score_font = pygame.font.SysFont(None, 35)

    def run(self):
        game_over = False
        game_close = False

        x1 = self.width / 2
        y1 = self.height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, self.width - self.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.height - self.snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                self.display.fill(self.black)
                self.message("You Lost! Press Q-Quit or C-Play Again", self.red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0

            if x1 >= self.width or x1 < 0 or y1 >= self.height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            self.display.fill(self.blue)
            pygame.draw.rect(self.display, self.green, [foodx, foody, self.snake_block, self.snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            self.our_snake(self.snake_block, snake_List)
            self.your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, self.width - self.snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, self.height - self.snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            self.clock.tick(self.snake_speed)

        pygame.quit()
        quit()

    def your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.white)
        self.display.blit(value, [0, 0])

    def our_snake(self, block, snake_List):
        for x in snake_List:
            pygame.draw.rect(self.display, self.white, [x[0], x[1], block, block])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.display.blit(mesg, [self.width / 6, self.height / 3])
