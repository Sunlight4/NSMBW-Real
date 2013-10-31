import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,name,img,size):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.img = pygame.image.load(img)
        self.image=self.img
        self.size = size
    def info(self):
        return [self.name,self.img,self.size]
    def render(self,surf,pos):
        self.surf = surf
        self.pos = pos

        self.surf.blit(self.img,self.pos)
