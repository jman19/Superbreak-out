import pygame

class Lives(pygame.sprite.Sprite):
    '''This class defines a lives sprite to display the # of lives.'''
    def __init__(self):
        '''This initializer loads the lives image, sets up the rect and
        starting value of 3 for lives'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the lives
        self.image=pygame.image.load('lives.png')
        self.image = self.image.convert_alpha()
         
        # Set the rect attributes for the lives
        self.rect = self.image.get_rect()
        self.rect.left= 20
        self.rect.top=10
        
        #Set the number of lives
        self.__lives=3
        
    def lose_life(self):
        '''crops out a heart and subtract a life everytime the ball 
        hits the endzone'''
        self.image=pygame.transform.chop(self.image,(0,20,28,20))
        self.__lives-=1
        
    def loser(self):
        '''returns 1 if there are no lives left or else returns a 0'''
        if self.__lives<=0:
            return 1
        else:
            return 0