import pygame
pygame.init()
class Brick(pygame.sprite.Sprite):
    '''This class defines our brick sprite'''
    def __init__(self,screen,x_value):
        '''This initializer takes brick x, brick y, width and color as parameters.
        It then sets up the surface for bricks, fills it and sets up the rect'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        
        self.image = pygame.Surface((screen.get_width()/18, 20))
        self.image=self.image.convert()
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.left = x_value
        self.rect.top = screen.get_height()/3

class Brick1(pygame.sprite.Sprite):
    '''This class defines our brick sprite'''
    def __init__(self,screen,x_value):
        '''This initializer takes brick x, brick y, width and color as parameters.
        It then sets up the surface for bricks, fills it and sets up the rect'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        
        self.image = pygame.Surface((screen.get_width()/18, 20))
        self.image=self.image.convert()
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.left = x_value
        self.rect.top = (screen.get_height()/3)-20
        
class Brick2(pygame.sprite.Sprite):
    '''This class defines our brick sprite'''
    def __init__(self,screen,x_value):
        '''This initializer takes brick x, brick y, width and color as parameters.
        It then sets up the surface for bricks, fills it and sets up the rect'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        
        self.image = pygame.Surface((screen.get_width()/18, 20))
        self.image=self.image.convert()
        self.image.fill((255,140,0))
        self.rect = self.image.get_rect()
        self.rect.left = x_value
        self.rect.top = (screen.get_height()/3)-40
        
class Brick3(pygame.sprite.Sprite):
    '''This class defines our brick sprite'''
    def __init__(self,screen,x_value):
        '''This initializer takes brick x, brick y, width and color as parameters.
        It then sets up the surface for bricks, fills it and sets up the rect'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        
        self.image = pygame.Surface((screen.get_width()/18, 20))
        self.image=self.image.convert()
        self.image.fill((255,215,0))
        self.rect = self.image.get_rect()
        self.rect.left = x_value
        self.rect.top = (screen.get_height()/3)-60
        
class Brick4(pygame.sprite.Sprite):
    '''This class defines our brick sprite'''
    def __init__(self,screen,x_value):
        '''This initializer takes brick x, brick y, width and color as parameters.
        It then sets up the surface for bricks, fills it and sets up the rect'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        
        self.image = pygame.Surface((screen.get_width()/18, 20))
        self.image=self.image.convert()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.left = x_value
        self.rect.top = (screen.get_height()/3)-80

class Brick5(pygame.sprite.Sprite):
    '''This class defines our brick sprite'''
    def __init__(self,screen,x_value):
        '''This initializer takes brick x, brick y, width and color as parameters.
        It then sets up the surface for bricks, fills it and sets up the rect'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        
        self.image = pygame.Surface((screen.get_width()/18, 20))
        self.image=self.image.convert()
        self.image.fill((127,0,255))
        self.rect = self.image.get_rect()
        self.rect.left = x_value
        self.rect.top = (screen.get_height()/3)-100