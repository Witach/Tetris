import pygame,sys
import random
def give_cell(x=0,y=0):
    lista=[pygame.Surface((25,25))]
    lista.append(lista[0].get_rect())
    lista[0].fill((255,0,0))
    lista[1].x=30+x
    lista[1].y=25+y
    pygame.draw.rect(lista[0],(150,150,150),(0,0,25,25),5)
    return lista
class block(object):
    def __init__(self):
        self.cells=[]
        self.x=8*25
        self.y=0
        self.wich=int(random.random()*8)
        self.blocks=[[[0,0],[0,25],[25,25],[25,0]],[[0,0],[25,0],[50,0],[50,-25]],[[0,0],[25,0],[25,25],[50,25]],[[0,0],[25,0],[25,25],[50,0]],[[0,0],[25,0],[25,-25],[50,-25]], [[0,0],[25,0],[50,0],[50,25]],[[0,0],[25,0],[50,0],[75,0]],[[0,0]]]
        for i in self.blocks[self.wich]:
            self.cells.append(give_cell(self.x+i[0]+25,self.y+i[1]))
    def move_down(self):
        for i in self.cells:
            i[1].y+=25
    def move_left(self):
        for i in self.cells:
            i[1].x-=25
    def move_right(self):
        for i in self.cells:
            i[1].x+=25
    #def rotate(self)
        #???
class CONTROL(object):
    def __init__(self):
        self.c=block()
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
         if komory.can_move("down",self.c.cells):
                self.c.move_down()
         else:
                for i in self.c.cells:
                    komory.add(*i)
                self.c=block()
                self.skip=0
                is_line=komory.is_line()
                self.s_pressed=0
                while is_line!=-1:
                     komory.delete_line(is_line)
                     is_line=komory.is_line()
    def move_left(self,komory):
        if komory.can_move("left",self.c.cells):
                self.c.move_left()
    def move_right(self,komory):
        if komory.can_move("right",self.c.cells):
                self.c.move_right()
    def blit(self,surface):
        for i in self.c.cells:
            surface.blit(*i)
        
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
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
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
        print("elo")
        for i in range(y,0,-1):
            print(i)
            for j in range(len(self.cells[i])):                
                self.cells[i][j]=self.cells[i-1][j]
                if self.rects[i][j]!=0:
                    self.rects[i][j][1].y+=25
                self.rects[i][j]=self.rects[i-1][j]
        for i in range(len(self.cells[0])):
            self.cells[0][i]=0
            self.rects[0][i]=0
    def is_line(self):
        for i in range(len(self.cells)-1,-1,-1):
            if sum(self.cells[i])==len(self.cells[i]):
                #print(i)
                return i
        return -1
    def can_move(self,kierunek,bloki):
        if kierunek=="left":
            for i in bloki:
                if not ((i[1].x>30) and  not komory.is_one((i[1].y-50)//25,(i[1].x-30-25)//25)):
                    return False
        if kierunek=="right":
            for i in bloki:
                if not ((i[1].x<350) and  not komory.is_one((i[1].y-50)//25,(i[1].x-30+25)//25)):
                    return False
        if kierunek=="down":
            for i in bloki:
                if not ((i[1].y<650) and  not komory.is_one((i[1].y-50+25)//25,(i[1].x-30)//25)):
                    return False
        return True
pygame.init()
WINDOW=pygame.display.set_mode((600,700),0,32)
pygame.display.set_caption("TETRIS")
CLOCK=pygame.time.Clock()
komory=CELLS()
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
    keys.blit(WINDOW)
    komory.blit(WINDOW)
    pygame.display.update()
    CLOCK.tick_busy_loop(10)
