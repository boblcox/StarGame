import pygame
import random

# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
OFFWHITE = [215, 215, 215]
RED = [255, 0 ,0]
GREEN = [0, 238, 0]
CYAN = [0, 238, 238]
sizex = 1600
sizey = 1000
# Set the height and width of the screen
SIZE = [sizex, sizey]
Font = pygame.font.SysFont('freesansbold.ttf',  72)
Font1 = pygame.font.SysFont('freesansbold.ttf',  124)
font = pygame.font.SysFont('freesansbold.ttf',  45)
font1 = pygame.font.SysFont('freesansbold.ttf',  24)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Star Game")

# Create an empty array
star_list01 = []
star_list02 = []
star_list03 = []
star_list04 = []
star_list05 = []
star_list06 = []
planet_list1 = []
planet_list2 = []
planet_list3 = []
#planet_list4 = []
planet_list5 = []
star_list1 = []
star_list2 = []
star_list3 = []
blast_list = []
astroidinfo1 = [random.randrange(50, 1550), random.randrange(-3000, -2700), random.randrange(200, 300), 2, 'astroid1.png']
astroidinfo2 = [random.randrange(50, 1550), random.randrange(-3000, -2700), random.randrange(200, 300), 2, 'astroid1.png']
astroidinfo3 = [random.randrange(50, 1550), random.randrange(-3000, -2700), random.randrange(200, 300), 2, 'astroid1.png']
alien1 = [random.randrange(50, 1550), -25, 25, 3, 'ship2.png']
alien2 = [random.randrange(50, 1550), -25, 25, 3, 'ship2.png']
alien3 = [random.randrange(50, 1550), -25, 25, 3, 'ship2.png']
alien4 = [random.randrange(50, 1550), -25, 25, 3, 'ship2.png']
alien5 = [random.randrange(50, 1550), -25, 25, 3, 'ship2.png']
alien1right = [-100, random.randrange(500, 1450), 25, 3, 'ship2.png']
alien2right = [-100, random.randrange(500, 1450), 25, 3, 'ship2.png']
alien1left = [1700, random.randrange(500, 1450), 25, 3, 'ship2.png']
alien2left = [1700, random.randrange(500, 1450), 25, 3, 'ship2.png']
alien1_type1 = [random.randrange(50, 1550), -25, 25, 3, 'ship3.png']
alien2_type1 = [random.randrange(50, 1550), -25, 25, 3, 'ship3.png']
alien3_type1 = [random.randrange(50, 1550), -25, 25, 3, 'ship3.png']
alien1_type2 = [random.randrange(50, 1550), -25, 25, 3, 'ship5.png']
alien2_type2 = [random.randrange(50, 1550), -25, 25, 3, 'ship5.png']
alien3_type2 = [random.randrange(50, 1550), -25, 25, 3, 'ship5.png']
gunup = [random.randrange(50, 1550), -25, random.randrange(200, 400), 'powerup1.png']
shieldup = [random.randrange(50, 1550), -25, random.randrange(200, 400), 'powerup2.png']
lifeup = [random.randrange(50, 1550), -25, random.randrange(1000, 1500), 'powerup3.png']
blast = False
score = 0
health = 100
lives = 3
menu = True
menuselect = 1
forcenewgame = True
guntimer = 0
gunmode = 1
shields = 0
gameover = False


star1 = pygame.image.load("star1.png").convert()
star1.set_colorkey(BLACK)

star2 = pygame.image.load("star2.png").convert()
star2.set_colorkey(BLACK)

star3 = pygame.image.load("star3.png").convert()
star3.set_colorkey(BLACK)

star4 = pygame.image.load("star4.png").convert()
star4.set_colorkey(BLACK)

star5 = pygame.image.load("star5.png").convert()
star5.set_colorkey(BLACK)

star6 = pygame.image.load("star6.png").convert()
star6.set_colorkey(BLACK)

planet1 = pygame.image.load("planet1.png").convert()
planet1.set_colorkey(BLACK)

planet2 = pygame.image.load("planet2.png").convert()
planet2.set_colorkey(BLACK)

planet3 = pygame.image.load("planet3.png").convert()
planet3.set_colorkey(BLACK)

#planet4 = pygame.image.load("planet4.png").convert()
#planet4.set_colorkey(BLACK)

planet5 = pygame.image.load("planet5.png").convert()
planet5.set_colorkey(BLACK)

# !
explan = pygame.image.load("!.png").convert()
explan.set_colorkey(BLACK)

#astroids
astroid1 = pygame.image.load("astroid1.png").convert()
astroid1.set_colorkey(BLACK)

#aliens1
ship2 = pygame.image.load("ship2.png").convert()
ship2.set_colorkey(BLACK)

#aliens1right
ship2right = pygame.image.load("ship2right.png").convert()
ship2right.set_colorkey(BLACK)

#aliens1right
ship2left = pygame.image.load("ship2left.png").convert()
ship2left.set_colorkey(BLACK)

#aliens1_type1
ship3 = pygame.image.load("ship3.png").convert()
ship3.set_colorkey(BLACK)

#aliens1_type2
ship5 = pygame.image.load("ship5.png").convert()
ship5.set_colorkey(BLACK)

#powerups
powerup1 = pygame.image.load("powerup1.png").convert()
powerup1.set_colorkey(BLACK)

powerup2 = pygame.image.load("powerup2.png").convert()
powerup2.set_colorkey(BLACK)

powerup3 = pygame.image.load("powerup3.png").convert()
powerup3.set_colorkey(BLACK)

# good-looking stars
for i in range(10):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list01.append([x, y])
for i in range(10):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list02.append([x, y])
for i in range(10):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list03.append([x, y])
for i in range(10):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list04.append([x, y])
for i in range(10):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list05.append([x, y])
for i in range(3):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list06.append([x, y])

# planets
for i in range(1):
    x = random.randrange(0, sizex)
    y = random.randrange(-20000, 2000)
    planet_list1.append([x, y])
for i in range(1):
    x = random.randrange(0, sizex)
    y = random.randrange(-20000, 2000)
    planet_list2.append([x, y])
for i in range(1):
    x = random.randrange(0, sizex)
    y = random.randrange(-20000, 2000)
    planet_list3.append([x, y])
#for i in range(1):
#    x = random.randrange(0, sizex)
#    y = random.randrange(-20000, 2000)
#    planet_list4.append([x, y])
for i in range(1):
    x = random.randrange(0, sizex)
    y = random.randrange(-20000, 2000)
    planet_list5.append([x, y])

# Loop 50 times and add a star in a random x,y position
for i in range(20):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list1.append([x, y])

for i in range(12):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list2.append([x, y])

for i in range(6):
    x = random.randrange(0, sizex)
    y = random.randrange(0, sizey)
    star_list3.append([x, y])

#astroid
#for i in range(1):
#    x = random.randrange(50, 1550),
#    y = random.randrange(-600, -200),
#    z = random.randrange(30, 40)
#    a = 'astroid1.png'
#    astroidinfo1: type(list) = [x, y, z, a]

# create player
player_image = pygame.image.load("ship1.png").convert()
player_image.set_colorkey(BLACK)

ship1right = pygame.image.load("ship1right.png").convert()
ship1right.set_colorkey(BLACK)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 800
y_coord = 800

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            if menu is False:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -30
                elif event.key == pygame.K_RIGHT:
                    x_speed = 30
                elif event.key == pygame.K_UP:
                    y_speed = -30
                elif event.key == pygame.K_DOWN:
                    y_speed = 30
                if event.key == pygame.K_SPACE:
                    blast = True
                elif event.key == pygame.K_ESCAPE:
                    menu = True
            if menu is True:
                if event.key == pygame.K_DOWN:
                    menuselect += 1
                    if menuselect > 3:
                        menuselect = 3
                elif event.key == pygame.K_UP:
                    menuselect -= 1
                    if menuselect < 1:
                        menuselect = 1
                elif event.key == pygame.K_RETURN:
                    if menuselect == 1:
                        menu = False
                    if menuselect == 2:
                        score = 0
                        health = 100
                        lives = 3
                        menu = False
                        forcenewgame = False
                        gameover = False
                    if menuselect == 3:
                        pygame.QUIT
                        done = True  # Flag that we are done so we exit this loop

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            if event.key == pygame.K_SPACE:
                blast = False



    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    # boundry rules
    if x_coord > sizex:
        x_coord = 0
    elif x_coord < 0:
        x_coord = sizex
    elif y_coord < 300:
        y_coord = 300
    elif y_coord > 800:
        y_coord = 800

    # Set the screen background
    screen.fill(BLACK)
    if menu is True:
        menutext1 = Font1.render("!!!STAR GAME!!!", True, WHITE)
        menutext2 = font.render("IN EARLY DEVELOPMENT", True, RED)
        menutext3 = Font.render("CONTINUE", True, WHITE)
        menutext4 = Font.render("NEW GAME", True, WHITE)
        menutext5 = Font.render("EXIT", True, WHITE)
        screen.blit(menutext1, (sizex*.3, sizey*.3))
        screen.blit(menutext2, (sizex*.4, sizey*.38))
        if forcenewgame is False:
            screen.blit(menutext3, (sizex*.42, sizey*.5))
        screen.blit(menutext4, (sizex*.42, sizey*.6))
        screen.blit(menutext5, (sizex*.42, sizey*.7))

        # Menu selecter
        if menuselect == 1:
            if forcenewgame is False:
                #pygame.draw.circle(screen, WHITE, [590, 825], 30)
                screen.blit(ship1right, [sizex*.3, sizey*.47])
            if forcenewgame is True:
                menuselect = 2
        elif menuselect == 2:
            #pygame.draw.circle(screen, WHITE, [590, 925], 30)
            screen.blit(ship1right, [sizex*.3, sizey*.57])
        elif menuselect == 3:
            #pygame.draw.circle(screen, WHITE, [590, 1025], 30)
            screen.blit(ship1right, [sizex*.3, sizey*.67])
        if gameover is True:
            scoretext = ("LAST GAME : SCORE : " + str(score))
            gameovertext = Font1.render("GAME OVER", True, WHITE)
            menutext6 = font.render(scoretext, True, WHITE)
            screen.blit(gameovertext, (sizex*.3, sizey*.5))
            screen.blit(menutext6, (sizex*.35, sizey*.6))
        elif forcenewgame is False:
            scoretext = ("CURRENT GAME : SCORE : " + str(score) + "   HEALTH : " + str(health) + "   LIVES : " + str(lives))
            menutext6 = font.render(scoretext, True, WHITE)
            screen.blit(menutext6, (sizex*.3, sizey*.85))

    if menu is False:
        # Process good looking stars 01
        for i in range(len(star_list01)):
            screen.blit(star1, star_list01[i])
            # Move the star down
            star_list01[i][1] += 7
            # If the star has moved off the bottom of the screen
            if star_list01[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list01[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list01[i][0] = x

        # Process good looking stars 02
        for i in range(len(star_list02)):
            screen.blit(star2, star_list02[i])
            # Move the star down
            star_list02[i][1] += 6
            # If the star has moved off the bottom of the screen
            if star_list02[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list02[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list02[i][0] = x

        # Process good looking stars 03
        for i in range(len(star_list03)):
            screen.blit(star3, star_list03[i])
            # Move the star down
            star_list03[i][1] += 5
            # If the star has moved off the bottom of the screen
            if star_list03[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list03[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list03[i][0] = x

        # Process good looking stars 04
        for i in range(len(star_list04)):
            screen.blit(star4, star_list04[i])
            # Move the star down
            star_list04[i][1] += 4
            # If the star has moved off the bottom of the screen
            if star_list04[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list04[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list04[i][0] = x

        # Process good looking stars 05
        for i in range(len(star_list05)):
            screen.blit(star5, star_list05[i])
            # Move the star down
            star_list05[i][1] += 3
            # If the star has moved off the bottom of the screen
            if star_list05[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list05[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list05[i][0] = x

        # Process good looking stars 06
        for i in range(len(star_list06)):
            screen.blit(star6, star_list06[i])
            # Move the star down
            star_list06[i][1] += 2
            # If the star has moved off the bottom of the screen
            if star_list06[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list06[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list06[i][0] = x

        # planets
        for i in range(len(planet_list1)):
            screen.blit(planet1, planet_list1[i])
            # Move the star down
            planet_list1[i][1] += 15
            # If the star has moved off the bottom of the screen
            if planet_list1[i][1] > 2000:
                # Reset it just above the top
                y = random.randrange(-20000, -200)
                planet_list1[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 1600)
                planet_list1[i][0] = x

        for e in range(len(planet_list2)):
            screen.blit(planet3, planet_list2[e])
            # Move the star down
            planet_list2[e][1] += 12
            # If the star has moved off the bottom of the screen
            if planet_list2[e][1] > 2000:
                # Reset it just above the top
                y = random.randrange(-20000, -200)
                planet_list2[e][1] = y
                # Give it a new x position
                x = random.randrange(0, 1600)
                planet_list2[e][0] = x

        for i in range(len(planet_list3)):
            screen.blit(planet2, planet_list3[i])
            # Move the star down
            planet_list3[i][1] += 10
            # If the star has moved off the bottom of the screen
            if planet_list3[i][1] > 2000:
                # Reset it just above the top
                y = random.randrange(-20000, -200)
                planet_list3[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 1600)
                planet_list3[i][0] = x

    #    for i in range(len(planet_list4)):
    #        screen.blit(planet4, planet_list4[i])
    #        # Move the star down
    #        planet_list4[i][1] += 11
    #        # If the star has moved off the bottom of the screen
    #        if planet_list4[i][1] > 2000:
    #            # Reset it just above the top
    #            y = random.randrange(-20000, -200)
    #            planet_list4[i][1] = y
    #            # Give it a new x position
    #            x = random.randrange(0, 1600)
    #            planet_list4[i][0] = x

        for i in range(len(planet_list5)):
            screen.blit(planet5, planet_list5[i])
            # Move the star down
            planet_list5[i][1] += 10
            # If the star has moved off the bottom of the screen
            if planet_list5[i][1] > 2000:
                # Reset it just above the top
                y = random.randrange(-20000, -200)
                planet_list5[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 1600)
                planet_list5[i][0] = x

        # Process each star in the list 1
        for i in range(len(star_list1)):
            # Draw the star
            pygame.draw.circle(screen, WHITE, star_list1[i], 2)
            # Move the star down
            star_list1[i][1] += 20
            # If the star has moved off the bottom of the screen
            if star_list1[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list1[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list1[i][0] = x

        # Process each star in the list 2
        for i in range(len(star_list2)):
            # Draw the star
            pygame.draw.circle(screen, WHITE, star_list2[i], 3)
            # Move the star down
            star_list2[i][1] += 30
            # If the star has moved off the bottom of the screen
            if star_list2[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list2[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list2[i][0] = x

        # Process each star in the list 3
        for i in range(len(star_list3)):
            # Draw the star
            pygame.draw.circle(screen, WHITE, star_list3[i], 4)
            # Move the star down
            star_list3[i][1] += 40
            # If the star has moved off the bottom of the screen
            if star_list3[i][1] > sizey:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                star_list3[i][1] = y
                # Give it a new x position
                x = random.randrange(0, sizex)
                star_list3[i][0] = x
        #call blasts
        for i in range(len(blast_list)):
            # Move the star down
            blast_list[i][1] -= 50
            if blast_list[i][1] > 0:
                # Draw the star
                pygame.draw.circle(screen, RED, blast_list[i], 3)
            if astroidinfo1[0]-10 <= blast_list[i][0]+20 <= astroidinfo1[0]+55 and astroidinfo1[1]-10 <= blast_list[i][1] \
                    <= astroidinfo1[1]+40 and blast_list[i][1] > 5:
                astroidinfo1[3] -= 1
                blast_list[i][1] -= 1600
            if astroidinfo2[0]-10 <= blast_list[i][0]+20 <= astroidinfo2[0]+55 and astroidinfo2[1]-10 <= blast_list[i][1] \
                    <= astroidinfo2[1]+40 and blast_list[i][1] > 5:
                astroidinfo2[3] -= 1
                blast_list[i][1] -= 1600
            if astroidinfo3[0] - 10 <= blast_list[i][0] + 20 <= astroidinfo3[0] + 55 and astroidinfo3[1] - 10 <= \
                    blast_list[i][1] <= astroidinfo3[1] + 40 and blast_list[i][1] > 5:
                astroidinfo3[3] -= 1
                blast_list[i][1] -= 1600
            if alien1[0] <= blast_list[i][0] <= alien1[0] + 120 and alien1[1] - 10 <= \
                    blast_list[i][1] <= alien1[1] + 30 and blast_list[i][1] > 5:
                alien1[3] -= 1
                blast_list[i][1] -= 1600
            if alien2[0] <= blast_list[i][0] <= alien2[0] + 120 and alien2[1] - 10 <= \
                    blast_list[i][1] <= alien2[1] + 30 and blast_list[i][1] > 5:
                alien2[3] -= 1
                blast_list[i][1] -= 1600
            if alien3[0] <= blast_list[i][0] <= alien3[0] + 120 and alien3[1] - 10 <= \
                    blast_list[i][1] <= alien3[1] + 30 and blast_list[i][1] > 5:
                alien3[3] -= 1
                blast_list[i][1] -= 1600
            if alien4[0] <= blast_list[i][0] <= alien4[0] + 120 and alien4[1] - 10 <= \
                    blast_list[i][1] <= alien4[1] + 30 and blast_list[i][1] > 5:
                alien4[3] -= 1
                blast_list[i][1] -= 1600
            if alien5[0] <= blast_list[i][0] <= alien5[0] + 120 and alien5[1] - 10 <= \
                    blast_list[i][1] <= alien5[1] + 30 and blast_list[i][1] > 5:
                alien5[3] -= 1
                blast_list[i][1] -= 1600
            if alien1right[0] <= blast_list[i][0] <= alien1right[0] + 120 and alien1right[1] - 10 <= \
                    blast_list[i][1] <= alien1right[1] + 30 and blast_list[i][1] > 5:
                alien1right[3] -= 1
                blast_list[i][1] -= 1600
            if alien2right[0] <= blast_list[i][0] <= alien2right[0] + 120 and alien2right[1] - 10 <= \
                    blast_list[i][1] <= alien2right[1] + 30 and blast_list[i][1] > 5:
                alien2right[3] -= 1
                blast_list[i][1] -= 1600
            if alien1left[0] <= blast_list[i][0] <= alien1left[0] + 120 and alien1left[1] - 10 <= \
                    blast_list[i][1] <= alien1left[1] + 30 and blast_list[i][1] > 5:
                alien1left[3] -= 1
                blast_list[i][1] -= 1600
            if alien2left[0] <= blast_list[i][0] <= alien2left[0] + 120 and alien2left[1] - 10 <= \
                    blast_list[i][1] <= alien2left[1] + 30 and blast_list[i][1] > 5:
                alien2left[3] -= 1
                blast_list[i][1] -= 1600
            if alien1_type1[0] <= blast_list[i][0] <= alien1_type1[0] + 120 and alien1_type1[1] - 10 <= \
                    blast_list[i][1] <= alien1_type1[1] + 30 and blast_list[i][1] > 5:
                alien1_type1[3] -= 1
                blast_list[i][1] -= 1600
            if alien2_type1[0] <= blast_list[i][0] <= alien2_type1[0] + 120 and alien2_type1[1] - 10 <= \
                    blast_list[i][1] <= alien2_type1[1] + 30 and blast_list[i][1] > 5:
                alien2_type1[3] -= 1
                blast_list[i][1] -= 1600
            if alien3_type1[0] <= blast_list[i][0] <= alien3_type1[0] + 120 and alien3_type1[1] - 10 <= \
                    blast_list[i][1] <= alien3_type1[1] + 30 and blast_list[i][1] > 5:
                alien3_type1[3] -= 1
                blast_list[i][1] -= 1600
            if alien1_type2[0] <= blast_list[i][0] <= alien1_type2[0] + 120 and alien1_type2[1] - 10 <= \
                    blast_list[i][1] <= alien1_type2[1] + 30 and blast_list[i][1] > 5:
                alien1_type2[3] -= 1
                blast_list[i][1] -= 1600
            if alien2_type2[0] <= blast_list[i][0] <= alien2_type2[0] + 120 and alien2_type2[1] - 10 <= \
                    blast_list[i][1] <= alien2_type2[1] + 30 and blast_list[i][1] > 5:
                alien2_type2[3] -= 1
                blast_list[i][1] -= 1600
            if alien3_type2[0] <= blast_list[i][0] <= alien3_type2[0] + 120 and alien3_type2[1] - 10 <= \
                    blast_list[i][1] <= alien3_type2[1] + 30 and blast_list[i][1] > 5:
                alien3_type2[3] -= 1
                blast_list[i][1] -= 1600

        #create blasts:
        if blast is True:
            if gunmode == 1:
                if guntimer <= 1:
                    x = x_coord + 53
                    y = y_coord
                    blast_list.append([x, y])
                    guntimer += 2
                else:
                    guntimer -= 1
        if blast is True:
            if gunmode == 2:
                x = x_coord + 53
                y = y_coord
                blast_list.append([x, y])
                guntimer -= 1
        if blast is True:
            if gunmode == 3:
                x = x_coord + 33
                y = y_coord
                blast_list.append([x, y])
                a = x_coord + 73
                b = y_coord
                blast_list.append([a, b])
                guntimer -= 1
        if blast is True:
            if gunmode == 4:
                x = x_coord + 13
                y = y_coord
                blast_list.append([x, y])
                a = x_coord + 53
                b = y_coord
                blast_list.append([a, b])
                c = x_coord + 93
                d = y_coord
                blast_list.append([c, d])
                guntimer -= 1

        #call astroids
        #print(astroidinfo1)
        if astroidinfo1[2] <= 1:
            screen.blit(astroid1, [astroidinfo1[0], astroidinfo1[1]])
            if astroidinfo1[1] <= -1300 or -1000 <= astroidinfo1[1] <= -700 or -400 <= astroidinfo1[1] <= -100:
                screen.blit(explan, [astroidinfo1[0], 20])
            astroidinfo1[1] += 45
        elif astroidinfo1[2] >= 1:
            astroidinfo1[2] -= 1
        if astroidinfo1[1] > 1800 or astroidinfo1[3] < 1:
            astroidinfo1[1] = random.randrange(-3000, -2700)
            astroidinfo1[0] = random.randrange(50, sizex - 50)
            astroidinfo1[2] += 150
            score += 10
            astroidinfo1[3] = 2
        if x_coord-10 <= astroidinfo1[0]+8 <= x_coord+110  and y_coord-10 <= astroidinfo1[1]+8 <= y_coord+50:
            health -= 26
            astroidinfo1[1] = random.randrange(-3000, -2700)
            astroidinfo1[0] = random.randrange(50, sizex - 50)
            astroidinfo1[2] += 150

        if score > 100:
            if astroidinfo2[2] <= 1:
                screen.blit(astroid1, [astroidinfo2[0], astroidinfo2[1]])
                if astroidinfo2[1] <= -1300 or -1000 <= astroidinfo2[1] <= -700 or -400 <= astroidinfo2[1] <= -100:
                    screen.blit(explan, [astroidinfo2[0], 20])
                astroidinfo2[1] += 45
            elif astroidinfo2[2] >= 1:
                astroidinfo2[2] -= 1
            if astroidinfo2[1] > 1800 or astroidinfo2[3] < 1:
                astroidinfo2[1] = random.randrange(-3000, -2700)
                astroidinfo2[0] = random.randrange(50, sizex - 50)
                astroidinfo2[2] += 150
                score += 10
                astroidinfo2[3] = 2
            if x_coord - 10 <= astroidinfo2[0] + 8 <= x_coord + 110 and y_coord - 10 <= astroidinfo2[1] + 8 <= y_coord + 50:
                health -= 26
                astroidinfo2[1] = random.randrange(-3000, -2700)
                astroidinfo2[0] = random.randrange(50, sizex - 50)
                astroidinfo2[2] += 150

        if score > 300:
            if astroidinfo3[2] <= 1:
                screen.blit(astroid1, [astroidinfo3[0], astroidinfo3[1]])
                if astroidinfo3[1] <= -1300 or -1000 <= astroidinfo3[1] <= -700 or -400 <= astroidinfo3[1] <= -100:
                    screen.blit(explan, [astroidinfo3[0], 20])
                astroidinfo3[1] += 45
            elif astroidinfo3[2] >= 1:
                astroidinfo3[2] -= 1
            if astroidinfo3[1] > 1800 or astroidinfo3[3] < 1:
                astroidinfo3[1] = random.randrange(-3000, -2700)
                astroidinfo3[0] = random.randrange(50, sizex - 50)
                astroidinfo3[2] += 150
                score += 10
                astroidinfo3[3] = 2
            if x_coord - 10 <= astroidinfo3[0] + 8 <= x_coord + 110 and y_coord - 10 <= astroidinfo3[1] + 8 <= y_coord + 50:
                health -= 26
                astroidinfo3[1] = random.randrange(-3000, -2700)
                astroidinfo3[0] = random.randrange(50, sizex - 50)
                astroidinfo3[2] += 150

        #aliens
        if score >= 5:
            if alien1[2] <= 1:
                screen.blit(ship2, [alien1[0], alien1[1]])
                alien1[1] += 12
            elif alien1[2] >= 1:
                alien1[2] -= 1
            if alien1[1] > 1800 or alien1[3] < 1:
                alien1[1] = -25
                alien1[0] = random.randrange(50, sizex - 50)
                alien1[2] += 150
                score += 25
                alien1[3] = 3
            if x_coord - 50 <= alien1[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien1[
                1] + 8 <= y_coord + 50:
                health -= 35
                alien1[1] = -25
                alien1[0] = random.randrange(50, sizex - 50)
                alien1[2] += 150
            if x_coord < alien1[0]:
                alien1[0] -= 2
                if x_coord < alien1[0]+200:
                    alien1[0] -= 4
            if x_coord > alien1[0]:
                alien1[0] += 2
                if x_coord > alien1[0]-200:
                    alien1[0] += 4

        if score >= 50:
            if alien2[2] <= 1:
                screen.blit(ship2, [alien2[0], alien2[1]])
                alien2[1] += 12
            elif alien2[2] >= 1:
                alien2[2] -= 1
            if alien2[1] > 1800 or alien2[3] < 1:
                alien2[1] = -25
                alien2[0] = random.randrange(50, sizex - 50)
                alien2[2] += 150
                score += 25
                alien2[3] = 3
            if x_coord - 50 <= alien2[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien2[
                1] + 8 <= y_coord + 50:
                health -= 35
                alien2[1] = -25
                alien2[0] = random.randrange(50, sizex - 50)
                alien2[2] += 150
            if x_coord < alien2[0]:
                alien2[0] -= 2
                if x_coord < alien2[0]+200:
                    alien2[0] -= 4
            if x_coord > alien2[0]:
                alien2[0] += 2
                if x_coord > alien2[0]-200:
                    alien2[0] += 4

        if score >= 150:
            if alien3[2] <= 1:
                screen.blit(ship2, [alien3[0], alien3[1]])
                alien3[1] += 12
            elif alien3[2] >= 1:
                alien3[2] -= 1
            if alien3[1] > 1800 or alien3[3] < 1:
                alien3[1] = -25
                alien3[0] = random.randrange(50, sizex - 50)
                alien3[2] += 150
                score += 25
                alien3[3] = 3
            if x_coord - 50 <= alien3[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien3[
                1] + 8 <= y_coord + 50:
                health -= 35
                alien3[1] = -25
                alien3[0] = random.randrange(50, sizex - 50)
                alien3[2] += 150
            if x_coord < alien3[0]:
                alien3[0] -= 2
                if x_coord < alien3[0]+200:
                    alien3[0] -= 4
            if x_coord > alien3[0]:
                alien3[0] += 2
                if x_coord > alien3[0]-200:
                    alien3[0] += 4

        if score >= 250:
            if alien4[2] <= 1:
                screen.blit(ship2, [alien4[0], alien4[1]])
                alien4[1] += 12
            elif alien4[2] >= 1:
                alien4[2] -= 1
            if alien4[1] > 1800 or alien4[3] < 1:
                alien4[1] = -25
                alien4[0] = random.randrange(50, sizex - 50)
                alien4[2] += 150
                score += 25
                alien4[3] = 3
            if x_coord - 50 <= alien4[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien4[
                1] + 8 <= y_coord + 50:
                health -= 35
                alien4[1] = -25
                alien4[0] = random.randrange(50, sizex - 50)
                alien4[2] += 150
            if x_coord < alien4[0]:
                alien4[0] -= 2
                if x_coord < alien4[0]+200:
                    alien4[0] -= 4
            if x_coord > alien4[0]:
                alien4[0] += 2
                if x_coord > alien4[0]-200:
                    alien4[0] += 4

        if score >= 350:
            if alien5[2] <= 1:
                screen.blit(ship2, [alien5[0], alien5[1]])
                alien5[1] += 12
            elif alien5[2] >= 1:
                alien5[2] -= 1
            if alien5[1] > 1800 or alien5[3] < 1:
                alien5[1] = -25
                alien5[0] = random.randrange(50, sizex - 50)
                alien5[2] += 150
                score += 25
                alien5[3] = 3
            if x_coord - 50 <= alien5[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien5[
                1] + 8 <= y_coord + 50:
                health -= 35
                alien5[1] = -25
                alien5[0] = random.randrange(50, sizex - 50)
                alien5[2] += 150
            if x_coord < alien5[0]:
                alien5[0] -= 2
                if x_coord < alien5[0]+200:
                    alien5[0] -= 4
            if x_coord > alien5[0]:
                alien5[0] += 2
                if x_coord > alien5[0]-200:
                    alien5[0] += 4

        # right aliens
        if score >= 450:
            if alien2right[2] <= 1:
                screen.blit(ship2right, [alien2right[0], alien2right[1]])
                alien2right[0] += 12
            elif alien2right[2] >= 1:
                alien2right[2] -= 1
                if 5 <= alien2right[2] <= 30 or 45 <= alien2right[2] <= 70 or 85 <= alien2right[2] <= 110:
                    screen.blit(explan, [20, alien2right[1]])
            if alien2right[0] > 1700 or alien2right[3] < 1:
                alien2right[0] = -100
                alien2right[1] = random.randrange(500, 1450)
                alien2right[2] += 300
                score += 35
                alien2right[3] = 3
            if x_coord - 90 <= alien2right[0] <= x_coord + 90 and y_coord - 90 <= alien2right[1] <= y_coord \
                    + 90:
                health -= 35
                alien2right[0] = -100
                alien2right[1] = random.randrange(500, 1450)
                alien2right[2] += 300
            if y_coord < alien2right[1]:
                alien2right[1] -= 2
                if y_coord < alien2right[1] + 200:
                    alien2right[1] -= 4
            if y_coord > alien2right[1]:
                alien2right[1] += 2
                if y_coord > alien2right[1] - 200:
                    alien2right[1] += 4

        # right aliens
        if score >= 1250:
            if alien1right[2] <= 1:
                screen.blit(ship2right, [alien1right[0], alien1right[1]])
                alien1right[0] += 12
            elif alien1right[2] >= 1:
                alien1right[2] -= 1
                if 5 <= alien1right[2] <= 30 or 45 <= alien1right[2] <= 70 or 85 <= alien1right[2] <= 110:
                    screen.blit(explan, [20, alien1right[1]])
            if alien1right[0] > 1700 or alien1right[3] < 1:
                alien1right[0] = -100
                alien1right[1] = random.randrange(500, 1450)
                alien1right[2] += 300
                score += 35
                alien1right[3] = 3
            if x_coord - 90 <= alien1right[0] <= x_coord + 90 and y_coord - 90 <= alien1right[1] <= y_coord \
                    + 90:
                health -= 35
                alien1right[0] = -100
                alien1right[1] = random.randrange(500, 1450)
                alien1right[2] += 300
            if y_coord < alien1right[1]:
                alien1right[1] -= 2
                if y_coord < alien1right[1] + 200:
                    alien1right[1] -= 4
            if y_coord > alien1right[1]:
                alien1right[1] += 2
                if y_coord > alien1right[1] - 200:
                    alien1right[1] += 4

        # left aliens
        if score >= 550:
            if alien1left[2] <= 1:
                screen.blit(ship2left, [alien1left[0], alien1left[1]])
                alien1left[0] -= 12
            elif alien1left[2] >= 1:
                alien1left[2] -= 1
                if 5 <= alien1left[2] <= 30 or 45 <= alien1left[2] <= 70 or 85 <= alien1left[2] <= 110:
                    screen.blit(explan, [1580, alien1left[1]])
            if alien1left[0] < -100 or alien1left[3] < 1:
                alien1left[0] = 1700
                alien1left[1] = random.randrange(500, 1450)
                alien1left[2] += 300
                score += 35
                alien1left[3] = 3
            if x_coord - 90 <= alien1left[0] <= x_coord + 90 and y_coord - 90 <= alien1left[1] <= y_coord \
                    + 90:
                health -= 35
                alien1left[0] = 1700
                alien1left[1] = random.randrange(500, 1450)
                alien1left[2] += 300
            if y_coord < alien1left[1]:
                alien1left[1] -= 2
                if y_coord < alien1left[1] + 200:
                    alien1left[1] -= 4
            if y_coord > alien1left[1]:
                alien1left[1] += 2
                if y_coord > alien1left[1] - 200:
                    alien1left[1] += 4

        # left aliens
        if score >= 1350:
            if alien2left[2] <= 1:
                screen.blit(ship2left, [alien2left[0], alien2left[1]])
                alien2left[0] -= 12
            elif alien2left[2] >= 1:
                alien2left[2] -= 1
                if 5 <= alien2left[2] <= 30 or 45 <= alien2left[2] <= 70 or 85 <= alien2left[2] <= 110:
                    screen.blit(explan, [1580, alien2left[1]])
            if alien2left[0] < -100 or alien2left[3] < 1:
                alien2left[0] = 1700
                alien2left[1] = random.randrange(500, 1450)
                alien2left[2] += 300
                score += 35
                alien2left[3] = 3
            if x_coord - 90 <= alien2left[0] <= x_coord + 90 and y_coord - 90 <= alien2left[1] <= y_coord \
                    + 90:
                health -= 35
                alien2left[0] = 1700
                alien2left[1] = random.randrange(500, 1450)
                alien2left[2] += 300
            if y_coord < alien2left[1]:
                alien2left[1] -= 2
                if y_coord < alien2left[1] + 200:
                    alien2left[1] -= 4
            if y_coord > alien2left[1]:
                alien2left[1] += 2
                if y_coord > alien2left[1] - 200:
                    alien2left[1] += 4



        if score >= 200:
            if alien1_type1[2] <= 1:
                screen.blit(ship3, [alien1_type1[0], alien1_type1[1]])
                alien1_type1[1] += 20
            elif alien1_type1[2] >= 1:
                alien1_type1[2] -= 1
            if alien1_type1[1] > 1800 or alien1_type1[3] < 1:
                alien1_type1[1] = -25
                alien1_type1[0] = random.randrange(50, sizex - 50)
                alien1_type1[2] += 150
                score += 75
                alien1_type1[3] = 3
            if x_coord - 50 <= alien1_type1[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien1_type1[
                1] + 8 <= y_coord + 50:
                health -= 41
                alien1_type1[1] = -25
                alien1_type1[0] = random.randrange(50, sizex - 50)
                alien1_type1[2] += 150
            if x_coord < alien1_type1[0]:
                if alien1_type1[2] <= 1:
                    alien1_type1[0] -= 2
                    if x_coord < alien1_type1[0] + 200:
                        alien1_type1[0] -= 3
                        if x_coord < alien1_type1[0] + 400:
                            alien1_type1[0] -= 2
            if x_coord > alien1_type1[0]:
                if alien1_type1[2] <= 1:
                    alien1_type1[0] += 2
                    if x_coord > alien1_type1[0] - 200:
                        alien1_type1[0] += 3
                        if x_coord > alien1_type1[0] - 400:
                            alien1_type1[0] += 2

        if score >= 1000:
            if alien2_type1[2] <= 1:
                screen.blit(ship3, [alien2_type1[0], alien2_type1[1]])
                alien2_type1[1] += 20
            elif alien2_type1[2] >= 1:
                alien2_type1[2] -= 1
            if alien2_type1[1] > 1800 or alien2_type1[3] < 1:
                alien2_type1[1] = -25
                alien2_type1[0] = random.randrange(50, sizex - 50)
                alien2_type1[2] += 150
                score += 75
                alien2_type1[3] = 3
            if x_coord - 50 <= alien2_type1[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien2_type1[
                1] + 8 <= y_coord + 50:
                health -= 41
                alien2_type1[1] = -25
                alien2_type1[0] = random.randrange(50, sizex - 50)
                alien2_type1[2] += 150
            if x_coord < alien2_type1[0]:
                if alien2_type1[2] <= 1:
                    alien2_type1[0] -= 2
                    if x_coord < alien2_type1[0] + 200:
                        alien2_type1[0] -= 3
                        if x_coord < alien2_type1[0] + 400:
                            alien2_type1[0] -= 2
            if x_coord > alien2_type1[0]:
                if alien2_type1[2] <= 1:
                    alien2_type1[0] += 2
                    if x_coord > alien2_type1[0] - 200:
                        alien2_type1[0] += 3
                        if x_coord > alien2_type1[0] - 400:
                            alien2_type1[0] += 2

        if score >= 2000:
            if alien3_type1[2] <= 1:
                screen.blit(ship3, [alien3_type1[0], alien3_type1[1]])
                alien3_type1[1] += 20
            elif alien3_type1[2] >= 1:
                alien3_type1[2] -= 1
            if alien3_type1[1] > 1800 or alien3_type1[3] < 1:
                alien3_type1[1] = -25
                alien3_type1[0] = random.randrange(50, sizex - 50)
                alien3_type1[2] += 150
                score += 75
                alien3_type1[3] = 3
            if x_coord - 50 <= alien3_type1[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien3_type1[
                1] + 8 <= y_coord + 50:
                health -= 41
                alien3_type1[1] = -25
                alien3_type1[0] = random.randrange(50, sizex - 50)
                alien3_type1[2] += 150
            if x_coord < alien3_type1[0]:
                if alien3_type1[2] <= 1:
                    alien3_type1[0] -= 2
                    if x_coord < alien3_type1[0] + 200:
                        alien3_type1[0] -= 3
                        if x_coord < alien3_type1[0] + 400:
                            alien3_type1[0] -= 2
            if x_coord > alien3_type1[0]:
                if alien3_type1[2] <= 1:
                    alien3_type1[0] += 2
                    if x_coord > alien3_type1[0] - 200:
                        alien3_type1[0] += 3
                        if x_coord > alien3_type1[0] - 400:
                            alien3_type1[0] += 2

        # type 2 aliens
        if score >= 400:
            if alien1_type2[2] <= 1:
                screen.blit(ship5, [alien1_type2[0], alien1_type2[1]])
                if alien1_type2[1] < 800:
                    alien1_type2[1] += 24
                elif alien1_type2[1] < 1200:
                    alien1_type2[1] += 16
                else:
                    alien1_type2[1] += 8
            elif alien1_type2[2] >= 1:
                alien1_type2[2] -= 1
            if alien1_type2[1] > 1800 or alien1_type2[3] < 1:
                alien1_type2[1] = -25
                alien1_type2[0] = random.randrange(50, sizex - 50)
                alien1_type2[2] += 250
                score += 100
                alien1_type2[3] = 3
            if x_coord - 50 <= alien1_type2[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien1_type2[
                1] + 8 <= y_coord + 50:
                health -= 41
                alien1_type2[1] = -25
                alien1_type2[0] = random.randrange(50, sizex - 50)
                alien1_type2[2] += 250
            if x_coord < alien1_type2[0]:
                if alien1_type2[2] <= 1:
                    alien1_type2[0] -= 3
                    if x_coord < alien1_type2[0] + 100 and alien1_type2[1] > 800:
                        alien1_type2[0] -= 7
                        if x_coord < alien1_type2[0] + 250 and alien1_type2[1] > 1000:
                            alien1_type2[0] -= 10
            if x_coord > alien1_type2[0]:
                if alien1_type2[2] <= 1:
                    alien1_type2[0] += 3
                    if x_coord > alien1_type2[0] - 100 and alien1_type2[1] > 800:
                        alien1_type2[0] += 7
                        if x_coord > alien1_type2[0] - 250 and alien1_type2[1] > 1000:
                            alien1_type2[0] += 10

        # type 2 aliens
        if score >= 1500:
            if alien2_type2[2] <= 1:
                screen.blit(ship5, [alien2_type2[0], alien2_type2[1]])
                if alien2_type2[1] < 800:
                    alien2_type2[1] += 24
                elif alien2_type2[1] < 1200:
                    alien2_type2[1] += 16
                else:
                    alien2_type2[1] += 8
            elif alien2_type2[2] >= 1:
                alien2_type2[2] -= 1
            if alien2_type2[1] > 1800 or alien2_type2[3] < 1:
                alien2_type2[1] = -25
                alien2_type2[0] = random.randrange(50, sizex - 50)
                alien2_type2[2] += 250
                score += 100
                alien2_type2[3] = 3
            if x_coord - 50 <= alien2_type2[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien2_type2[1] + 8 <= \
                    y_coord + 50:
                health -= 41
                alien2_type2[1] = -25
                alien2_type2[0] = random.randrange(50, sizex - 50)
                alien2_type2[2] += 250
            if x_coord < alien2_type2[0]:
                if alien2_type2[2] <= 1:
                    alien2_type2[0] -= 3
                    if x_coord < alien2_type2[0] + 100 and alien2_type2[1] > 800:
                        alien2_type2[0] -= 7
                        if x_coord < alien2_type2[0] + 250 and alien2_type2[1] > 1000:
                            alien2_type2[0] -= 10
            if x_coord > alien2_type2[0]:
                if alien2_type2[2] <= 1:
                    alien2_type2[0] += 3
                    if x_coord > alien2_type2[0] - 100 and alien2_type2[1] > 800:
                        alien2_type2[0] += 7
                        if x_coord > alien2_type2[0] - 250 and alien2_type2[1] > 1000:
                            alien2_type2[0] += 10

        # type 2 aliens
        if score >= 3000:
            if alien3_type2[2] <= 1:
                screen.blit(ship5, [alien3_type2[0], alien3_type2[1]])
                if alien3_type2[1] < 800:
                    alien3_type2[1] += 24
                elif alien3_type2[1] < 1200:
                    alien3_type2[1] += 16
                else:
                    alien3_type2[1] += 8
            elif alien3_type2[2] >= 1:
                alien3_type2[2] -= 1
            if alien3_type2[1] > 1800 or alien3_type2[3] < 1:
                alien3_type2[1] = -25
                alien3_type2[0] = random.randrange(50, 1550)
                alien3_type2[2] += 250
                score += 100
                alien3_type2[3] = 3
            if x_coord - 50 <= alien3_type2[0] + 8 <= x_coord + 110 and y_coord - 10 <= alien3_type2[1] \
                    + 8 <= y_coord + 50:
                health -= 41
                alien3_type2[1] = -25
                alien3_type2[0] = random.randrange(50, 1550)
                alien3_type2[2] += 250
            if x_coord < alien3_type2[0]:
                if alien3_type2[2] <= 1:
                    alien3_type2[0] -= 3
                    if x_coord < alien3_type2[0] + 100 and alien3_type2[1] > 800:
                        alien3_type2[0] -= 7
                        if x_coord < alien3_type2[0] + 250 and alien3_type2[1] > 1000:
                            alien3_type2[0] -= 10
            if x_coord > alien3_type2[0]:
                if alien3_type2[2] <= 1:
                    alien3_type2[0] += 3
                    if x_coord > alien3_type2[0] - 100 and alien3_type2[1] > 800:
                        alien3_type2[0] += 7
                        if x_coord > alien3_type2[0] - 250 and alien3_type2[1] > 1000:
                            alien3_type2[0] += 10

        # Powerups
        if gunup[2] <= 1:
            screen.blit(powerup1, [gunup[0], gunup[1]])
            gunup[1] += 10
        elif gunup[2] >= 1:
            gunup[2] -= 1
        if gunup[1] > 1800:
            gunup[1] = -25
            gunup[0] = random.randrange(50, sizex - 50)
            gunup[2] += 150
        if x_coord - 70 <= gunup[0] + 8 <= x_coord + 120 and y_coord - 10 <= gunup[1] + 8 <= y_coord + 50:
            gunmode += 1
            guntimer += 500
            score += 10
            gunup[1] = -25
            gunup[0] = random.randrange(50, sizex - 50)
            gunup[2] += random.randrange(600, 1000)

        if shieldup[2] <= 1:
            screen.blit(powerup2, [shieldup[0], shieldup[1]])
            shieldup[1] += 10
        elif shieldup[2] >= 1:
            shieldup[2] -= 1
        if shieldup[1] > 1800:
            shieldup[1] = -25
            shieldup[0] = random.randrange(50, sizex - 50)
            shieldup[2] += 150
        if x_coord - 70 <= shieldup[0] + 8 <= x_coord + 120 and y_coord - 10 <= shieldup[1] + 8 <= y_coord + 50:
            shields += 50
            score += 10
            shieldup[1] = -25
            shieldup[0] = random.randrange(50, sizex - 50)
            shieldup[2] += random.randrange(600, 1000)

        if lifeup[2] <= 1:
            screen.blit(powerup3, [lifeup[0], lifeup[1]])
            lifeup[1] += 10
        elif lifeup[2] >= 1:
            lifeup[2] -= 1
        if lifeup[1] > 1800:
            lifeup[1] = -25
            lifeup[0] = random.randrange(50, sizex - 50)
            lifeup[2] += 150
        if x_coord - 70 <= lifeup[0] + 8 <= x_coord + 120 and y_coord - 10 <= lifeup[1] + 8 <= y_coord + 50:
            lives += 1
            score += 100
            lifeup[1] = -25
            lifeup[0] = random.randrange(50, sizex - 50)
            lifeup[2] += random.randrange(2000, 4000)
            if lives > 8:
                lives = 8

        # resolve lives and health
        if shields > 0:
            ding = 100 - health
            shields = shields - ding
            health = health + ding
            del ding
        if shields <= 0:
            shields = 0
        if shields > 100:
            shields = 100
        if health < 0 and lives >= 0:
            lives -= 1
            health = 100
        elif health < 0 and lives < 0:
            menu = True
            gameover = True
            forcenewgame = True
        if guntimer < 0:
            gunmode -= 1
            if gunmode > 1:
                guntimer = 150
        if gunmode > 4:
            gunmode = 4

        # Copy image to screen:
        screen.blit(player_image, [x_coord, y_coord])

        #score and stuff
        text1 = Font.render("SCORE :  " + str(score), True, OFFWHITE)
        text2 = font.render("HEALTH : " + str(health) + "/100", True, BLACK)
        text3 = font.render("LIVES :  ", True, OFFWHITE)
        screen.blit(text1, (10, 10))
        #screen.blit(text2, (45, 1505))
        screen.blit(text3, (35, sizey * .96))

        # life bar and lives
        if gunmode == 1:
            firetext = font.render("FIREMODE : NORMAL", True, OFFWHITE)
            screen.blit(firetext, (35, sizey * .85))
        elif gunmode == 2:
            firetext = font.render("FIREMODE : RAPID : " + str(guntimer), True, OFFWHITE)
            screen.blit(firetext, (35, sizey * .85))
        elif gunmode == 3:
            firetext = font.render("FIREMODE : RAPIDx2 : " + str(guntimer), True, OFFWHITE)
            screen.blit(firetext, (35, sizey * .85))
        elif gunmode == 4:
            firetext = font.render("FIREMODE : RAPIDx3 : " + str(guntimer), True, OFFWHITE)
            screen.blit(firetext, (35, sizey * .85))
        if shields > 0:
            pygame.draw.rect(screen, CYAN, pygame.Rect(30, sizey * .89, int(shields) * 8 + 30, 40)), 2
        pygame.draw.rect(screen, RED, pygame.Rect(30, sizey * .89, 830, 50)), 2
        pygame.draw.rect(screen, GREEN, pygame.Rect(30, sizey * .89, int(health) * 8 + 30, 50)), 2
        screen.blit(text2, (45, sizey * .90))
        for i in range(lives):
            pygame.draw.rect(screen, OFFWHITE, pygame.Rect(150 + (i * 115), sizey * .96, 100, 30)), 2

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(30)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()