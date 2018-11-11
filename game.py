import pygame,sys
def give_cell():
    lista=[pygame.Surface((25,25))]
    lista.append(lista[0].get_rect())
    return lista
pygame.init()
WINDOW=pygame.display.set_mode((600,700),0,32)
pygame.display.set_caption("TETRIS")
CLOCK=pygame.time.Clock()
c=give_cell()
c[0].fill((255,0,0))
c[1].x=30
c[1].y=25
a_pressed=0
d_pressed=0
pressed=0
skip=0
pygame.draw.rect(c[0],(150,150,150),(0,0,25,25),5)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_a and a_pressed==0):
                if(c[1].x>30):
                    c[1].x-=25
                a_pressed=1
            if(event.key==pygame.K_d and d_pressed==0):
                if(c[1].x<350):
                    c[1].x+=25
                d_pressed=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                a_pressed=0
            if event.key==pygame.K_d:
                d_pressed=0
        pressed=1
    if d_pressed and pressed==0:
        if(c[1].x<350):
            c[1].x+=25
            d_pressed=1
    if a_pressed and pressed==0:
        if(c[1].x>30):
            c[1].x-=25
            a_pressed=1
    WINDOW.fill((0,0,0))
    pygame.draw.line(WINDOW,(255,255,255),(24,20),(24,680),10)
    pygame.draw.line(WINDOW,(255,255,255),(385,20),(385,680),10)
    pygame.draw.line(WINDOW,(255,255,255),(20,20),(390,20),10)
    pygame.draw.line(WINDOW,(255,255,255),(20,680),(390,680),10)
    if(c[1].y<645 and skip==5):
        c[1].y+=25
        skip=0
    WINDOW.blit(*c)
    pygame.display.update()
    pressed=0
    skip+=1
    CLOCK.tick_busy_loop(10)
