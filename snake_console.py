import random
import curses
import time

gameOver = False

score = 0

class Block:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol


class Snake:
    def __init__(self, x, y, symbol):
        self.parts = []
        self.symbol = symbol
        self.size = 1
        self.parts.append(Block(x, y, self.symbol))
        self.direction = curses.KEY_RIGHT

    def eat_apple(self):
        self.size += 1
        tail = self.parts[-1]
        if self.direction == curses.KEY_RIGHT:
            new_block = Block(tail.x - 1, tail.y, self.symbol)
        elif self.direction == curses.KEY_LEFT:
            new_block = Block(tail.x + 1, tail.y, self.symbol)
        elif self.direction == curses.KEY_UP:
            new_block = Block(tail.x, tail.y + 1, self.symbol)
        elif self.direction == curses.KEY_DOWN:
            new_block = Block(tail.x, tail.y - 1, self.symbol)
        self.parts.append(new_block)

    def move(self):
        head = self.parts[0]
        if self.direction == curses.KEY_RIGHT:
            new_head = Block(head.x + 1, head.y, self.symbol)
        elif self.direction == curses.KEY_LEFT:
            new_head = Block(head.x - 1, head.y, self.symbol)
        elif self.direction == curses.KEY_UP:
            new_head = Block(head.x, head.y - 1, self.symbol)
        elif self.direction == curses.KEY_DOWN:
            new_head = Block(head.x, head.y + 1, self.symbol)

        self.parts.insert(0, new_head)  # Add the new head
        if len(self.parts) > self.size:  # Remove the last segment if not growing
            self.parts.pop()


class Board:
    def __init__(self, width, height, snake):
        self.width = width
        self.height = height
        self.apple_coords = []
        self.snake = snake

    def generate_apple(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if all(part.x != x or part.y != y for part in self.snake.parts):  # Ensure apple is not on the snake
                self.apple_coords = (x, y)
                break

    def draw_board(self, stdscr):
        global score
        stdscr.clear()  # Clear the screen
        for i in range(self.height):
            for j in range(self.width):
                if (j, i) == self.apple_coords:  # Check if it's an apple
                    stdscr.addstr(i, j, 'A')
                elif any(b.x == j and b.y == i for b in self.snake.parts):  # Check if it's a snake part
                    stdscr.addstr(i, j, self.snake.symbol)
                else:
                    stdscr.addstr(i, j, '-')  # Empty space
        stdscr.addstr(self.height, 10, ("Score: " + str(score)))
        stdscr.refresh()  # Refresh the screen

    def check_apple(self):
        global score
        snakeX = self.snake.parts[0].x
        snakeY = self.snake.parts[0].y
        appleX = self.apple_coords[0]
        appleY = self.apple_coords[1]
        if snakeX == appleX and snakeY == appleY:
            score += 1
            self.snake.eat_apple()
            self.generate_apple()


    def check_collision(self):
        global gameOver
        snakeX = self.snake.parts[0].x
        snakeY = self.snake.parts[0].y
        if snakeX >= self.width or snakeX < 0 or snakeY >= self.height or snakeY < 0:
            gameOver = True
        for i in range(1, len(self.snake.parts)):
            if snakeX == self.snake.parts[i].x and snakeY == self.snake.parts[i].y:
                gameOver = True


def game_render(stdscr):
    global gameOver
    snake = Snake(20, 10, '*')
    board = Board(50, 20, snake)
    board.generate_apple()

    stdscr.nodelay(True)  # moving without stop
    while not gameOver:
        key = stdscr.getch()  # Get the pressed key
        if key in [curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP]:
            snake.direction = key
        snake.move()

        board.check_collision()
        board.check_apple()
        board.draw_board(stdscr)

        time.sleep(0.5)
        if gameOver:
            stdscr.clear()
            stdscr.addstr("GAME OVER!")
            break
        time.sleep(0.5)

    stdscr.refresh()
    stdscr.getch()  # Wait for another key press before exiting


def main():
    curses.wrapper(game_render)


main()
