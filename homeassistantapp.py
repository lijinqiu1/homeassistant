# -*-coding:utf-8-*-
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.config import Config

from main import MainFloatLayout
from easy import EasyFloatLayout
from profession import ProfessionFloatLayout

Config.write()

kivy.resources.resource_add_path("data/font")
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')


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

        profession = ProfessionFloatLayout()
        profession_screen = Screen(name='profession')
        profession_screen.add_widget(profession)
        self.root.ids.sm.add_widget(profession_screen)

        self.root.ids.sm.current = 'main'

    def on_easy_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        self.root.ids.sm.current = 'easy'

    def on_profession_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        self.root.ids.sm.current = 'profession'

    def on_main_screen(self):
        self.root.ids.sm.transition.direction = 'right'
        self.root.ids.sm.current = 'main'

    def on_door_control(self):
        self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
        self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"


if __name__ == '__main__':
    Homeassistant().run()

