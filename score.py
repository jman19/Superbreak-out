import pygame
pygame.init()
class ScoreKeeper(pygame.sprite.Sprite): 
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the custom font "vermin_vibes.ttf", and
        sets the starting score to 0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.Font("vermin_vibes.ttf", 40)
        self.__score = 0
         
    def scored(self,value):
        '''This method takes a value as a parameter and adds to the score'''
        self.__score += value
     
    def get_score(self):
        '''Returns the score'''
        return self.__score
 
    def update(self):
        '''This method will be called automatically to display
        the current score at the top of the game window.'''
        message = "Score: %d" %\
                (self.__score)
        self.image = self.__font.render(message, 1, (193,205,193))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 30)