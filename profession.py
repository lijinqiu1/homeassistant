#coding=utf-8

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.clock import Clock
from RsetAPI import RsetAPI
Builder.load_file('data/screens/profession.kv')


class ProfessionFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(ProfessionFloatLayout, self).__init__(**kwargs)
        self.api = RsetAPI()
        self.profession_current_type = 1
        self.profession_event = 'None'
        self.profession_air_switch = 0
        self.profession_floor_heating_switch = 0
        self.profession_climate_switch = 0
        self.profession_climate_mode = 'None'
        self.profession_climate_temp = 25
        self.profession_atmosphere_color = {'color_1': [255, 255, 255],
                                            'color_2': [255, 217, 154],
                                            'color_3': [255, 155, 213],
                                            'color_4': [153, 226, 255],
                                            'color_5': [154, 254, 209]}
        self.profession_atmosphere_get_color = {'color_1': [255, 255, 255],
                                                'color_2': [255, 214, 153],
                                                'color_3': [255, 153, 209],
                                                'color_4': [153, 224, 255],
                                                'color_5': [153, 255, 204]}
        self.profession_atmosphere_brightness = {'level_1': 50,
                                                 'level_2': 100,
                                                 'level_3': 150,
                                                 'level_4': 200,
                                                 'level_5': 230}
        self.profession_lights_bedroom = {'switch': 'None', 'level': 1}
        self.profession_lights_livingroom = {'switch': 'None', 'level': 1}
        self.profession_lights_vestibule = {'switch': 'None', 'level': 1}
        self.profession_lights_bashroom = {'switch': 'None', 'level': 1}

        self.profession_atmosphere_bedroom = {'switch': 'off', 'color': 'None', 'level': 'None'}
        self.profession_atmosphere_livingroom = {'switch': 'off', 'color': 'None', 'level': 'None'}
        self.profession_atmosphere_vestibule = {'switch': 'off', 'color': 'None', 'level': 'None'}
        self.profession_atmosphere_bashroom = {'switch': 'off', 'color': 'None', 'level': 'None'}

        self.profession_cover_left = {'action': 0, 'postion': 1}
        self.profession_cover_right = {'action': 0, 'postion': 1}
        self.profession_cover_bashroom = {'action': 0, 'postion': 1}

        self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"

        self.ids.sm_profession.current = 'environment_air'

        Clock.schedule_interval(self._update_clock, 1/2.)
        self.api = RsetAPI()

    def update_climate_screen(self, mode, temp):
        if mode == 'False':
            if self.profession_climate_switch == 1:
                self.profession_climate_switch = 0
                self.ids.climate_switch_button.background_normal = "data/icons/profession/climate/off.jpg"
                self.ids.climate_switch_button.background_down = "data/icons/profession/climate/off.jpg"
                self.ids.climate_FloatLayout.canvas.before.clear()
                with self.ids.climate_FloatLayout.canvas.before:
                    Rectangle(size=(self.width * 0.7, self.height * 0.70263), pos=(self.width * 0.15, self.height * 0.0421),
                              source='data/icons/profession/climate/background_off.jpg')
                self.ids.climate_heat_button.background_normal = \
                    "data/icons/profession/climate/switch_disable.jpg"
                self.ids.climate_heat_button.background_down = \
                    "data/icons/profession/climate/switch_disable.jpg"
                self.ids.climate_cool_button.background_normal = \
                    "data/icons/profession/climate/switch_disable.jpg"
                self.ids.climate_cool_button.background_down = \
                    "data/icons/profession/climate/switch_disable.jpg"
                self.ids.climate_dry_button.background_normal = \
                    "data/icons/profession/climate/switch_disable.jpg"
                self.ids.climate_dry_button.background_down = \
                    "data/icons/profession/climate/switch_disable.jpg"
                self.ids.climate_up_button.background_normal = \
                    "data/icons/profession/climate/up_disable.jpg"
                self.ids.climate_up_button.background_down = \
                    "data/icons/profession/climate/up_disable.jpg"
                self.ids.climate_down_button.background_normal = \
                    "data/icons/profession/climate/down_disable.jpg"
                self.ids.climate_down_button.background_down = \
                    "data/icons/profession/climate/down_disable.jpg"
        else:
            if self.profession_climate_switch == 0:
                self.profession_climate_switch = 1
                self.ids.climate_switch_button.background_normal = "data/icons/profession/climate/on.jpg"
                self.ids.climate_switch_button.background_down = "data/icons/profession/climate/on.jpg"
                self.ids.climate_FloatLayout.canvas.before.clear()
                with self.ids.climate_FloatLayout.canvas.before:
                    Rectangle(size=(self.width * 0.7, self.height * 0.70263), pos=(self.width * 0.15, self.height * 0.0421),
                              source='data/icons/profession/climate/background_on1.jpg')
                self.ids.climate_up_button.background_normal = \
                    "data/icons/profession/climate/up.jpg"
                self.ids.climate_up_button.background_down = \
                    "data/icons/profession/climate/up.jpg"
                self.ids.climate_down_button.background_normal = \
                    "data/icons/profession/climate/down.jpg"
                self.ids.climate_down_button.background_down = \
                    "data/icons/profession/climate/down.jpg"

            if mode != self.profession_climate_mode:
                self.ids.climate_heat_button.background_normal = \
                    "data/icons/profession/climate/select.jpg"
                self.ids.climate_heat_button.background_down = \
                    "data/icons/profession/climate/select.jpg"
                self.ids.climate_cool_button.background_normal = \
                    "data/icons/profession/climate/select.jpg"
                self.ids.climate_cool_button.background_down = \
                    "data/icons/profession/climate/select.jpg"
                self.ids.climate_dry_button.background_normal = \
                    "data/icons/profession/climate/select.jpg"
                self.ids.climate_dry_button.background_down = \
                    "data/icons/profession/climate/select.jpg"
                if mode == 'COOL':
                    self.ids.climate_cool_button.background_normal = "data/icons/profession/climate/selected.jpg"
                    self.ids.climate_cool_button.background_down = "data/icons/profession/climate/selected.jpg"
                    self.profession_climate_mode = 'COOL'
                elif mode == 'HEAT':
                    self.ids.climate_heat_button.background_normal = "data/icons/profession/climate/selected.jpg"
                    self.ids.climate_heat_button.background_down = "data/icons/profession/climate/selected.jpg"
                    self.profession_climate_mode = 'HEAT'
                elif mode == 'DRY':
                    self.ids.climate_dry_button.background_normal = "data/icons/profession/climate/selected.jpg"
                    self.ids.climate_dry_button.background_down = "data/icons/profession/climate/selected.jpg"
                    self.profession_climate_mode = 'DRY'

            self.profession_climate_temp = temp
            if temp == 18:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/18.jpg'
            elif temp == 19:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/19.jpg'
            elif temp == 20:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/20.jpg'
            elif temp == 21:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/21.jpg'
            elif temp == 22:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/22.jpg'
            elif temp == 23:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/23.jpg'
            elif temp == 24:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/24.jpg'
            elif temp == 25:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/25.jpg'
            elif temp == 26:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/26.jpg'
            elif temp == 27:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/27.jpg'
            elif temp == 28:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/28.jpg'
            elif temp == 29:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/29.jpg'
            elif temp == 30:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/30.jpg'

    def update_floor_heat_screen(self):
        if self.profession_floor_heating_switch == 1:
            self.ids.floor_heating_switch_button.background_normal = "data/icons/profession/floor_heating/on.jpg"
            self.ids.floor_heating_switch_button.background_down = "data/icons/profession/floor_heating/on.jpg"
            self.ids.floor_heating_FloatLayout.canvas.before.clear()
            with self.ids.floor_heating_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/floor_heating/background_on.jpg')
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
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/floor_heating/background_off.jpg')
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

    def update_bedroom_light(self):
        if self.profession_lights_bedroom['switch'] == 'on':
            self.ids.lights_bedroom_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bedroom_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/bedroom_background_on.jpg')
            self.ids.lights_bedroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_bedroom['switch'] == 'off':
            self.ids.lights_bedroom_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bedroom_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/lights/bedroom_background_off.jpg')
            self.ids.lights_bedroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bedroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"

    def update_livingroom_light(self):
        if self.profession_lights_livingroom['switch'] == 'on':
            self.ids.lights_livingroom_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_livingroom_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_livingroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/livingroom_background_on.jpg')
            self.ids.lights_livingroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_livingroom['switch'] == 'off':
            self.ids.lights_livingroom_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_livingroom_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_livingroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/lights/livingroom_background_off.jpg')
            self.ids.lights_livingroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_livingroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"

    def update_vestibule_light(self):
        if self.profession_lights_vestibule['switch'] == 'on':
            self.ids.lights_vestibule_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_vestibule_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_vestibule_FloatLayout.canvas.before.clear()
            with self.ids.lights_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/vestibule_background_on.jpg')
            self.ids.lights_vestibule_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_vestibule['switch'] == 'off':
            self.ids.lights_vestibule_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_vestibule_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_vestibule_FloatLayout.canvas.before.clear()
            with self.ids.lights_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/lights/vestibule_background_off.jpg')
            self.ids.lights_vestibule_level_1_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_1_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_2_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_2_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_3_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_3_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_4_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_4_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_5_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_vestibule_level_5_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"

    def update_bashroom_light(self):
        if self.profession_lights_bashroom['switch'] == 'on':
            self.ids.lights_bashroom_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bashroom_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/bashroom_background_on.jpg')
            self.ids.lights_bashroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_bashroom['switch'] == 'off':
            self.ids.lights_bashroom_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bashroom_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/lights/bashroom_background_off.jpg')
            self.ids.lights_bashroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch_disable.jpg"
            self.ids.lights_bashroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch_disable.jpg"

    def update_atmosphere_bedroom(self):
        state = self.api.get_group_light_state('bedroom')
        if state['state'] == 'on':
            if state['state'] != self.profession_atmosphere_bedroom['switch']:
                self.profession_atmosphere_bedroom['switch'] = state['state']
                self.ids.atmosphere_bedroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
                self.ids.atmosphere_bedroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
                self.ids.atmosphere_bedroom_switch_button.canvas.before.clear()
                with self.ids.atmosphere_bedroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                              pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                              source='data/icons/profession/atmosphere/bedroom_background_on.jpg')
                self.profession_atmosphere_bedroom['color'] = 'none'
                self.profession_atmosphere_bedroom['level'] = 'none'

            current_color = self.api.get_light_color('bedroom')
            current_level = self.api.get_light_brightness('bedroom')

            if current_color != self.profession_atmosphere_bedroom['color']:
                self.profession_atmosphere_bedroom['color'] = current_color
                self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1.jpg"
                self.ids.atmosphere_bedroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1.jpg"
                self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2.jpg"
                self.ids.atmosphere_bedroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2.jpg"
                self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3.jpg"
                self.ids.atmosphere_bedroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3.jpg"
                self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4.jpg"
                self.ids.atmosphere_bedroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4.jpg"
                self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5.jpg"
                self.ids.atmosphere_bedroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5.jpg"

                if current_color == 'WHITE':
                    self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                        "data/icons/profession/atmosphere/color_1_on.jpg"
                    self.ids.atmosphere_bedroom_color_1_button.background_down = \
                        "data/icons/profession/atmosphere/color_1_on.jpg"
                elif current_color == 'YELLOW':
                    self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                        "data/icons/profession/atmosphere/color_2_on.jpg"
                    self.ids.atmosphere_bedroom_color_2_button.background_down = \
                        "data/icons/profession/atmosphere/color_2_on.jpg"
                elif current_color == 'PINK':
                    self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                        "data/icons/profession/atmosphere/color_3_on.jpg"
                    self.ids.atmosphere_bedroom_color_3_button.background_down = \
                        "data/icons/profession/atmosphere/color_3_on.jpg"
                elif current_color == 'BLUE':
                    self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                        "data/icons/profession/atmosphere/color_4_on.jpg"
                    self.ids.atmosphere_bedroom_color_4_button.background_down = \
                        "data/icons/profession/atmosphere/color_4_on.jpg"
                elif current_color == 'GREEN':
                    self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                        "data/icons/profession/atmosphere/color_5_on.jpg"
                    self.ids.atmosphere_bedroom_color_5_button.background_down = \
                        "data/icons/profession/atmosphere/color_5_on.jpg"

            if current_level != self.profession_atmosphere_bedroom['level']:
                self.profession_atmosphere_bedroom['level'] = current_level
                self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bedroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"

                if current_level == 'LEVEL_ONE':
                    self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bedroom_level_1_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_TWO':
                    self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bedroom_level_2_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_THREE':
                    self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bedroom_level_3_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_FOUR':
                    self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bedroom_level_4_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_FIVE':
                    self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bedroom_level_5_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"

        elif state['state'] == 'off':
            if self.profession_atmosphere_bedroom['switch'] != state['state']:
                self.profession_atmosphere_bedroom['switch'] = state['state']
                self.ids.atmosphere_bedroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
                self.ids.atmosphere_bedroom_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
                self.ids.atmosphere_bedroom_FloatLayout.canvas.before.clear()
                with self.ids.atmosphere_bedroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                              pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                              source='data/icons/profession/atmosphere/bedroom_background_off.jpg')
                self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bedroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"

                self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_off.jpg"
                self.ids.atmosphere_bedroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_off.jpg"
                self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_off.jpg"
                self.ids.atmosphere_bedroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_off.jpg"
                self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_off.jpg"
                self.ids.atmosphere_bedroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_off.jpg"
                self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_off.jpg"
                self.ids.atmosphere_bedroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_off.jpg"
                self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_off.jpg"
                self.ids.atmosphere_bedroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_off.jpg"

    def update_atmosphere_bashroom(self):
        state = self.api.get_group_light_state('bashroom')
        if state['state'] == 'on':
            if state['state'] != self.profession_atmosphere_bashroom['switch']:
                self.profession_atmosphere_bashroom['switch'] = state['state']
                self.ids.atmosphere_bashroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
                self.ids.atmosphere_bashroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
                self.ids.atmosphere_bashroom_switch_button.canvas.before.clear()
                with self.ids.atmosphere_bashroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                              pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                              source='data/icons/profession/atmosphere/bashroom_background_on.jpg')
                self.profession_atmosphere_bashroom['color'] = 'none'
                self.profession_atmosphere_bashroom['level'] = 'none'

            current_color = self.api.get_light_color('bashroom')
            current_level = self.api.get_light_brightness('bashroom')

            if current_color != self.profession_atmosphere_bashroom['color']:
                self.profession_atmosphere_bashroom['color'] = current_color
                self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1.jpg"
                self.ids.atmosphere_bashroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1.jpg"
                self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2.jpg"
                self.ids.atmosphere_bashroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2.jpg"
                self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3.jpg"
                self.ids.atmosphere_bashroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3.jpg"
                self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4.jpg"
                self.ids.atmosphere_bashroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4.jpg"
                self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5.jpg"
                self.ids.atmosphere_bashroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5.jpg"

                if current_color == 'WHITE':
                    self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                        "data/icons/profession/atmosphere/color_1_on.jpg"
                    self.ids.atmosphere_bashroom_color_1_button.background_down = \
                        "data/icons/profession/atmosphere/color_1_on.jpg"
                elif current_color == 'YELLOW':
                    self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                        "data/icons/profession/atmosphere/color_2_on.jpg"
                    self.ids.atmosphere_bashroom_color_2_button.background_down = \
                        "data/icons/profession/atmosphere/color_2_on.jpg"
                elif current_color == 'PINK':
                    self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                        "data/icons/profession/atmosphere/color_3_on.jpg"
                    self.ids.atmosphere_bashroom_color_3_button.background_down = \
                        "data/icons/profession/atmosphere/color_3_on.jpg"
                elif current_color == 'BLUE':
                    self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                        "data/icons/profession/atmosphere/color_4_on.jpg"
                    self.ids.atmosphere_bashroom_color_4_button.background_down = \
                        "data/icons/profession/atmosphere/color_4_on.jpg"
                elif current_color == 'GREEN':
                    self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                        "data/icons/profession/atmosphere/color_5_on.jpg"
                    self.ids.atmosphere_bashroom_color_5_button.background_down = \
                        "data/icons/profession/atmosphere/color_5_on.jpg"

            if current_level != self.profession_atmosphere_bashroom['level']:
                self.profession_atmosphere_bashroom['level'] = current_level
                self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch.jpg"
                self.ids.atmosphere_bashroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch.jpg"

                if current_level == 'LEVEL_ONE':
                    self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bashroom_level_1_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_TWO':
                    self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bashroom_level_2_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_THREE':
                    self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bashroom_level_3_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_FOUR':
                    self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bashroom_level_4_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                elif current_level == 'LEVEL_FIVE':
                    self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                        "data/icons/profession/atmosphere/switch_h.jpg"
                    self.ids.atmosphere_bashroom_level_5_button.background_down = \
                        "data/icons/profession/atmosphere/switch_h.jpg"

        elif state['state'] == 'off':
            if self.profession_atmosphere_bashroom['switch'] != state['state']:
                self.profession_atmosphere_bashroom['switch'] = state['state']
                self.ids.atmosphere_bashroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
                self.ids.atmosphere_bashroom_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
                self.ids.atmosphere_bashroom_FloatLayout.canvas.before.clear()
                with self.ids.atmosphere_bashroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                              pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                              source='data/icons/profession/atmosphere/bashroom_background_off.jpg')
                self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"
                self.ids.atmosphere_bashroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_disable.jpg"

                self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_off.jpg"
                self.ids.atmosphere_bashroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_off.jpg"
                self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_off.jpg"
                self.ids.atmosphere_bashroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_off.jpg"
                self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_off.jpg"
                self.ids.atmosphere_bashroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_off.jpg"
                self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_off.jpg"
                self.ids.atmosphere_bashroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_off.jpg"
                self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_off.jpg"
                self.ids.atmosphere_bashroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_off.jpg"

    def _update_clock(self, dt):
        #获取新风状态
        if self.ids.sm_profession.current == 'environment_air':
            pass
        #获取地暖状态
        elif self.ids.sm_profession.current == 'environment_floor_heating':
            state = self.api.get_group_switch_state('floor_heat_switch')
            if state == 'on':
                self.profession_floor_heating_switch = 1
                self.update_floor_heat_screen()
            elif state == 'off':
                self.profession_floor_heating_switch = 0
                self.update_floor_heat_screen()
        #获取空调状态
        elif self.ids.sm_profession.current == 'environment_climate':
            state = self.api.get_ac_mode()
            temp = self.api.get_ac_temp()
            self.update_climate_screen(state, temp)
        #获取卧室灯状态
        elif self.ids.sm_profession.current == 'lights_bedroom':
            state = self.api.get_group_switch_state('bedroom_light_switch')
            if state != self.profession_lights_bedroom['switch']:
                self.profession_lights_bedroom['switch'] = state
                self.update_bedroom_light()
        #获取客厅灯状态
        elif self.ids.sm_profession.current == 'lights_livingroom':
            state = self.api.get_group_switch_state('livingroom_light_switch')
            if state != self.profession_lights_livingroom['switch']:
                self.profession_lights_livingroom['switch'] = state
                self.update_livingroom_light()
        #获取玄关灯状态
        elif self.ids.sm_profession.current == 'lights_vestibule':
            state = self.api.get_group_switch_state('vestibule_light_switch')
            if state != self.profession_lights_vestibule['switch']:
                self.profession_lights_vestibule['switch'] = state
                self.update_vestibule_light()
        #获取卫浴灯状态
        elif self.ids.sm_profession.current == 'lights_bashroom':
            state = self.api.get_group_switch_state('bashroom_light_switch')
            if state != self.profession_lights_bashroom['switch']:
                self.profession_lights_bashroom['switch'] = state
                self.update_bashroom_light()
        #获取卧室氛围灯状态
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.update_atmosphere_bedroom()
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.update_atmosphere_bashroom()

    def on_type_selected(self, *args):
        if self.profession_current_type != args[0]:
            if self.profession_current_type < args[0]:
                self.ids.sm_profession.transition.direction = 'left'
            else:
                self.ids.sm_profession.transition.direction = 'right'
            self.profession_current_type = args[0]
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            if args[0] == 1:
                self.ids.sm_profession.current = 'environment_air'
                self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
                self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            elif args[0] == 2:
                self.ids.sm_profession.current = 'lights_bedroom'
                self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
                self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            elif args[0] == 3:
                self.ids.sm_profession.current = 'atmosphere_bedroom'
                self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
                self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            elif args[0] == 4:
                self.ids.sm_profession.current = 'cover_left'
                self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
                self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"

    # 页面切换
    def go_next_screen(self):
        self.ids.sm_profession.transition.direction = 'left'
        if self.ids.sm_profession.current == 'environment_air':
            self.ids.sm_profession.current = 'environment_floor_heating'
        elif self.ids.sm_profession.current == 'environment_floor_heating':
            self.ids.sm_profession.current = 'environment_climate'
        elif self.ids.sm_profession.current == 'environment_climate':
            self.profession_current_type = 2
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'lights_bedroom'
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.ids.sm_profession.current = 'lights_livingroom'
        elif self.ids.sm_profession.current == 'lights_livingroom':
            self.ids.sm_profession.current = 'lights_vestibule'
        elif self.ids.sm_profession.current == 'lights_vestibule':
            self.ids.sm_profession.current = 'lights_bashroom'
        elif self.ids.sm_profession.current == 'lights_bashroom':
            self.profession_current_type = 3
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'atmosphere_bedroom'
        # elif self.ids.sm_profession.current == 'atmosphere_bedroom':
        #     self.ids.sm_profession.current = 'atmosphere_livingroom'
        # elif self.ids.sm_profession.current == 'atmosphere_livingroom':
        #     self.ids.sm_profession.current = 'atmosphere_vestibule'
        # elif self.ids.sm_profession.current == 'atmosphere_vestibule':
        #     self.ids.sm_profession.current = 'atmosphere_bashroom'
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.ids.sm_profession.current = 'atmosphere_bashroom'
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.profession_current_type = 4
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
            self.ids.sm_profession.current = 'cover_left'
        elif self.ids.sm_profession.current == 'cover_left':
            self.ids.sm_profession.current = 'cover_right'
        elif self.ids.sm_profession.current == 'cover_right':
            self.ids.sm_profession.current = 'cover_bashroom'
        elif self.ids.sm_profession.current == 'cover_bashroom':
            self.profession_current_type = 1
            self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'environment_air'

    def go_previous_screen(self):
        self.ids.sm_profession.transition.direction = 'right'
        if self.ids.sm_profession.current == 'environment_floor_heating':
            self.ids.sm_profession.current = 'environment_air'
        elif self.ids.sm_profession.current == 'environment_climate':
            self.ids.sm_profession.current = 'environment_floor_heating'
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.profession_current_type = 1
            self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'environment_climate'
        elif self.ids.sm_profession.current == 'lights_livingroom':
            self.ids.sm_profession.current = 'lights_bedroom'
        elif self.ids.sm_profession.current == 'lights_vestibule':
            self.ids.sm_profession.current = 'lights_livingroom'
        elif self.ids.sm_profession.current == 'lights_bashroom':
            self.ids.sm_profession.current = 'lights_vestibule'
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.profession_current_type = 2
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'lights_bashroom'
        # elif self.ids.sm_profession.current == 'atmosphere_livingroom':
        #     self.ids.sm_profession.current = 'atmosphere_bedroom'
        # elif self.ids.sm_profession.current == 'atmosphere_vestibule':
        #     self.ids.sm_profession.current = 'atmosphere_livingroom'
        # elif self.ids.sm_profession.current == 'atmosphere_bashroom':
        #     self.ids.sm_profession.current = 'atmosphere_vestibule'
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.ids.sm_profession.current = 'atmosphere_bedroom'
        elif self.ids.sm_profession.current == 'cover_left':
            self.profession_current_type = 3
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'atmosphere_bashroom'
        elif self.ids.sm_profession.current == 'cover_right':
            self.ids.sm_profession.current = 'cover_left'
        elif self.ids.sm_profession.current == 'cover_bashroom':
            self.ids.sm_profession.current = 'cover_left'
        elif self.ids.sm_profession.current == 'environment_air':
            self.profession_current_type = 4
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
            self.ids.sm_profession.current = 'cover_bashroom'

    #新风快关
    def on_air_switch_selected(self):
        if self.profession_air_switch == 0:
            self.ids.air_FloatLayout.canvas.before.clear()
            with self.ids.air_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/air/background_on.jpg')
            self.ids.air_switch_button.background_normal = "data/icons/profession/air/on.jpg"
            self.ids.air_switch_button.background_down = "data/icons/profession/air/on.jpg"
            self.profession_air_switch = 1
        else:
            self.ids.air_FloatLayout.canvas.before.clear()
            with self.ids.air_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/air/background_off.jpg')
            self.ids.air_switch_button.background_normal = "data/icons/profession/air/off.jpg"
            self.ids.air_switch_button.background_down = "data/icons/profession/air/off.jpg"
            self.profession_air_switch = 0

    #地暖开关
    def on_floor_heating_switch_selected(self):
        if self.profession_floor_heating_switch == 0:
            self.api.set_group_switch_on('floor_heat_switch')
        else:
            self.api.set_group_switch_off('floor_heat_switch')

    #地暖温度调节
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

    #空调开关
    def on_climate_switch_selected(self):
        if self.profession_climate_switch == 0:
            self.api.set_ac_mode('COOL')
        else:
            self.api.set_ac_mode('False')
            self.profession_climate_mode = 'None'

    #空调模式选择
    def on_climate_mode_selected(self, *args):
        if self.profession_climate_switch == 1:
            self.api.set_ac_mode(args[0])

    # 空调温度
    def on_climate_temp_selected(self, *args):
        temp = self.api.get_ac_temp()
        if args[0] is 'up':
            if temp < 30:
                temp = temp + 1
        elif args[0] is 'down':
            if temp > 18:
                temp = temp - 1
        self.api.set_ac_temp(temp)

    #卧室灯
    def on_lights_bedroom_switch_selected(self):
        if self.profession_lights_bedroom['switch'] == 'on':
            self.api.set_group_switch_off('bedroom_light_switch')
        else:
            self.api.set_group_switch_on('bedroom_light_switch')

    #卧室灯亮度选择
    def on_lights_bedroom_level_selected(self,*args):
        if self.profession_lights_bedroom['switch'] == 1:
            self.ids.lights_bedroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    #客厅灯开关
    def on_lights_livingroom_switch_selected(self):
        if self.profession_lights_livingroom['switch'] == 'on':
            self.api.set_group_switch_off('livingroom_light_switch')
        else:
            self.api.set_group_switch_on('livingroom_light_switch')

    #客厅灯亮度选择
    def on_lights_livingroom_level_selected(self, *args):
        if self.profession_lights_livingroom['switch'] == 1:
            self.ids.lights_livingroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_livingroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_livingroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_livingroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_livingroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_livingroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    # 玄关灯开关
    def on_lights_vestibule_switch_selected(self):
        if self.profession_lights_vestibule['switch'] == 'on':
            self.api.set_group_switch_off('vestibule_light_switch')
        else:
            self.api.set_group_switch_on('vestibule_light_switch')

    # 玄关灯亮度选择
    def on_lights_vestibule_level_selected(self, *args):
        if self.profession_lights_vestibule['switch'] == 1:
            self.ids.lights_vestibule_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_vestibule_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_vestibule_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_vestibule_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_vestibule_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_vestibule_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"


    # 浴室灯开关
    def on_lights_bashroom_switch_selected(self):
        if self.profession_lights_bashroom['switch'] == 'on':
            self.api.set_group_switch_off('bashroom_light_switch')
        else:
            self.api.set_group_switch_on('bashroom_light_switch')

    # 浴室灯亮度选择
    def on_lights_bashroom_level_selected(self, *args):
        if self.profession_lights_bashroom['switch'] == 1:
            self.ids.lights_bashroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    #卧室氛围灯开关
    def on_atmosphere_bedroom_switch_selected(self):
        if self.profession_atmosphere_bedroom['switch'] == 'off':
            self.api.set_group_light_switch_on('bedroom')
        else:
            self.api.set_group_light_off('bedroom')


    #卧室氛围灯亮度调节
    def on_atmosphere_bedroom_level_selected(self,*args):
        if self.profession_atmosphere_bedroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_brightness('bedroom', 'LEVEL_ONE')
            elif args[0] == 2:
                self.api.set_light_brightness('bedroom', 'LEVEL_TWO')
            elif args[0] == 3:
                self.api.set_light_brightness('bedroom', 'LEVEL_THREE')
            elif args[0] == 4:
                self.api.set_light_brightness('bedroom', 'LEVEL_FOUR')
            elif args[0] == 5:
                self.api.set_light_brightness('bedroom', 'LEVEL_FIVE')

    def on_atmosphere_bedroom_color_selected(self, *args):
        if self.profession_atmosphere_bedroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_color('bedroom', 'WHITE')
            elif args[0] == 2:
                self.api.set_light_color('bedroom', 'YELLOW')
            elif args[0] == 3:
                self.api.set_light_color('bedroom', 'PINK')
            elif args[0] == 4:
                self.api.set_light_color('bedroom', 'BLUE')
            elif args[0] == 5:
                self.api.set_light_color('bedroom', 'GREEN')

    def on_atmosphere_livingroom_switch_selected(self):
        if self.profession_atmosphere_livingroom['switch'] == 0:
            self.profession_atmosphere_livingroom['switch'] = 1
            self.ids.atmosphere_livingroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_livingroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_livingroom_switch_button.canvas.before.clear()
            with self.ids.atmosphere_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/livingroom_background_on.jpg')
            self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"

            self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
        else:
            self.profession_atmosphere_livingroom['switch'] = 0
            self.ids.atmosphere_livingroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_livingroom_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_livingroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/livingroom_background_off.jpg')
            self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"

            self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_livingroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5_off.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5_off.jpg"

    #客厅氛围灯亮度调节
    def on_atmosphere_livingroom_level_selected(self,*args):
        if self.profession_atmosphere_livingroom['switch'] == 1:
            self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            if args[0] == 1:
                self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"

    def on_atmosphere_livingroom_color_selected(self,*args):
        if self.profession_atmosphere_livingroom['switch'] == 1:
            self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
            if args[0] == 1:
                self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_livingroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_livingroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_livingroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_livingroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_livingroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

    def on_atmosphere_vestibule_switch_selected(self):
        if self.profession_atmosphere_vestibule['switch'] == 0:
            self.profession_atmosphere_vestibule['switch'] = 1
            self.ids.atmosphere_vestibule_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_vestibule_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_vestibule_switch_button.canvas.before.clear()
            with self.ids.atmosphere_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/vestibule_background_on.jpg')
            self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"

            self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
        else:
            self.profession_atmosphere_vestibule['switch'] = 0
            self.ids.atmosphere_vestibule_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_vestibule_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_vestibule_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/vestibule_background_off.jpg')
            self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"

            self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_vestibule_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5_off.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5_off.jpg"

    #玄关氛围灯亮度调节
    def on_atmosphere_vestibule_level_selected(self,*args):
        if self.profession_atmosphere_vestibule['switch'] == 1:
            self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            if args[0] == 1:
                self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"

    def on_atmosphere_vestibule_color_selected(self,*args):
        if self.profession_atmosphere_vestibule['switch'] == 1:
            self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
            if args[0] == 1:
                self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_vestibule_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_vestibule_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_vestibule_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_vestibule_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_vestibule_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

    def on_atmosphere_bashroom_switch_selected(self):
        if self.profession_atmosphere_bashroom['switch'] == 'off':
            self.api.set_group_light_switch_on('bashroom')
        else:
            self.api.set_group_light_off('bashroom')

    #浴室氛围灯亮度调节
    def on_atmosphere_bashroom_level_selected(self,*args):
        if self.profession_atmosphere_bashroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_brightness('bashroom', 'LEVEL_ONE')
            elif args[0] == 2:
                self.api.set_light_brightness('bashroom', 'LEVEL_TWO')
            elif args[0] == 3:
                self.api.set_light_brightness('bashroom', 'LEVEL_THREE')
            elif args[0] == 4:
                self.api.set_light_brightness('bashroom', 'LEVEL_FOUR')
            elif args[0] == 5:
                self.api.set_light_brightness('bashroom', 'LEVEL_FIVE')

    def on_atmosphere_bashroom_color_selected(self,*args):
        if self.profession_atmosphere_bashroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_color('bashroom', 'WHITE')
            elif args[0] == 2:
                self.api.set_light_color('bashroom', 'YELLOW')
            elif args[0] == 3:
                self.api.set_light_color('bashroom', 'PINK')
            elif args[0] == 4:
                self.api.set_light_color('bashroom', 'BLUE')
            elif args[0] == 5:
                self.api.set_light_color('bashroom', 'GREEN')

    #窗帘
    def on_cover_left_action_button(self):
        if self.profession_cover_left['action'] == 0:
            self.profession_cover_left['action'] = 1
            self.ids.cover_left_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_left_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_left['action'] = 0
            self.ids.cover_left_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_left_move_button(self, *args):
        if args[0] == 1:
            #升起
            pass
        elif args[0] == 2:
            #停止
            pass
        elif args[0] == 3:
            #下降
            pass

    def on_cover_left_postion_button(self, *args):
        if self.profession_cover_left['postion'] == 1:
            self.ids.cover_left_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_1_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_2_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_3_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.cover_left_postion_4_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_postion_5_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            if args[0] == 1:
                self.ids.cover_left_postion_1_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_left_postion_1_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 2:
                self.ids.cover_left_postion_2_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_left_postion_2_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 3:
                self.ids.cover_left_postion_3_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_left_postion_3_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 4:
                self.ids.cover_left_postion_4_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_left_postion_4_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 5:
                self.ids.cover_left_postion_5_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_left_postion_5_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"

    def on_cover_right_action_button(self):
        if self.profession_cover_right['action'] == 0:
            self.profession_cover_right['action'] = 1
            self.ids.cover_right_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_right_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_right['action'] = 0
            self.ids.cover_right_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_right_move_button(self, *args):
        if args[0] == 1:
            #升起
            pass
        elif args[0] == 2:
            #停止
            pass
        elif args[0] == 3:
            #下降
            pass

    def on_cover_right_postion_button(self, *args):
        if self.profession_cover_right['postion'] == 1:
            self.ids.cover_right_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_1_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_2_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_3_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.cover_right_postion_4_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_postion_5_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            if args[0] == 1:
                self.ids.cover_right_postion_1_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_right_postion_1_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 2:
                self.ids.cover_right_postion_2_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_right_postion_2_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 3:
                self.ids.cover_right_postion_3_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_right_postion_3_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 4:
                self.ids.cover_right_postion_4_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_right_postion_4_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 5:
                self.ids.cover_right_postion_5_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_right_postion_5_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"

    def on_cover_bashroom_action_button(self):
        if self.profession_cover_bashroom['action'] == 0:
            self.profession_cover_bashroom['action'] = 1
            self.ids.cover_bashroom_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_bashroom_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_bashroom['action'] = 0
            self.ids.cover_bashroom_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_bashroom_move_button(self, *args):
        if args[0] == 1:
            #升起
            pass
        elif args[0] == 2:
            #停止
            pass
        elif args[0] == 3:
            #下降
            pass

    def on_cover_bashroom_postion_button(self, *args):
        if self.profession_cover_bashroom['postion'] == 1:
            self.ids.cover_bashroom_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_1_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_2_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_3_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.cover_bashroom_postion_4_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_postion_5_button.background_down = \
                "data/icons/profession/cover/switch.jpg"
            if args[0] == 1:
                self.ids.cover_bashroom_postion_1_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_bashroom_postion_1_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 2:
                self.ids.cover_bashroom_postion_2_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_bashroom_postion_2_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 3:
                self.ids.cover_bashroom_postion_3_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_bashroom_postion_3_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 4:
                self.ids.cover_bashroom_postion_4_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_bashroom_postion_4_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
            elif args[0] == 5:
                self.ids.cover_bashroom_postion_5_button.background_normal = \
                    "data/icons/profession/cover/switch_h.jpg"
                self.ids.cover_bashroom_postion_5_button.background_down = \
                    "data/icons/profession/cover/switch_h.jpg"
