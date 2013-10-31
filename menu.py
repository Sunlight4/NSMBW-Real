import pygame
pygame.font.init()
def imagemenu(screen, *sprites):
    run=1
    poslist=[]
    x=0
    y=0
    screen.fill([255, 255, 255])
    for sprite in sprites:
        screen.blit(sprite.image, [x, y])

        poslist.append([sprite, [x, y]])

        x+=72
        if x >= 640:
            y+=72
            x-=640
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y=pygame.mouse.get_pos()
                for pos in poslist:
                    x2, y2=pos[1]
                    if x2//72==x//72 and y2//72==y//72: 
                        return pos[0].name
def textmenu(screen, msg):
    textfont=pygame.font.Font(None, 18)
    typing=pygame.font.Font(None, 12)
    typed=""
    while True:
        screen.fill([255,255,255])
        text1=textfont.render(msg, False, [0,0,0])
        screen.blit(text1, [100,100])
        if typed:
            text2=textfont.render(typed, False, [0,0,0])
            screen.blit(text2, [100,200])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:return typed
                elif event.key==pygame.K_UP:typed=typed.title()
                try:
                    key=chr(event.key)
                    typed+=key
                except:pass


        
    

                    
                
        
        
        
        
