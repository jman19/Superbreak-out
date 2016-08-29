
import pygame
pygame.init()
class EndZone(pygame.sprite.Sprite): 
    '''This class defines the sprite for our left and right end zones'''
    def __init__(self, screen): 
        '''This initializer takes a screen surface, and x position  as 
        parameters.  For the left (player 1) endzone, x_position will = 0, 
        and for the right (player 2) endzone, x_position will = 639.'''
        # Call the parent __init__() method 
        pygame.sprite.Sprite.__init__(self) 
          
        # Our endzone sprite will be a 1 pixel wide black line. 
        self.image = pygame.Surface((640,1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
        # Set the rect attributes for the endzone 
        self.rect = self.image.get_rect()
        self.rect.left=0
        self.rect.bottom=screen.get_height()