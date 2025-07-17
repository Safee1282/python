import pygame 
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

while not done:
     for event in pygame.event.get():
         if event.type==pygame.QUIT:
             done = True
pygame.draw.rect(screen,(0 , 125, 255), pygame.rect(30,30,60,60))    

pygame.display.flip() 
   

# import pygame
# pygame.init()
# window= pygame.display.set_mode((400,400))
# window.fill(("black"))
# green=(0,255,0)
# pygame.draw.circle(window,green,(300,300),50)
# pygame.draw.circle(window,green,(100,100),50,3)
# pygame.display.update()
# running=True
# while running:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running = False
# pygame.quit()            


