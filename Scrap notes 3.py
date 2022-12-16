class Button():
    def __init__(self,setting,text):
        self.width,self.height = 400,100

        self.button_color=(0,100,100,128)
        self.text_color=(255,0,0,128)
        self.text = pygame.font.Font(None,100).render(text,True,self.text_color, self.button_color)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

        self.btnsurf = pygame.Surface(self.rect.size,pygame.SRCALPHA)
        self.btnsurf.fill(self.button_color)
        self.btnsurf.blit(self.text, self.text_rect, special_flags=pygame.BLEND_MAX)

        self.rect.center = setting.screen_rect.center

    def draw_button(self,setting):
        setting.screen.blit(self.btnsurf,self.rect)
        