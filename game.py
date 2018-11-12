import pygame,sys
def give_cell():
    lista=[pygame.Surface((25,25))]
    lista.append(lista[0].get_rect())
    lista[0].fill((255,0,0))
    lista[1].x=30
    lista[1].y=25
    pygame.draw.rect(lista[0],(150,150,150),(0,0,25,25),5)
    return lista
def colide(CELLS,BLOCK):
    print()
class CELLS(object):
    def __init__(self):
        self.cells=[[0 for x in range(14)] for y in range(25)]
        self.rects=[[0 for x in range(14)] for y in range(25)]
        self.ids=[]
    def add(self,Surface,Rect):
        print(self.cells)
        print((Rect.y-50)//25,(Rect.x-30)//25)
        self.cells[(Rect.y-50)//25][(Rect.x-30)//25]=1
        self.rects[(Rect.y-50)//25][(Rect.x-30)//25]=[Surface,Rect]
        self.ids.append([(Rect.y-50)//25,(Rect.x-30)//25])
    def print(self):
        for i in range(14):
            for j in range(25):
                print(self.cells[i][j],end="")
            print("\n",end="")
    def blit(self,WINDOW):
        for i in self.ids: 
            WINDOW.blit(*self.rects[i[0]][i[1]])
    def is_one(self,i,j):
        if(self.cells[i][j]):
            return True
        else:
            return False
pygame.init()
WINDOW=pygame.display.set_mode((600,700),0,32)
pygame.display.set_caption("TETRIS")
CLOCK=pygame.time.Clock()
c=give_cell()
komory=CELLS()
a_pressed=0
d_pressed=0
s_pressed=0
pressed=0
l=0
skip=0
#14/25
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_a and a_pressed==0):
                if(c[1].x>30) and  not komory.is_one((c[1].y-50)//25,(c[1].x-30-25)//25):
                    c[1].x-=25
                a_pressed=1
            if(event.key==pygame.K_d and d_pressed==0):
                if(c[1].x<350) and  not komory.is_one((c[1].y-50)//25,(c[1].x-30+25)//25):
                    c[1].x+=25
                d_pressed=1
            if event.key==pygame.K_s and s_pressed==0:
                if  c[1].y<650 and  not komory.is_one((c[1].y-50+25)//25,(c[1].x-30)//25):
                    c[1].y+=25
                s_pressed=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                a_pressed=0
            if event.key==pygame.K_d:
                d_pressed=0
            if event.key==pygame.K_s:
                s_pressed=0
        pressed=1
    if d_pressed and pressed==0:
        if(c[1].x<350) and  not komory.is_one((c[1].y-50)//25,(c[1].x-30+25)//25):
            c[1].x+=25
            d_pressed=1
    if a_pressed and pressed==0 :
        if(c[1].x>30) and  not komory.is_one((c[1].y-50)//25,(c[1].x-30-25)//25):
            c[1].x-=25
            a_pressed=1
    if s_pressed and pressed==0:
        if(c[1].y<650) and  not komory.is_one((c[1].y-50+25)//25,(c[1].x-30)//25):
            c[1].y+=25
            s_pressed=1
    if skip==5:
        if c[1].y<645 and  not komory.is_one((c[1].y-50+25)//25,(c[1].x-30)//25): 
            l+=1
            c[1].y+=25
            #print(c[1].y,c[1].x)
            skip=0
        else:
            komory.add(*c)
            c=give_cell()
            c[1].y=25
            c[1].x=30
            skip=0
    pressed=0
    skip+=1
    WINDOW.fill((0,0,0))
    pygame.draw.line(WINDOW,(255,255,255),(24,20),(24,680),10)
    pygame.draw.line(WINDOW,(255,255,255),(385,20),(385,680),10)
    pygame.draw.line(WINDOW,(255,255,255),(20,20),(390,20),10)
    pygame.draw.line(WINDOW,(255,255,255),(20,680),(390,680),10)
    WINDOW.blit(*c)
    komory.blit(WINDOW)
    pygame.display.update()
    CLOCK.tick_busy_loop(10)
