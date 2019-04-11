#coding=utf-8

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.clock import Clock
from RsetAPI import RsetAPI
Builder.load_file('data/screens/setting.kv')


class SettingFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(SettingFloatLayout, self).__init__(**kwargs)
