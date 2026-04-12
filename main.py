import pygame
import sys


pygame.init()
pygame.font.init()

width,height=800,500


font = pygame.font.SysFont('Arial', 32)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

class Level:
    def __init__(self,amount_w,amount_h):
        self.amount_w = amount_w
        self.amount_h = amount_h
    
    # rysowanie planszy,
    # jeżeli kwadrawty nie wyhodzą kwadratowe- rysuje biały margines po lewej i prawej
    def draw_map(self):
        size_h = height/self.amount_h
        size_w = width/self.amount_w
        zmiana = 1
        margin_width = 0

        if size_h != size_w: 
            if size_h < size_w:
                difference_in_size = size_w - size_h
                size_w = (width/self.amount_w) - difference_in_size
            else:
                difference_in_size = size_h - size_w
                size_h = (height/self.amount_h) - difference_in_size

            margin_width = (difference_in_size * self.amount_w) /2
            pygame.draw.rect(screen,(255,255,255),(0, 0, margin_width, (height -(size_h * self.amount_h))//2))

        for y in range(self.amount_h):
            for x in range(self.amount_w):
                if zmiana % 2 == 1:
                    pygame.draw.rect(screen,(0,255,127),((size_w * x) + margin_width, (size_h * y) ,size_w, size_h)) #jasny kwadrat
                    zmiana += 1
                else:
                    pygame.draw.rect(screen,(60,179,113),((size_w * x) + margin_width, (size_h * y), size_w, size_h)) #ciemny kwadrat
                    zmiana -= 1
            zmiana += 1

Level1= Level(10,10)



while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("klik")
                

    screen.fill((128,128,128))
    
    Level1.draw_map()




    pygame.display.flip()
