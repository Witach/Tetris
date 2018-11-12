import pygame,sys
def give_cell():
    lista=[pygame.Surface((25,25))]
    lista.append(lista[0].get_rect())
    lista[0].fill((255,0,0))
    lista[1].x=30
    lista[1].y=25
    pygame.draw.rect(lista[0],(150,150,150),(0,0,25,25),5)
    return lista
class CONTROL(object):
    def __init__(self):
        self.c=give_cell()
        self.a_pressed=0
        self.d_pressed=0
        self.s_pressed=0
        self.pressed=0
        self.skip=0
    def k_down(self,key,komory):
        if(key==pygame.K_a and self.a_pressed==0):
                self.move_left(komory)
                self.a_pressed=1
        if(key==pygame.K_d and self.d_pressed==0):
                self.move_right(komory)
                self.d_pressed=1
        if key==pygame.K_s and self.s_pressed==0:
                self.move_down(komory)
                self.s_pressed=1
        self.pressed=1
    def k_up(self,key):
        if key==pygame.K_a:
                self.a_pressed=0
        if key==pygame.K_d:
                self.d_pressed=0
        if key==pygame.K_s:
                self.s_pressed=0
        self.pressed=1
    def cycle(self,komory):
        if self.d_pressed and self.pressed==0:
            self.move_right(komory)
        if self.a_pressed and self.pressed==0:
            self.move_left(komory)
        if self.s_pressed and self.pressed==0:
            self.move_down(komory)
    def move_down(self,komory):
         if(self.c[1].y<650) and  not komory.is_one((self.c[1].y-50+25)//25,(self.c[1].x-30)//25):
                self.c[1].y+=25
         else:
                komory.add(*(self.c))
                self.c=give_cell()
                self.c[1].y=25
                self.c[1].x=30
                self.skip=0
                is_line=komory.is_line()
                self.s_pressed=0
                while is_line!=-1:
                     komory.delete_line(is_line)
                     is_line=komory.is_line()
    def move_left(self,komory):
        if(self.c[1].x>30) and  not komory.is_one((self.c[1].y-50)//25,(self.c[1].x-30-25)//25):
                self.c[1].x-=25
    def move_right(self,komory):
        if(self.c[1].x<350) and  not komory.is_one((self.c[1].y-50)//25,(self.c[1].x-30+25)//25):
                self.c[1].x+=25
class CELLS(object):
    def __init__(self):
        self.cells=[[0 for x in range(14)] for y in range(25)]
        self.rects=[[0 for x in range(14)] for y in range(25)]
    def add(self,Surface,Rect):
        print(self.cells)
        print((Rect.y-50)//25,(Rect.x-30)//25)
        self.cells[(Rect.y-50)//25][(Rect.x-30)//25]=1
        self.rects[(Rect.y-50)//25][(Rect.x-30)//25]=[Surface,Rect]
    def print(self):
        for i in range(14):
            for j in range(25):
                print(self.cells[i][j],end="")
            print("\n",end="")
    def blit(self,WINDOW):
        for i in self.rects:
            for j in i:
                if type(j)==type(list()):
                    WINDOW.blit(*j)
    def is_one(self,i,j):
        if(self.cells[i][j]):
            return True
        else:
            return False
    def delete_line(self,y):
        for i in range(1,y+1,-1):
            for j in range(len(self.cells[i])):
                self.cells[i][j]=self.cells[i-1][j]
                self.rects[i][j][1].y+=25
                self.rects=[i][j]=self.rects[i-1][j]
        for i in range(len(self.cells[0])):
            self.cells[0][i]=0
            self.rects[0][i]=0
    def is_line(self):
        for i in range(len(self.cells)-1,-1,-1):
            print(i)
            if sum(self.cells[i])==len(self.cells[i]):
                return i
        return -1
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
keys=CONTROL()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            keys.k_down(event.key,komory)
        if event.type==pygame.KEYUP:
            keys.k_up(event.key)
    keys.cycle(komory)
    if keys.skip==5:
        keys.move_down(komory)
        keys.skip=0
    keys.pressed=0
    keys.skip+=1
    WINDOW.fill((0,0,0))
    pygame.draw.line(WINDOW,(255,255,255),(24,20),(24,680),10)
    pygame.draw.line(WINDOW,(255,255,255),(385,20),(385,680),10)
    pygame.draw.line(WINDOW,(255,255,255),(20,20),(390,20),10)
    pygame.draw.line(WINDOW,(255,255,255),(20,680),(390,680),10)
    WINDOW.blit(*(keys.c))
    komory.blit(WINDOW)
    pygame.display.update()
    CLOCK.tick_busy_loop(10)
