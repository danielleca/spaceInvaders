import pygame, sys
pygame.init()
vel=5
maxbullet=3
bulletvel=7
WIDTH,HEIGHT=900,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders")
screen.fill("lightpink")
space=pygame.image.load("outerspace.png")
space1=pygame.transform.scale(space,(WIDTH,HEIGHT))
border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
healthfont=pygame.font.SysFont('comicsans',40)
winnerfont=pygame.font.SysFont('comicsans',100)
sw,sh=55,40
redp=pygame.image.load("spaceshipRed.png")
yellowp=pygame.image.load("spaceshipYellow.png")
redr=pygame.transform.rotate(pygame.transform.scale(redp,(sw,sh)),90)
yellowr=pygame.transform.rotate(pygame.transform.scale(yellowp,(sw,sh)),270)

pygame.display.update()
def draw(yellowhealth,redhealth,red,yellow,redbullets,yellowbullets):
    screen.blit(space1,(0,0))
    pygame.draw.rect(screen,"black",border)
    yellowh=healthfont.render("HEALTH:"+str(yellowhealth),True,"yellow")
    redh=healthfont.render("HEALTH:"+str(redhealth),True,"red")
    screen.blit(yellowh,(WIDTH-yellowh.get_width(),10))
    screen.blit(redh,(0,10))
    screen.blit(redr,(red.x,red.y))
    screen.blit(yellowr,(yellow.x,yellow.y))
    for bullet in redbullets:
        pygame.draw.rect(screen,"red",bullet)
    for bullet in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullet)
    pygame.display.update()
def redmovement(keys_pressed,red):
    if keys_pressed[pygame.K_UP] and red.y>0:
        red.y-=vel
    if keys_pressed[pygame.K_DOWN] and red.y+red.height<HEIGHT:
        red.y+=vel
    if keys_pressed[pygame.K_LEFT] and red.x>0:
        red.x-=vel
    if keys_pressed[pygame.K_RIGHT] and red.x+red.width<border.x:
        red.x+=vel

def yellowmovement(keys_pressed,yellow):
    if keys_pressed[pygame.K_w] and yellow.y>0:
        yellow.y-=vel
    if keys_pressed[pygame.K_s] and yellow.y+yellow.height<HEIGHT:
        yellow.y+=vel
    if keys_pressed[pygame.K_a] and yellow.x>border.x+border.width:
        yellow.x-=vel
    if keys_pressed[pygame.K_d] and yellow.x+yellow.width<WIDTH:
        yellow.x+=vel
def movebullets(redbullets,yellow,yellowbullets):
    for bullet in redbullets:
        bullet.x+=bulletvel
        if yellow.colliderect(bullet):
            yellowbullets.remove(yellow)
        elif bullet.x>WIDTH:
            yellowbullets.remove(yellow)
    for bullet in yellowbullets:
        bullet.x+=bulletvel
        if red.colliderect(bullet):
            redbullets.remove(red)
        elif bullet.x<WIDTH:
            redbullets.remove(red)
def main():
    redhealth=10
    yellowhealth=10
    red=pygame.Rect(100,300,sw,sh)
    yellow=pygame.Rect(800,300,sw,sh)
    redbullets=[]
    yellowbullets=[]
    while True:
        keys_pressed=pygame.key.get_pressed()
        redmovement(keys_pressed,red)
        yellowmovement(keys_pressed,yellow)
        movebullets(redbullets,yellow,yellowbullets)
        draw(yellowhealth,redhealth,red,yellow,redbullets,yellowbullets)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LSHIFT and len(redbullets)<maxbullet:
                    bullet=pygame.Rect(red.x+red.width,red.y+red.height/2,10,5)
                    redbullets.append(bullet)
                if event.key==pygame.K_RSHIFT and len(yellowbullets)<maxbullet:
                    bullet=pygame.Rect(yellow.x,yellow.y+yellow.height/2,10,5)
                    yellowbullets.append(bullet)
if __name__=="__main__":
    main()
