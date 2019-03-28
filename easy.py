from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from RsetAPI import RsetAPI

Builder.load_file('data/screens/easy.kv')


class EasyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(EasyFloatLayout, self).__init__(**kwargs)
        self.api = RsetAPI()
        self.ids.sm_easy.current = 'screen_mode'
        self.screen_index = 0
        self.current_mode = 'day'
        self.current_cover = 'open'

        self.ids.button_mode_day.background_normal = 'data/icons/easy/day_h.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day_h.jpg'

        self.ids.button_cover_open.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/selected.jpg'

    def on_main_screen(self):
        pass

    def go_previous_screen(self):
        self.ids.sm_easy.transition.direction = 'right'
        if self.screen_index == 0:
            self.ids.sm_easy.current = 'screen_cover'
            self.screen_index = 1
        else:
            self.ids.sm_easy.current = 'screen_mode'
            self.screen_index = 0

    def go_next_screen(self):
        self.ids.sm_easy.transition.direction = 'left'
        if self.screen_index == 0:
            self.ids.sm_easy.current = 'screen_cover'
            self.screen_index = 1
        else:
            self.ids.sm_easy.current = 'screen_mode'
            self.screen_index = 0

    def on_mode_day_selected(self):
        self.current_mode = 'day'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day_h.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day_h.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic.jpg'

    def on_mode_night_selected(self):
        self.current_mode = 'night'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night_h.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night_h.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic.jpg'

    def on_mode_sleep_selected(self):
        self.current_mode = 'sleep'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep_h.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep_h.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic.jpg'

    def on_mode_romantic_selected(self):
        self.current_mode = 'romantic'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic_h.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic_h.jpg'

    def on_cover_open_selected(self):
        self.current_cover = 'open'
        self.ids.button_cover_open.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/selected.jpg'

        self.ids.button_cover_half.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_half.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_close.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_close.background_down = 'data/icons/easy/select.jpg'

        self.api.set_cover_open('left_cover')
        self.api.set_cover_open('right_cover')
        self.api.set_cover_open('bashroom_cover')

    def on_cover_half_selected(self):
        self.current_cover = 'half'
        self.ids.button_cover_open.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_half.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_half.background_down = 'data/icons/easy/selected.jpg'

        self.ids.button_cover_close.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_close.background_down = 'data/icons/easy/select.jpg'

        self.api.set_cover_position('left_cover', 50)
        self.api.set_cover_position('right_cover', 50)
        self.api.set_cover_position('bashroom_cover', 50)

    def on_cover_close_selected(self):
        self.current_cover = 'close'
        self.ids.button_cover_open.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_half.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_half.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_close.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_close.background_down = 'data/icons/easy/selected.jpg'

        self.api.set_cover_close('left_cover')
        self.api.set_cover_close('right_cover')
        self.api.set_cover_close('bashroom_cover')

