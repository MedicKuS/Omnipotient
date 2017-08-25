from pygame import *
import sys

class Menu:
    def __init__(self, items = [200, 200, 'item', (120,120,120), (255,0,0), 0]):
        self.items = items
    def render(self, layout, font, act_item):
        for i in self.items:
            if act_item == i[5]:
                layout.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                layout.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True
        menu_font = font.Font('9921.otf', 50)
        item = 0
        while done:
            logo = image.load('image/menu/mainWindow.png')  # Фон меню
            mp = mouse.get_pos()
            for i in self.items:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    item = i[5]
            self.render(logo, menu_font, item)
            for ev in event.get():
                if ev.type == QUIT:
                    sys.exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        sys.exit()
                    if ev.key == K_UP:
                        if item > 0:
                            item = item - 1
                    if ev.key == K_DOWN:
                        if item < len(self.items) - 1:
                            item = item + 1
                if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                    if item == 0:
                        done = False
                    elif item == 1:
                        sys.exit()
            scene.blit(logo, (0, 0))
            display.flip()

# Загрузка картинок
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)

    def render(self):
        scene.blit(self.bitmap, (self.x, self.y))

scene = display.set_mode((1000, 673)) # Создание пустого рабочего окна
logo = image.load('image/logo.ico')
display.set_icon(logo)
display.set_caption('Omnipotient') # Название игры
font.init()
items = [
    (750, 270, 'Game', (120,120,120), (255,0,0), 0),
    (760, 320, 'Quit', (120,120,120), (255,0,0), 1)
]
gameMenu = Menu(items)
gameMenu.menu()
# Бесконечный цикл для корректной работы программы (чтобы не закрывалось окно)
process = True
while process:
    for i in event.get():
        if i.type == QUIT:
            process = False
            square_run = True

    display.flip()
    font.quit()