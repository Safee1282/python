import pygame 

#initialise required modules
pygame.init()
#set up window geometry
screen = pygame.display.set_mode((400,500))
# Create a loop to run till the games isquit by the user

done=False

while not done:

    #clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()

    pygame.display.flip()        
    