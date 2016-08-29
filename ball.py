import pygame
pygame.init()
class Ball(pygame.sprite.Sprite): 
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen): 
        '''This initializer takes a screen surface as a parameter,
        initializes the image and rect attributes, and x,y direction of the       
        ball.'''
        # Call the parent __init__() method 
        pygame.sprite.Sprite.__init__(self) 
  
        # Set the image and rect attributes for the Ball 
        self.image = pygame.image.load('ball.png')
        self.image= self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
  
        # Instance variables to keep track of the screen surface 
        # and set the initial x and y vector for the ball. 
        self.__screen = screen
        self.__dx = 6
        self.__dy = -6
    
    def reset(self):
        '''This method resets the ball's position to the center'''
        self.rect.center = (self.__screen.get_width()/2,self.__screen.get_height()/2)
 
    def change_direction(self):
        '''This method causes the y direction of the ball to reverse.'''
        self.__dy = -self.__dy         
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the ball in the same x direction.
        if ((self.rect.left > 0) and (self.__dx < 0)) or\
           ((self.rect.right < self.__screen.get_width()) and (self.__dx > 0)):
            self.rect.left += self.__dx
        # If yes, then reverse the x direction. 
        else:
            self.__dx = -self.__dx
             
        # Check if we have reached the top or bottom of the court.
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
            self.rect.top -= self.__dy
        # If yes, then reverse the y direction. 
        else:
            self.__dy = -self.__dy
