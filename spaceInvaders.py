import pygame, sys
pygame.init()
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
def draw(yellowhealth,redhealth,red,yellow):
    screen.blit(space1,(0,0))
    pygame.draw.rect(screen,"black",border)
    yellowh=healthfont.render("HEALTH:"+str(yellowhealth),True,"yellow")
    redh=healthfont.render("HEALTH:"+str(redhealth),True,"red")
    screen.blit(yellowh,(WIDTH-yellowh.get_width(),10))
    screen.blit(redh,(0,10))
    screen.blit(redr,(red.x,red.y))
    screen.blit(yellowr,(yellow.x,yellow.y))
    pygame.display.update()
def main():
    redhealth=10
    yellowhealth=10
    red=pygame.Rect(100,300,sw,sh)
    yellow=pygame.Rect(800,300,sw,sh)

    while True:
        draw(yellowhealth,redhealth,red,yellow)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
if __name__=="__main__":
    main()