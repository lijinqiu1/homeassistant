from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
import kivy

Builder.load_file('data/screens/main.kv')

kivy.resources.resource_add_path("data/font")


class MainFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MainFloatLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self._update_clock, 1 / 60.)

    def _update_clock(self,dt):
        self.ids.main_atmosphere_Label.text = 'bad'
        self.ids.main_WaterQuality_Label.text = 'bad'
        self.ids.main_temperature_Label.text = '25' + "C"
        self.ids.main_Hum_Label.text = 'bad'

    def on_easy_screen(self, *l):
        pass

