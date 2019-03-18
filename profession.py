from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.properties import StringProperty
Builder.load_file('data/screens/profession.kv')


class ProfessionFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(ProfessionFloatLayout, self).__init__(**kwargs)
        self.profession_current_screen = 'environment'
        self.profession_air_switch = 0
        self.profession_floor_heating_switch = 0

        # self.floor_heating_level_1_button = Button(size_hint=(0.0575, 0.092), pos_hint={"x": 0.29625, 'y': 0.274},
        #                                            id='floor_heating_level_1_button',
        #                                            background_normal="data/icons/profession/floor_heating/switch.jpg",
        #                                            background_down="data/icons/profession/floor_heating/switch.jpg",
        #                                            on_press=self.on_floor_heating_level_1_selected)

        self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"

        self.ids.sm_profession.current = 'environment_air'

    def on_environment_selected(self):
        self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
        self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        self.profession_current_screen = 'environment'

    def on_lights_selected(self):
        self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
        self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
        self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        self.profession_current_screen = 'lights'

    def on_atmosphere_selected(self):
        self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
        self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
        self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        self.profession_current_screen = 'atmosphere'

    def on_cover_button_selected(self):
        self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
        self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
        self.profession_current_screen = 'cover'

    def go_next_screen(self):
        # if self.profession_current_screen == 'environment':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        #     self.profession_current_screen = 'lights'
        # elif self.profession_current_screen == 'lights':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        #     self.profession_current_screen = 'atmosphere'
        # elif self.profession_current_screen == 'atmosphere':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
        #     self.profession_current_screen = 'cover'
        # elif self.profession_current_screen == 'cover':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        #     self.profession_current_screen = 'environment'
        self.ids.sm_profession.transition.direction = 'left'
        if self.ids.sm_profession.current == 'environment_air':
            self.ids.sm_profession.current = 'environment_floor_heating'

    def go_previous_screen(self):
        # if self.profession_current_screen == 'environment':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
        #     self.profession_current_screen = 'cover'
        # elif self.profession_current_screen == 'lights':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        #     self.profession_current_screen = 'environment'
        # elif self.profession_current_screen == 'atmosphere':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        #     self.profession_current_screen = 'lights'
        # elif self.profession_current_screen == 'cover':
        #     self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
        #     self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
        #     self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
        #     self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
        #     self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
        #     self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
        #     self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
        #     self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
        #     self.profession_current_screen = 'atmosphere'
        self.ids.sm_profession.transition.direction = 'right'
        if self.ids.sm_profession.current == 'environment_floor_heating':
            self.ids.sm_profession.current = 'environment_air'

    def on_air_switch_selected(self):
        if self.profession_air_switch == 0:
            self.ids.air_FloatLayout.canvas.before.clear()
            with self.ids.air_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
                          source='data/icons/profession/air/background_on.jpg')
            self.ids.air_switch_button.background_normal = "data/icons/profession/air/on.jpg"
            self.ids.air_switch_button.background_down = "data/icons/profession/air/on.jpg"
            self.profession_air_switch = 1
        else:
            self.ids.air_FloatLayout.canvas.before.clear()
            with self.ids.air_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
                          source='data/icons/profession/air/background_off.jpg')
            self.ids.air_switch_button.background_normal = "data/icons/profession/air/off.jpg"
            self.ids.air_switch_button.background_down = "data/icons/profession/air/off.jpg"
            self.profession_air_switch = 0

    def on_floor_heating_switch_selected(self):
        if self.profession_floor_heating_switch == 0:
            self.ids.floor_heating_switch_button.background_normal = "data/icons/profession/floor_heating/on.jpg"
            self.ids.floor_heating_switch_button.background_down = "data/icons/profession/floor_heating/on.jpg"
            self.ids.floor_heating_FloatLayout.canvas.before.clear()
            with self.ids.floor_heating_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
                          source='data/icons/profession/floor_heating/background_on.jpg')
            self.profession_floor_heating_switch = 1
            self.ids.floor_heating_level_1_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_1_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
        else:
            self.ids.floor_heating_switch_button.background_normal = "data/icons/profession/floor_heating/off.jpg"
            self.ids.floor_heating_switch_button.background_down = "data/icons/profession/floor_heating/off.jpg"
            self.ids.floor_heating_FloatLayout.canvas.before.clear()
            with self.ids.floor_heating_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
                          source='data/icons/profession/floor_heating/background_off.jpg')
            self.profession_floor_heating_switch = 0
            self.ids.floor_heating_level_1_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_1_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_2_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_2_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_3_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_3_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_4_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_5_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_5_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"

    def on_floor_heating_level_selected(self,*args):
        if self.profession_floor_heating_switch == 1:
            self.profession_floor_heating_switch = 1
            self.ids.floor_heating_level_1_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_1_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            if args[0] == '1':
                self.ids.floor_heating_level_1_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_1_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '2':
                self.ids.floor_heating_level_2_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_2_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '3':
                self.ids.floor_heating_level_3_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_3_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '4':
                self.ids.floor_heating_level_4_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_4_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '5':
                self.ids.floor_heating_level_5_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_5_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"





