# -*-coding:utf-8-*-
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.config import Config

from main import MainFloatLayout
from easy import EasyFloatLayout

Config.write()

kivy.resources.resource_add_path("data/font")
# Config.set('graphics', 'width', '800')
# Config.set('graphics', 'height', '600')


class Homeassistant(App):

    def build(self):

        main = MainFloatLayout()
        main_screen = Screen(name='main')
        main_screen.add_widget(main)
        self.root.ids.sm.add_widget(main_screen)

        easy = EasyFloatLayout()
        easy_screen = Screen(name='easy')
        easy_screen.add_widget(easy)
        self.root.ids.sm.add_widget(easy_screen)

        self.root.ids.sm.current = 'main'

        self.bind(on_easy_screen=main.on_easy_screen)
        self.bind(on_main_screen=easy.on_main_screen)

    def on_easy_screen(self):
        self.root.ids.sm.current = 'easy'

    def on_main_screen(self):
        self.root.ids.sm.current = 'main'

    def on_door_control(self):
        self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
        self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"


if __name__ == '__main__':
    Homeassistant().run()

