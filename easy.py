from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

Builder.load_file('data/screens/easy.kv')


class EasyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(EasyFloatLayout, self).__init__(**kwargs)
        self.manager = ScreenManager(transition=SlideTransition(
            duration=.15))
        self.ids.easy.current = 'mode'


    def on_main_screen(self):
        pass
