import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from aspirador import Aspirador_de_po

# INTERFACE = Builder.load_file("tela.kv")
aspirador_de_cache = Aspirador_de_po

class Botao(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (255, 1, 1 ,1)

    def printar_batata(self):
        print('batata')


class interface(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 10
        self.cols = 3


    def click(self):
        self.ids["apps_e_peso"].text = f'{aspirador_de_cache.analisador_de_cache(self)}'
    

class MeuAplicativo(App):

    # def build(self):
    #     return INTERFACE

    pass

aplicativo = MeuAplicativo()
aplicativo.run()
