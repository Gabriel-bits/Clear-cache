import kivy
from kivy import utils
from kivy.app import App
from kivy.core import window
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from aspirador import Aspirador_de_po

# INTERFACE = Builder.load_file("MeuAplicativo.kv")
aspirador_de_cache = Aspirador_de_po
# window.WindowBase.size = (1920,1080)

Window.size = (4*73.5, 4*149)

class Fatias(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Botao(ButtonBehavior, Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print(utils.get_color_from_hex("#40004D"))

        # self.color = (255, 1, 1 )
        # c = (0.87,0.14,0.82)
        # self.size = ("100dp", "10dp")
        # self.size_hint_x = '100dp'
        # self.size_hint_max_x = 150
        # print(utils.get_color_from_hex("#0D002C"))

class interface(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Label.color = (0.87,0.14,0.82)
        self.padding = 10
        self.rows = 3
        self.size_files = str(aspirador_de_cache.analisador_de_cache(self))

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.050980392156862744, 0.0, 0.17254901960784313, 1)
            Rectangle(pos=self.pos, size=self.size)

    def click(self):
        if type(self.ids["apps_e_peso"].text) == str:
            number = self.ids["apps_e_peso"].text
            number = int(number)
            number += 1
            self.ids["apps_e_peso"].text = str(number)


        # f'{aspirador_de_cache.analisador_de_cache(self)}'


class MeuAplicativo(App):

    # def build(self):
    #     return INTERFACE

    pass


aplicativo = MeuAplicativo()
aplicativo.run()
