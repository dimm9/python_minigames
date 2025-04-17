import pygame

pygame.init()

frameW = 1400
frameH = 700

window = pygame.display.set_mode((frameW, frameH))
pygame.display.set_caption("Dungeon")
bg = pygame.image.load('bg.png')
standing = pygame.image.load('standing.png')
enemy = pygame.image.load('enemy.png')
block = pygame.image.load('block.png')
coinIm = pygame.image.load('coin.png')

music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

hitMusic = pygame.mixer.Sound('gun.mp3')
wizardHit = pygame.mixer.Sound('demon.mp3')

walkRight = [pygame.image.load('L1.png'), pygame.image.load('L4.png'), pygame.image.load('L2.png'),  pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L2.png'), pygame.image.load('L1.png')]
walkLeft = [pygame.image.load('R1.png'), pygame.image.load('R4.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R2.png'), pygame.image.load('R1.png')]

clock = pygame.time.Clock()
score = 0
class Player:
    def __init__(self, width, height, vel, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.initX = x
        self.initY = y
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.standing = False
        self.walkCount = 0
        self.isJump = False
        self.on_block = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        if self.walkCount >= 21:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))

    def check_collision(self):
        for block in blocks:
            if (self.x + self.width > block.x and self.x < block.x + block.width and
                    self.y + self.height >= block.y and self.y < block.y + block.height):
                self.on_block = True
                self.y = block.y - self.height - 30
                return
            self.on_block = False




    def hit(self):
        self.x = self.initX
        self.y = self.initY
        self.jumpCount = 10
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 42)
        text = font1.render('You was hit -5!', 1, (200, 50, 50))
        window.blit(text, (self.height/2 + 500, self.width/2 + 250))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class Enemy:
    def __init__(self, width, height, vel, x, y, endX):
        self.x = x
        self.y = y
        self.width = width
        self.endX = endX
        self.height = height
        self.walkCount = 0
        self.vel = vel
        self.health = 10
        self.visible = True
        self.initial = x
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        if self.vel > 0:  # it means what we are moving right
            if self.x + self.vel < self.endX:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.initial:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def draw(self):
        self.move()
        if self.visible:
            window.blit(enemy, (self.x, self.y))
            pygame.draw.rect(window, (255, 0, 10), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, self.health * 10 / 2, 10))
        self.hitbox = (self.x + 20, self.y, 25, 55)

    def hit(self):
        for bullet in bullets:
            if self.health > 0:
                if bullet.x >= self.x and bullet.x <= self.x + self.width:
                    if bullet.y >= self.y and bullet.y <= self.y + self.height:
                        self.health -= 1
            else:
                self.visible = False
                self.x = 0
                self.y = 0
                global score
                score += 10


class Bullet:
    def __init__(self, x, y, radius, side):
        self.x = x
        self.y = y
        self.radius = radius
        self.side = side
        self.velocity = 10 * side

    def draw(self):
        pygame.draw.circle(window, (0, 0, 140), (self.x, self.y), self.radius)
        pygame.display.update()


class Coin:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        if self.visible:
            window.blit(coinIm, (self.x, self.y))



class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        window.blit(block, (self.x, self.y))


coinScore = 0

man = Player(84, 84, 10, 50, 550)
wizards = [Enemy(84, 84, 15, 500, 100, 500+300), Enemy(84, 84, 15, 1100, 200, 1100+200), Enemy(84, 84, 15, 300, 550, 300+200)]

block1 = Block(350, 300, 64, 64)
block2 = Block(600, 200, 64, 64)
block3 = Block(100, 500, 64, 64)
block4 = Block(1200, 300, 64, 64)
block5 = Block(950, 300, 64, 64)
block6 = Block(700, 200, 64, 64)
block7 = Block(800, 500, 64, 64)

coin1 = Coin(610, 130, 50, 50)
coin2 = Coin(110, 430, 50, 50)
coin3 = Coin(1205, 230, 50, 50)

coins = [coin1, coin2, coin3]

blocks = [block1, block2, block3, block4, block5, block6, block7]
bullets = []
shootLoop = 0

font = pygame.font.SysFont('comicsans', 32)
def redrawWin():
    window.blit(bg, (0, 0))
    man.draw()
    text = font.render(f"Score: {score} ", 1, (255, 170, 50))
    text2 = font.render(f"Coins: {coinScore} ", 1, (255, 170, 50))
    window.blit(text, (30, 0))
    window.blit(text2, (1250, 0))
    for wizard in wizards:
        if wizard.visible and wizard.health > 0:
            wizard.draw()
        else:
            text3 = font.render(f"+1 Kill! ", 1, (200, 50, 50))
            window.blit(text3, (700, 350))
            wizards.pop(wizards.index(wizard))
    for coin in coins:
        coin.draw()
    for block in blocks:
        block.draw()
    for bullet in bullets:
        bullet.draw()
    pygame.display.update()


# main loop
gameOver = False

while not gameOver:
    clock.tick(21)
    pygame.time.delay(100)
    man.check_collision()
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    man.check_collision()

    if not man.on_block:
        if man.y < frameH - man.height - 100 and man.y >= 0:
            man.y += 5
    elif man.on_block:
        man.y = man.y

    for wizard in wizards:
        if wizard.visible:
            if man.x < wizard.x + wizard.width and man.x + man.width > wizard.x:
                if man.y + man.height > wizard.y and man.y < wizard.y + wizard.height:
                    man.hit()
                    score -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    for coin in coins:
        if man.x >= coin.x and man.x < coin.x + coin.width:
            if man.y > coin.y - coin.height and man.y < coin.y:
                coin.visible = False
                coin.x = -1
                coin.y = -1
                coinScore += 1

    for bullet in bullets:
        if bullet.x > 0 and bullet.x < frameW:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
        for wizard in wizards:
            if wizard.x < bullet.x and wizard.x + wizard.width > bullet.x:
                if bullet.y > wizard.y and bullet.y < wizard.y + wizard.height:
                    wizard.hit()
                    wizardHit.play()
                    score += 1
                    bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        hitMusic.play()
        facing = 1
        if man.left:
            facing = -1
        elif man.right:
            facing = 1
        if len(bullets) < 5:
            bullets.append(
                Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, facing))
        shootLoop += 1

    if keys[pygame.K_RIGHT] and man.x < frameW - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False

    elif keys[pygame.K_LEFT] and man.x >= man.width + man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0
        man.check_collision()

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.jumpCount += 1

    else:
        temp = man.y
        if man.jumpCount >= -11:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg  # quadratic equation(multiply by 0.5 to decrease jump height)
            man.jumpCount -= 1
            man.check_collision()

        else:
            man.isJump = False
            man.jumpCount = 10
    redrawWin()


pygame.quit()