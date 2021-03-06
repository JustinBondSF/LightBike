
import pygame

pygame.init()
clock = pygame.time.Clock()
screenWidth, screenHeight = 512, 512
screen = pygame.display.set_mode((screenWidth, screenHeight))
space = []

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255,255,255)
grey = (128,128,128,0)
screen.fill(black)


def Grid():
    blockSize = 32 #Set the size of the grid block
    for x in range(screenWidth): # this grid is purely for visual purposes
        for y in range(screenHeight):
            rect = pygame.Rect(x*blockSize, y*blockSize,
            blockSize, blockSize)
            pygame.draw.rect(screen, grey, rect, 1)
    for i in range(64): # a grid to track where the player can go/has been
        space.append([])
        for j in range(64):
            space[i].append(0)






class Player:
    def __init__(self,x,y, color):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 6
        self.color = color
        self.direction = 0


    def update(self, up, left, right, down, wintext):
            global running
            global winner
            global space
            if self.x+self.w > 512 or self.y+self.h > 512 or self.x < 0 or self.y < 0: # if the player hits the edge of the screen
                running = False
                winner = f'{wintext} wins'
                return None
            if self.x % 8 == 0 and self.y % 8 == 0: # if the player is on a grid square
                if space[self.x//8][self.y//8] == 1: # if the player hits a wall or the trail of another player
                    running = False
                    print("test")
                    winner = f'{wintext} wins'
                    return None
            # if two players are on the same grid square


                space[self.x//8][self.y//8] = 1 # if the player is on a grid square, set the space to 1 (trail)

            keys = pygame.key.get_pressed()
            # dont let players turn in the exact opposite direction, keep them on the grid
            if keys[up] and self.x % 8 == 0 and self.direction != 3:
                self.direction = 1
            if keys[down] and self.x % 8 == 0 and self.direction != 1:
                self.direction = 3
            if keys[right] and self.y % 8 == 0 and self.direction != 2:
                self.direction = 0
            if keys[left] and self.y % 8 == 0 and self.direction != 0 :
                self.direction = 2

            if self.direction == 0:
                self.x += 2
            if self.direction == 1:
                self.y -= 2
            if self.direction == 2:
                self.x -= 2
            if self.direction == 3:
                self.y += 2


    def draw(self, screen):
        #represent the player as a rectangle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

    def reset(self,):
        self.__init__(self.x, self.y, self.color)


def startMenu():
    global start
    start = True
    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False
                    return None

        screen.fill(black)
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Press Space to start', True, white)
        screen.blit(text, (screenWidth/2 - text.get_width()/2, screenHeight/2 - text.get_height()/2))
        pygame.display.update()
        clock.tick(15)





player1 = Player(0,256,blue)
player2 = Player(500,256,red)
player2.direction = 2


# Game Loop
start = True
running = True
winner = None
def main():
    global start
    global running
    global winner
    screen.fill(black)
    Grid()
    while running:
        if start:
            startMenu()

        if winner == None:
            if start == False:


    #init gameworld

                player1.draw(screen)
                player2.draw(screen)


        # Process input (events)
                for event in pygame.event.get():
            # check for closing window
                    if event.type == pygame.QUIT:
                        running = False
                player1.update(pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_DOWN,"red")
                player2.update(pygame.K_w,pygame.K_a,pygame.K_d,pygame.K_s,"blue")
                if winner != None:
                    pygame.font.init()
                    font = pygame.font.SysFont("Futura", 32)
                    wintext = font.render(winner,True,white)
                    screen.blit(wintext,(screenWidth/2, screenHeight/2))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    player1.reset()
                    player2.reset()
                    winner = None



        # Update
                pygame.display.flip()
                clock.tick(60)
startMenu()
main()
pygame.quit()