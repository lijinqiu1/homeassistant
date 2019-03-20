#coding=utf-8

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
Builder.load_file('data/screens/profession.kv')


class ProfessionFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(ProfessionFloatLayout, self).__init__(**kwargs)
        self.profession_current_type = 0
        self.profession_air_switch = 0
        self.profession_floor_heating_switch = 0
        self.profession_climate_switch = 0
        self.profession_climate_mode = 'cool'
        self.profession_climate_temp = 25
        self.profession_lights_bedroom = {'switch': 0, 'level': 1}
        self.profession_lights_livingroom = {'switch': 0, 'level': 1}
        self.profession_lights_vestibule = {'switch': 0, 'level': 1}
        self.profession_lights_bashroom = {'switch': 0, 'level': 1}

        self.profession_atmosphere_bedroom = {'switch': 0, 'color': 1, 'level': 1}
        self.profession_atmosphere_livingroom = {'switch': 0, 'color': 1, 'level': 1}
        self.profession_atmosphere_vestibule = {'switch': 0, 'color': 1, 'level': 1}
        self.profession_atmosphere_bashroom = {'switch': 0, 'color': 1, 'level': 1}

        self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"

        self.ids.sm_profession.current = 'environment_air'

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
            if args[0] == 0:
                self.ids.sm_profession.current = 'environment_air'
                self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
                self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            elif args[0] == 1:
                self.ids.sm_profession.current = 'lights_bedroom'
                self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
                self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            elif args[0] == 2:
                self.ids.sm_profession.current = 'atmosphere_bedroom'
                self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
                self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            elif args[0] == 3:
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
            self.profession_current_type = 1
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
            self.profession_current_type = 2
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'atmosphere_bedroom'
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.ids.sm_profession.current = 'atmosphere_livingroom'
        elif self.ids.sm_profession.current == 'atmosphere_livingroom':
            self.ids.sm_profession.current = 'atmosphere_vestibule'
        elif self.ids.sm_profession.current == 'atmosphere_vestibule':
            self.ids.sm_profession.current = 'atmosphere_bashroom'


    #页面切换
    def go_previous_screen(self):
        self.ids.sm_profession.transition.direction = 'right'
        if self.ids.sm_profession.current == 'environment_floor_heating':
            self.ids.sm_profession.current = 'environment_air'
        elif self.ids.sm_profession.current == 'environment_climate':
            self.ids.sm_profession.current = 'environment_floor_heating'
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.profession_current_type = 0
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
            self.profession_current_type = 1
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'lights_bashroom'
        elif self.ids.sm_profession.current == 'atmosphere_livingroom':
            self.ids.sm_profession.current = 'atmosphere_bedroom'
        elif self.ids.sm_profession.current == 'atmosphere_vestibule':
            self.ids.sm_profession.current = 'atmosphere_livingroom'
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.ids.sm_profession.current = 'atmosphere_vestibule'

    #新风快关
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

    #地暖开关
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
            self.ids.climate_switch_button.background_normal = "data/icons/profession/climate/on.jpg"
            self.ids.climate_switch_button.background_down = "data/icons/profession/climate/on.jpg"
            self.ids.climate_FloatLayout.canvas.before.clear()
            with self.ids.climate_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666), pos=(self.width * 0.15, self.height * 0.096),
                          source='data/icons/profession/climate/background_on.jpg')
            self.profession_climate_switch = 1
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
            self.ids.climate_up_button.background_normal = \
                "data/icons/profession/climate/up.jpg"
            self.ids.climate_up_button.background_down = \
                "data/icons/profession/climate/up.jpg"
            self.ids.climate_down_button.background_normal = \
                "data/icons/profession/climate/down.jpg"
            self.ids.climate_down_button.background_down = \
                "data/icons/profession/climate/down.jpg"
        else:
            self.ids.climate_switch_button.background_normal = "data/icons/profession/climate/off.jpg"
            self.ids.climate_switch_button.background_down = "data/icons/profession/climate/off.jpg"
            self.ids.climate_FloatLayout.canvas.before.clear()
            with self.ids.climate_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666), pos=(self.width * 0.15, self.height * 0.096),
                          source='data/icons/profession/climate/background_off.jpg')
            self.profession_climate_switch = 0
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

    #空调模式选择
    def on_climate_mode_selected(self, *args):
        self.ids.climate_heat_button.background_normal = "data/icons/profession/climate/select.jpg"
        self.ids.climate_heat_button.background_down = "data/icons/profession/climate/select.jpg"
        self.ids.climate_cool_button.background_normal = "data/icons/profession/climate/select.jpg"
        self.ids.climate_cool_button.background_down = "data/icons/profession/climate/select.jpg"
        self.ids.climate_dry_button.background_normal = "data/icons/profession/climate/select.jpg"
        self.ids.climate_dry_button.background_down = "data/icons/profession/climate/select.jpg"
        if args[0] == 'heat':
            self.ids.climate_heat_button.background_normal = "data/icons/profession/climate/selected.jpg"
            self.ids.climate_heat_button.background_down = "data/icons/profession/climate/selected.jpg"
            self.profession_climate_mode = 'heat'
        elif args[0] == 'cool':
            self.ids.climate_cool_button.background_normal = "data/icons/profession/climate/selected.jpg"
            self.ids.climate_cool_button.background_down = "data/icons/profession/climate/selected.jpg"
            self.profession_climate_mode = 'cool'
        elif args[0] == 'dry':
            self.ids.climate_dry_button.background_normal = "data/icons/profession/climate/selected.jpg"
            self.ids.climate_dry_button.background_down = "data/icons/profession/climate/selected.jpg"
            self.profession_climate_mode = 'dry'

    def on_climate_temp_selected(self, *args):
        pass

    #卧室灯
    def on_lights_bedroom_switch_selected(self):
        if self.profession_lights_bedroom['switch'] == 0:
            self.profession_lights_bedroom['switch'] = 1
            self.ids.lights_bedroom_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bedroom_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
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
        else:
            self.profession_lights_bedroom['switch'] = 0
            self.ids.lights_bedroom_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bedroom_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
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
        if self.profession_lights_livingroom['switch'] == 0:
            self.profession_lights_livingroom['switch'] = 1
            self.ids.lights_livingroom_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_livingroom_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_livingroom_switch_button.canvas.before.clear()
            with self.ids.lights_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
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
        else:
            self.profession_lights_livingroom_switch = 0
            self.ids.lights_livingroom_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_livingroom_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_livingroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.466), pos=(self.width*0.15, self.height*0.204),
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

    # 客厅灯亮度选择
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
        if self.profession_lights_vestibule['switch'] == 0:
            self.profession_lights_vestibule['switch'] = 1
            self.ids.lights_vestibule_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_vestibule_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_vestibule_switch_button.canvas.before.clear()
            with self.ids.lights_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.466),
                          pos=(self.width * 0.15, self.height * 0.204),
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
        else:
            self.profession_lights_vestibule['switch'] = 0
            self.ids.lights_vestibule_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_vestibule_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_vestibule_FloatLayout.canvas.before.clear()
            with self.ids.lights_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.466),
                          pos=(self.width * 0.15, self.height * 0.204),
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
        if self.profession_lights_bashroom['switch'] == 0:
            self.profession_lights_bashroom['switch'] = 1
            self.ids.lights_bashroom_switch_button.background_normal = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bashroom_switch_button.background_down = "data/icons/profession/lights/on.jpg"
            self.ids.lights_bashroom_switch_button.canvas.before.clear()
            with self.ids.lights_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.466),
                          pos=(self.width * 0.15, self.height * 0.204),
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
        else:
            self.profession_lights_bashroom['switch'] = 0
            self.ids.lights_bashroom_switch_button.background_normal = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bashroom_switch_button.background_down = "data/icons/profession/lights/off.jpg"
            self.ids.lights_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.466),
                          pos=(self.width * 0.15, self.height * 0.204),
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
        if self.profession_atmosphere_bedroom['switch'] == 0:
            self.profession_atmosphere_bedroom['switch'] = 1
            self.ids.atmosphere_bedroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_bedroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_bedroom_switch_button.canvas.before.clear()
            with self.ids.atmosphere_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
                          source='data/icons/profession/atmosphere/bedroom_background_on.jpg')
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
        else:
            self.profession_atmosphere_bedroom['switch'] = 0
            self.ids.atmosphere_bedroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_bedroom_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
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

    #卧室氛围灯亮度调节
    def on_atmosphere_bedroom_level_selected(self,*args):
        if self.profession_atmosphere_bedroom['switch'] == 1:
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
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.atmosphere_bedroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            if args[0] == 1:
                self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"

    def on_atmosphere_bedroom_color_selected(self,*args):
        if self.profession_atmosphere_bedroom['switch'] == 1:
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
            if args[0] == 1:
                self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_bedroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_bedroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_bedroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_bedroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_bedroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

    def on_atmosphere_livingroom_switch_selected(self):
        if self.profession_atmosphere_livingroom['switch'] == 0:
            self.profession_atmosphere_livingroom['switch'] = 1
            self.ids.atmosphere_livingroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_livingroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_livingroom_switch_button.canvas.before.clear()
            with self.ids.atmosphere_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
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
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
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
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
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
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
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
        if self.profession_atmosphere_bashroom['switch'] == 0:
            self.profession_atmosphere_bashroom['switch'] = 1
            self.ids.atmosphere_bashroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_bashroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_bashroom_switch_button.canvas.before.clear()
            with self.ids.atmosphere_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
                          source='data/icons/profession/atmosphere/bashroom_background_on.jpg')
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
        else:
            self.profession_atmosphere_bashroom['switch'] = 0
            self.ids.atmosphere_bashroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_bashroom_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.666),
                          pos=(self.width * 0.15, self.height * 0.096),
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
    #浴室氛围灯亮度调节
    def on_atmosphere_bashroom_level_selected(self,*args):
        if self.profession_atmosphere_bashroom['switch'] == 1:
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
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.atmosphere_bashroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            if args[0] == 1:
                self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"

    def on_atmosphere_bashroom_color_selected(self,*args):
        if self.profession_atmosphere_bashroom['switch'] == 1:
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
            if args[0] == 1:
                self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_bashroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_bashroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_bashroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_bashroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_bashroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
