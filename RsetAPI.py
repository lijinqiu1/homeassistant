from requests import get
from requests import post
import json


class RsetAPI():
    def __init__(self):
        self.url = 'http://guoxi.natapp1.cc/api/'
        self.headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTA2NzIzOTAsImlzcyI6ImVmYmU5YWFhMWZlYzQ4YTNhOGVkZTNjNTU2YWE4MTU1IiwiZXhwIjoxODY2MDMyMzkwfQ.GlA1Qb0LmIWqSvkTSgv_7bUyMxq5IfU1kPR9PBBCb5Y',
            'content-type': 'application/json'
        }

    def get_light_state(self, arg):
        response = get(self.url+'states/light.'+arg, headers=self.headers)
        return json.loads(response.text)

    def set_switch_on(self, arg):
        body = {"entity_id": "switch." + arg}

        response = post(self.url + 'services/switch/turn_on', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_switch_off(self, arg):
        body = {"entity_id": "switch." + arg}

        response = post(self.url + 'services/switch/turn_off', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_light_on(self, light, brightness, rgb_color):
        body = {"entity_id": "light." + light, "brightness": brightness, "rgb_color": rgb_color}
        response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_light_off(self, light):
        body = {"entity_id": "light." + light}
        response = post(self.url + 'services/light/turn_off', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_cover_open(self, cover):
        body = {"entity_id": "cover." + cover}
        response = post(self.url + 'services/cover/open_cover', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_cover_close(self, cover):
        body = {"entity_id": "cover." + cover}
        response = post(self.url + 'services/cover/close_cover', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_cover_stop(self, cover):
        body = {"entity_id": "cover." + cover}
        response = post(self.url + 'services/cover/stop_cover', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_cover_position(self, cover, position):
        body = {"entity_id": "input_number." + cover + '_set_position', 'value': position}
        response = post(self.url + 'services/input_number/set_value', data=json.dumps(body), headers=self.headers)
        return response.text

    def get_cover_position(self, cover):
        response = get(self.url + 'states/input_number.'+cover + '_position', headers=self.headers)
        return json.loads(response.text)['state']

    def get_temp(self):
        response = get(self.url + 'states/sensor.wen_du', headers=self.headers)
        return json.loads(response.text)['state']

    def get_hum(self):
        response = get(self.url + 'states/sensor.shi_du', headers=self.headers)
        return json.loads(response.text)['state']

    def get_PM25(self):
        response = get(self.url + 'states/sensor.pm2_5', headers=self.headers)
        return json.loads(response.text)['state']

    def get_jia_quan(self):
        response = get(self.url + 'states/sensor.jia_quan', headers=self.headers)
        return json.loads(response.text)['state']

    def get_liangdu(self,index):
        response = get(self.url + 'states/sensor.liang_du_'+ index, headers=self.headers)
        return json.loads(response.text)['state']

    def set_group_light_on(self, light, brightness, rgb_color):
        body = {"entity_id": "group." + light, "brightness": brightness, "rgb_color": rgb_color}
        response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
        return response.text

    def set_group_light_off(self, light):
        body = {"entity_id": "group." + light}
        response = post(self.url + 'services/light/turn_off', data=json.dumps(body), headers=self.headers)
        return response.text


if __name__ == '__main__':
    api = RsetAPI()
    entity_id = 'bedroom_light'
    brightness = 50
    rgb_color = [255, 0, 0]
    request = api.set_group_light_on(entity_id,brightness,rgb_color)
    print request

