# Initialize 
import pygame,player,ball,endzone,colourbrick,score,lives
pygame.init()
pygame.mixer.init()
pygame.key.set_repeat(17,17)  
# Display 
screen = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption("move a box") 
  
# Entities 
background = pygame.Surface(screen.get_size()) 
background = pygame.image.load('backimage.jpg')
background = background.convert()  
screen.blit(background, (0, 0)) 

#Set sound effect for when ball hits the brick
hit_brick = pygame.mixer.Sound('hit_brick.ogg')
hit_brick.set_volume(1)
#Set sound effect for when ball hits the paddle
hit_paddle = pygame.mixer.Sound('hit_paddle.ogg')
hit_paddle.set_volume(1)
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(1) 
pygame.mixer.music.play(-1)
gameover_img = pygame.image.load('gameover.png')
gameover_img = gameover_img.convert_alpha()
# sprites 
player1=player.Player(screen,1)
player2=player.Player(screen,2)
ball=ball.Ball(screen)
endzone=endzone.EndZone(screen)
life=lives.Lives()
score_keeper=score.ScoreKeeper()
playerGroup=pygame.sprite.Group(player1,player2)
# Create the bricks
#list of colors (blue, green, orange, yellow, red, and violet)

bricklist=[]
bricklist1=[]
bricklist2=[]
bricklist3=[]
bricklist4=[]
bricklist5=[]

x_value=0
x_value1=0
x_value2=0
x_value3=0
x_value4=0
x_value5=0

for brick in range(18):
    
    bricklist.append(colourbrick.Brick(screen,x_value))
    x_value=x_value+36
    
    bricklist1.append(colourbrick.Brick1(screen,x_value1))
    x_value1=x_value1+36
    
    bricklist2.append(colourbrick.Brick2(screen,x_value2))
    x_value2=x_value2+36
    
    bricklist3.append(colourbrick.Brick3(screen,x_value3))
    x_value3=x_value3+36
    
    bricklist4.append(colourbrick.Brick4(screen,x_value4))
    x_value4=x_value4+36
    
    bricklist5.append(colourbrick.Brick5(screen,x_value5))
    x_value5=x_value5+36
    

brickGroup = pygame.sprite.Group(bricklist)
brickGroup1 = pygame.sprite.Group(bricklist1)   
brickGroup2 = pygame.sprite.Group(bricklist2)    
brickGroup3 = pygame.sprite.Group(bricklist3)
brickGroup4 = pygame.sprite.Group(bricklist4)
brickGroup5 = pygame.sprite.Group(bricklist5)

    
allSprites = pygame.sprite.Group(score_keeper,life,player1,player2,ball,endzone,\
bricklist,bricklist1,bricklist2,bricklist3,bricklist4,bricklist5)

  
# ACTION 
  
    # Assign  
clock = pygame.time.Clock() 
keepGoing = True
# Hide the mouse pointer
pygame.mouse.set_visible(False) 
    
    # Loop 
while keepGoing: 
  
    # Time 
    clock.tick(30) 
  
    # Events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.change_direction(-10) 
            if event.key == pygame.K_RIGHT: 
                player1.change_direction(10) 
    player2.change_direction(pygame.mouse.get_pos())
    
    x=pygame.sprite.spritecollide(ball,brickGroup, False)
    if pygame.sprite.spritecollide(ball,brickGroup, True):
        score_keeper.scored(len(x))
        hit_brick.play()
        ball.change_direction()
        
    x=pygame.sprite.spritecollide(ball,brickGroup1, False)
    if pygame.sprite.spritecollide(ball,brickGroup1, True):
        score_keeper.scored((len(x))*2)
        hit_brick.play()
        ball.change_direction()
    
    x=pygame.sprite.spritecollide(ball,brickGroup2, False)
    if pygame.sprite.spritecollide(ball,brickGroup2, True):
        score_keeper.scored((len(x))*3)
        hit_brick.play()
        ball.change_direction()
        
    x=pygame.sprite.spritecollide(ball,brickGroup3, False)
    if pygame.sprite.spritecollide(ball,brickGroup3, True):
        score_keeper.scored((len(x))*4)
        hit_brick.play()
        ball.change_direction()
    
    x=pygame.sprite.spritecollide(ball,brickGroup4, False)
    if pygame.sprite.spritecollide(ball,brickGroup4, True):
        score_keeper.scored((len(x))*5)
        hit_brick.play()
        ball.change_direction()
        
    x=pygame.sprite.spritecollide(ball,brickGroup5, False)   
    if pygame.sprite.spritecollide(ball,brickGroup5, True):
        score_keeper.scored((len(x))*6)
        hit_brick.play()
        ball.change_direction()
    
    if pygame.sprite.spritecollide(ball,playerGroup,False):
            hit_paddle.play()
            ball.change_direction()
    
    if ball.rect.colliderect(endzone.rect):
            ball.reset()
            life.lose_life()
    
    if score_keeper.get_score==378 or life.loser():
            keepGoing=False
    # Refresh screen 
    allSprites.clear(screen, background) 
    allSprites.update() 
    allSprites.draw(screen)        
    pygame.display.flip() 
#Unhide the mouse pointer
pygame.mouse.set_visible(True)
#Blit gameover on screen
screen.blit(gameover_img, (100, 100))
pygame.display.flip()
pygame.mixer.music.fadeout(4500)
pygame.time.delay(4500)
# Close the game window 
pygame.quit()
  
      
