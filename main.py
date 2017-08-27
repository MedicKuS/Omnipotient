from pygame import *
import sys

'''класс инициализации меню'''
class Menu:
    '''функция получения списка меню'''
    def __init__(self, items = [200, 200, 'item', (120,120,120), (255,0,0), 0]):
        self.items = items
    '''функия инициализации меню с отображением активной кнопки'''
    def render(self, layout, font, act_item):
        for i in self.items:
            if act_item == i[5]:
                layout.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                layout.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    '''функция цикла сцены, которая вызывает меню'''
    def menu(self):
        menu_font = font.Font('9921.otf', 50) # шрифт
        done = True
        item = 0
        while done:
            logo = image.load('image/menu/mainWindow.png')  # Фон меню
            mp = mouse.get_pos() #задание позиции мыши и изменения цвета кнопки
            for i in self.items:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    item = i[5]
            self.render(logo, menu_font, item)
            '''события при нажатиии кнопок или мыши'''
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
                    if ev.key == K_SPACE:
                        if item == 0:
                            done = False
                        elif item == 1:
                            sys.exit()
                if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                    if item == 0:
                        done = False
                    elif item == 1:
                        sys.exit()
            scene.blit(logo, (0, 0))
            display.flip()
# первая сцена(демо)
class Level1:
    def __init__(self, text = [0 , 0, 'text', (0, 0, 0), 0]):
        self.text = text
    def level1(self):
        dialog_font = font.Font('9921.otf', 24) # шрифт
        init = True
        boll = True
        n = 0
        while init:
            logo = image.load('image/intro/intro.png')
            dialog_hero = image.load('image/intro/dialog_ghero.png')
            dialog_phone = image.load('image/intro/dialog_phone.png')
            if boll == True:
                i = self.text[n]
                dialog_phone.blit(dialog_font.render(i[2], 1, i[3]), (i[0], i[1]))
                logo.blit(dialog_phone, (0, 500))
                scene.blit(logo, (0, 0))
                display.flip()
            else:
                i = self.text[n]
                dialog_hero.blit(dialog_font.render(i[2], 1, i[3]), (i[0], i[1]))
                logo.blit(dialog_hero, (0, 500))
                scene.blit(logo, (0, 0))
                display.flip()
            for ev in event.get():
                if ev.type == QUIT:
                    init = False
                if ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        sys.exit()
                    if ev.key == K_SPACE:
                        if boll == True:
                            boll = False
                            if n < 12:
                                n = n + 1
                            else:
                                gameMenu.menu()
                        else:
                            boll = True
                            if n < 12:
                                n = n + 1
                            else:
                                gameMenu.menu()

'''главный блок программы'''
scene = display.set_mode((1000, 673)) # Создание пустого рабочего окна
logo = image.load('image/logo.ico')
display.set_icon(logo) #Логотип (иконка) игры
display.set_caption('Omnipotient') # Название игры
font.init() # иницализация шрифтов

''' список кнопок в меню (x, y, name, color_def, act_color, num) '''
items = [
    (750, 270, 'Game', (120,120,120), (255,0,0), 0),
    (760, 320, 'Quit', (120,120,120), (255,0,0), 1)
]
'''инициализация меню'''
gameMenu = Menu(items)
gameMenu.menu()

'''инициализация 1 уровня (демо) *1 диалог'''
text = [
    (300, 7, 'звонок', (5, 5, 5), 0),
    (300, 7, 'Да?', (5, 5, 5), 1),
    (300, 7, 'Это я, у меня есть поручение для тебя.', (5, 5, 5), 2),
    (300, 7, 'Я уже ожидаю худшего.', (5, 5, 5), 3),
    (300, 7, 'Да потерпи ты. Наш уговор в силе, и тебе осталось совсем чуть-чуть. Нужно совершить сделку в отеле Монтана, с директором.', (5, 5, 5), 4),
    (300, 7, 'Надеюсь, я сам буду?', (5, 5, 5), 5),
    (300, 7, 'Нет, с тобой будет мой человек. Его нужно многому учить, но стреляет он неплохо.', (5, 5, 5), 6),
    (300, 7, 'Блять...', (5, 5, 5), 7),
    (300, 7, '...Наш клиент последнее время очень'
             ' не доволен нашими условиями и, по слухам, плохо о нас высказывается.', (5, 5, 5), 8),
    (300, 7, 'Если на вас будет покушение - убейте его и взорвите отель.', (5, 5, 5), 9),
    (300, 7, 'Блять...', (5, 5, 5), 10),
    (300, 7, 'Не ной. Задание простое.'
             ' На месте напарник тебя уже будет ждать. Он знает, как ты выглядишь. Удачи.', (5, 5, 5), 11),
    (300, 7, '...', (5, 5, 5), 12)
]
gameLevel1 = Level1(text)
gameLevel1.level1()

font.quit()