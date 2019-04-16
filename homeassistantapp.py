# -*-coding:utf-8-*-
import platform
if platform.machine() == 'armv6l':
    import os
    os.environ['KIVY_GL_BACKEND'] = 'gl'
    os.environ['KIVY_BCM_DISPMANX_ID'] = '2'
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.clock import Clock

from main import MainFloatLayout
from easy import EasyFloatLayout
from profession import ProfessionFloatLayout
from setting import SettingFloatLayout
from RsetAPI import RsetAPI
import gevent
import gevent.monkey
gevent.monkey.patch_socket()
Config.write()

kivy.resources.resource_add_path("data/font")
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')


class Homeassistant(App):
    def __init__(self, **kwargs):
        super(Homeassistant, self).__init__(**kwargs)
        self.api = RsetAPI()
        self.men_xi = 'men_xi'
        self.door_state = 'close'
        Clock.schedule_interval(self._update_clock, 1.)
        Clock.schedule_interval(self._update_state, 1.)

    def build(self):
        self.main = MainFloatLayout()
        main_screen = Screen(name='main')
        main_screen.add_widget(self.main)
        self.root.ids.sm.add_widget(main_screen)

        self.easy = EasyFloatLayout()
        easy_screen = Screen(name='easy')
        easy_screen.add_widget(self.easy)
        self.root.ids.sm.add_widget(easy_screen)

        self.profession = ProfessionFloatLayout()
        profession_screen = Screen(name='profession')
        profession_screen.add_widget(self.profession)
        self.root.ids.sm.add_widget(profession_screen)

        setting = SettingFloatLayout()
        setting_screen = Screen(name='setting')
        setting_screen.add_widget(setting)
        self.root.ids.sm.add_widget(setting_screen)

        self.root.ids.sm.current = 'main'

        self.men_xi_state = 'on'

    def on_easy_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        self.root.ids.sm.current = 'easy'

    def on_profession_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        # self.root.ids.sm.transition.duration = 1.
        self.root.ids.sm.current = 'profession'

    def on_main_screen(self):
        self.root.ids.sm.transition.direction = 'right'
        # self.root.ids.sm.transition.duration = 1.
        self.root.ids.sm.current = 'main'

    def on_setting_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        # self.root.ids.sm.transition.duration = 1.
        self.root.ids.sm.current = 'setting'

    def on_door_control(self):
        if self.door_state == 'close':
            self.root.ids.door_control.background_normal = "data/icons/door/opening.jpg"
            self.root.ids.door_control.background_down = "data/icons/door/opening.jpg"
            self.api.set_switch_off(self.men_xi)
            self.door_state = 'opening'
        elif self.door_state == 'opened':
            self.api.set_switch_on(self.men_xi)
            self.door_state = 'close'

    def _update_state(self, dt):
        gevent.joinall([
            gevent.spawn(self.update_state())
        ])

    def _update_clock(self, dt):
        if self.men_xi_state == 'on':
            if self.door_state == 'opened':
                self.door_state = 'close'
                self.root.ids.door_control.background_normal = "data/icons/door/open.jpg"
                self.root.ids.door_control.background_down = "data/icons/door/open.jpg"
        elif self.men_xi_state == 'off':
            self.door_state = 'opened'
            self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
            self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"

    def update_state(self):
        self.men_xi_state = self.api.get_switch_state(self.men_xi)
        temp = self.api.get_temp()
        temp = int(float(str(temp)))
        self.main.set_temp(temp)
        self.easy.set_temp(temp)



if __name__ == '__main__':
    Homeassistant().run()

