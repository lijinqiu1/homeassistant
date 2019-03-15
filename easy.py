from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

Builder.load_file('data/screens/easy.kv')


class EasyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(EasyFloatLayout, self).__init__(**kwargs)
        self.ids.easy.current = 'mode'
        self.screen_index = 0
        self.mode_index = 0

    def on_main_screen(self):
        pass

    def go_previous_screen(self):
        self.ids.easy.transition.direction = 'left'
        if self.screen_index == 0:
            self.ids.easy.current = 'cover'
            self.screen_index = 1
        else:
            self.ids.easy.current = 'mode'
            self.screen_index = 0

    def go_next_screen(self):
        self.ids.easy.transition.direction = 'right'
        if self.screen_index == 0:
            self.ids.easy.current = 'cover'
            self.screen_index = 1
        else:
            self.ids.easy.current = 'mode'
            self.screen_index = 0
