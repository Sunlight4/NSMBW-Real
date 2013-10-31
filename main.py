import pygame, menu, objects, os, Tile, sys
pygame.init()
mixer = pygame.mixer
mixer.init()
music=mixer.music
screen=pygame.display.set_mode([640, 480])
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
fill=screen.fill
titlescreen=load("images/titlescreen.png")
run=1
pygame.display.set_icon(load("icon.png"))
pygame.display.set_caption("NSMBW Level Creator")
q=0
blit(titlescreen, [0,0])
music.load("music/Title.mp3")
music.set_volume(1)
music.play(-1)
while run:
    flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0
            q=1
        elif event.type==pygame.KEYDOWN and event.key==ord("x"):
            run=0

if q:pygame.quit();sys.exit()
run=1
q=0
current_room=objects.Room()
kind=None
tile=None
lastmusic=None
while run:
    fill([0,0,0])
    blit(current_room.bg, [0,0])
    if lastmusic!=current_room.music:
        music.fadeout(100)
        music.load("music/"+current_room.music)
        music.play(-1)
        lastmusic=current_room.music
    for i in current_room.objs:
        blit(i.image, [i.rect.left, i.rect.top])
    current_room.render_tiles(screen)
    flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            q=1
            run=0
        elif event.type==pygame.KEYDOWN:
            if event.key==ord(" "):
                kind=current_room.object_menu(screen)
            elif event.key==ord("p"):
                run=0
            elif event.key==ord("q"):
                run=0
                q=1
            elif event.key==ord("b"):
                kind=objects.Bowser
            elif event.key==ord("m"):
                kind=objects.SmallMario
            elif event.key==ord("n"):
                current_room.new_bg(screen)
            elif event.key==ord("g"):
                current_room.music=menu.textmenu(screen, "Enter music filename:")
            elif event.key==pygame.K_DELETE:
                del current_room.objs[-1]
            elif event.key==pygame.K_w:
                selected=current_room.objs.pop()
                selected.rect.top-=5
                current_room.objs.append(selected)
            elif event.key==ord("t"):
                kind=None
                tile=menu.imagemenu(screen, Tile.Tile("grass", "images/grasstile.png", 72), Tile.Tile("dark", "images/DarkLand.png", 72),
                                    Tile.Tile("desert", "images/DesertTile.png", 72), Tile.Tile("desertBlock", "images/DesertBlock.png", 72),
                                    Tile.Tile("ghostBlock", "images/GhostBlock.png", 72), Tile.Tile("snow", "images/SnowBlock.png", 72),
                                    Tile.Tile("volcano", "images/VolcanoBlock.png", 72), Tile.Tile("cave", "images/UndergroundTile.png", 72),
                                    Tile.Tile("airshipHole", "images/AirshipCannonHole.png", 24),
                                    Tile.Tile("airshipBarrel", "images/AirshipBarrel.png", 50))
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if kind!=None:
                x, y=pygame.mouse.get_pos()
                current_room.add_object(x, y, kind)
                if kind.single:kind=None
            elif tile!=None:
                x, y=pygame.mouse.get_pos()
                current_room.add_tile(tile, [x, y])

if q:pygame.quit();sys.exit()

        
            
    
    

    
