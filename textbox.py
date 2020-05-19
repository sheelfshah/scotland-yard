import pygame

validChars = "1234567890qwertyuiopasdfghjklzxcvbnm, "
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

class TextBox(pygame.sprite.Sprite):
  def __init__(self,fontSize, max_length=11):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.max_length=max_length
    self.fontSize=fontSize
    self.font = pygame.font.SysFont("comicsans", fontSize)
    self.image = self.font.render("", 1, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center=(1200,20)

  def add_chr(self, char, shiftDown):
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    if len(self.text)>self.max_length:
        self.text=self.text[:self.max_length]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos

def display_textBox(textBox, screen):
    blankSurface=pygame.Surface((textBox.max_length*12, textBox.fontSize*1.7))
    blankSurface.fill((128,128,128))
    blankRect=blankSurface.get_rect()
    screen.blit(blankSurface, (textBox.rect.center[0]-round(blankRect.width/2),textBox.rect.center[1]-round(blankRect.height/2)))
    screen.blit(textBox.image, textBox.rect)

def get_input_textBox(textBox, screen):
    running = True
    shiftDown=False
    while running:
      display_textBox(textBox, screen)
      pygame.display.flip()
      for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = False
        if e.type == pygame.KEYDOWN:
            textBox.add_chr(pygame.key.name(e.key), shiftDown)
            if e.key == pygame.K_SPACE:
                textBox.text += " "
                textBox.update()
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = True
            if e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN:
                if len(textBox.text) > 0:
                    print (textBox.text)
                    running = False
    return textBox.text