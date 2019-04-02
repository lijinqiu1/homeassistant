# -*-coding:utf-8-*-
import kivy
kivy.resources.resource_add_path('data/font/')
font = kivy.resources.resource_find('simhei.ttf')
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from RsetAPI import RsetAPI
Builder.load_file('data/screens/main.kv')

kivy.resources.resource_add_path("data/font")


class MainFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MainFloatLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self._update_clock, 30)
        self.api = RsetAPI()

    def _update_clock(self,dt):
        temp = self.api.get_temp()
        if temp:
            self.ids.Label.text = '[color=#6E6E6E]'+temp+'[/color]'

    def on_easy_screen(self, *l):
        pass

