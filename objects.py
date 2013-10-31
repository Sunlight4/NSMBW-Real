import pygame, Tile,menu
tiledict={"grass":["grasstile.png", 72], "dark":["DarkLand.png", 72],
          "desert":["DesertTile.png", 72], "desertBlock":["DesertBlock.png", 72],
          "ghostBlock":["GhostBlock.png", 72], "snow":["SnowBlock.png", 72],
          "volcano":["VolcanoBlock.png", 72], "cave":["UndergroundTile.png", 72],
          "airshipHole":["AirshipCannonHole.png", 24],
          "airshipBarrel":["AirshipBarrel.png", [50, 72]]}

class Room(object):
    objs=[]
    tiles=[]
    music="Overworld.mp3"
    bg=pygame.image.load("bg/Grass_BG.png")
    def add_tile(self, tilename, pos):
        img, size=tiledict[tilename] 
        img="images/"+img
        pos=[int(x//size+0.5)*size for x in pos]
        self.tiles.append([Tile.Tile(tilename, img, size), pos])
    
    def render_tiles(self, screen):
        for tile, pos in self.tiles:
            tile.render(screen, pos)
    def object_menu(self, screen):
        x=[i(0,0) for i in objs_dict.values()]
        x.insert(0, screen)
        kind=objs_dict[menu.imagemenu(*x)]
        return kind
    def add_object(self, x, y, kind):
        sprite=kind(x, y)
        self.objs.append(sprite)
    def new_bg(self, screen):
        self.bg=pygame.image.load("bg/"+menu.imagemenu(screen, Preview("Grass_BG.png"),
                                                       Preview("Desert_BG.png"), Preview("Boss_BG.png"),
                                                       Preview("Ghost_BG.png"), Preview("Snow_BG.png"),
                                                       Preview("Volcano_BG.png"), Preview("Cave_BG.png"),
                                                       Preview("Mountain_BG.png")))
class GameObject(pygame.sprite.Sprite):
    single=False
    name="none"
    def __init__(self, x, y, img):
        x=int(x//24+0.5)*24
        y=int(y//24+0.5)*24
        self.image=pygame.image.load("images/"+img)
        self.rect=self.image.get_rect(top=y, left=x)
        
class Preview(pygame.sprite.Sprite):
    def __init__(self, img):
        self.image=pygame.image.load("preview/"+img)
        self.name=img
previews=[]
class Goomba(GameObject):
    name="goomba"
    def __init__(self, x, y):
        super(Goomba, self).__init__(x, y, "Goomba.png")
        
class Broozer(GameObject):
    name="broozer"
    def __init__(self, x, y):
        super(Broozer, self).__init__(x, y, "Broozer_Sprite.png")
class KoopaRed(GameObject):
    name="koopaRed"
    def __init__(self, x, y):
        super(KoopaRed, self).__init__(x, y, "Koopa_red.png")
class KoopaGreen(GameObject):
    name="koopaGreen"
    def __init__(self, x, y):
        super(KoopaGreen, self).__init__(x, y, "Koopa.png")
class SmallMario(GameObject):
    name="smallMario"
    single=True
    def __init__(self, x, y):
        super(SmallMario, self).__init__(x, y, "Small_Mario.png")
class Bowser(GameObject):
    name="bowserBoss"
    single=True
    def __init__(self, x, y):
        super(Bowser, self).__init__(x, y, "Bowser_Sprite_NSMBW.png")
class LarryKoopa(GameObject):
    name="larryKoopa"
    single=True
    def __init__(self, x, y):
        super(LarryKoopa, self).__init__(x, y, "LarryKoopa.png")
class Boo(GameObject):
    name="boo"
    def __init__(self, x, y):
        super(Boo, self).__init__(x, y, "Glow_boo_sprite.png")
class Thwomp(GameObject):
    name="thwomp"
    def __init__(self, x, y):
        super(Thwomp, self).__init__(x, y, "60px-Thwomp.png")
class LemmyKoopa(GameObject):
    name="lemmyKoopa"
    single=True
    def __init__(self, x, y):
        super(LemmyKoopa, self).__init__(x, y, "LemmyKoopa.png")
objs_dict={"goomba":Goomba, "koopaRed":KoopaRed, "koopaGreen":KoopaGreen,
           "broozer":Broozer, "lemmyKoopa":LemmyKoopa,
           "larryKoopa":LarryKoopa, "boo":Boo, "thwomp":Thwomp}

