import pygame
pygame.init()
class Player(pygame.sprite.Sprite): 
    '''This class defines the sprite for Player 1 and Player 2'''
    def __init__(self, screen,player_num): 
        '''This initializer takes a screen surface, and player number as 
        parameters.  Depending on the player number it loads the appropriate 
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method 
        pygame.sprite.Sprite.__init__(self) 
          
        # Define the image attributes for a black rectangle. 
        self.image = pygame.Surface((100, 10)) 
        self.image = self.image.convert() 
        self.image.fill((0, 0, 0)) 
        self.rect = self.image.get_rect() 
  
        self.__player_num=player_num
        
        # If we are initializing a sprite for player 1,
        # position it 50 pixels from the bottom of the screen
        if player_num == 1:
            self.rect.bottom = screen.get_height()-50
        #Otherwise, position it 20 pixels from the bottom of the screen.
        else:
            self.rect.bottom = screen.get_height()-20
 
        # Center the player horizontally in the window.
        self.rect.left = screen.get_width()/2
    
    def change_direction(self, displacement):
        if self.__player_num==2:
            self.rect.left = displacement[0]
        else:
            if self.rect.left==0:
                if displacement>0:
                    self.rect.left += displacement
            elif self.rect.left==550:
                if displacement<0:
                    self.rect.left += displacement
            else:
                self.rect.left += displacement 
          
    