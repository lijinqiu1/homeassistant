from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file('data/screens/profession.kv')


class ProfessionFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(ProfessionFloatLayout, self).__init__(**kwargs)
        self.profession_current_screen = 'environment'

        self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"

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
        if self.profession_current_screen == 'environment':
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.profession_current_screen = 'lights'
        elif self.profession_current_screen == 'lights':
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.profession_current_screen = 'atmosphere'
        elif self.profession_current_screen == 'atmosphere':
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
            self.profession_current_screen = 'cover'
        elif self.profession_current_screen == 'cover':
            self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.profession_current_screen = 'environment'

    def go_previous_screen(self):
        if self.profession_current_screen == 'environment':
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
            self.profession_current_screen = 'cover'
        elif self.profession_current_screen == 'lights':
            self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.profession_current_screen = 'environment'
        elif self.profession_current_screen == 'atmosphere':
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.profession_current_screen = 'lights'
        elif self.profession_current_screen == 'cover':
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.profession_current_screen = 'atmosphere'






