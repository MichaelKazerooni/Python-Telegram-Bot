import requests
import configparser as cfg
import json
from datetime import datetime
class telegram_bot():
    def __init__(self, config):
        self.token = self.read_config_file(config)
        self.base = f"https://api.telegram.org/bot{self.token}/"
        # self.base = f'https://api.telegram.org/bot{self.token}/'
    def get_update(self, offset = None):
        url = self.base + "getUpdates?timeout=100"
        print('url is: ' , url)
        # url = self.base+'getUpdates'
        if offset:
            url += f'&offset={offset + 1}'
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self,audiance_name):
        chat_id = 191305056 # this chat bot only works for specific chat_id
        current_time = datetime.now()
        current_time = current_time.strftime("%H:%M:%S")
        text = f" Hello {audiance_name}. Current time is: {current_time}"
        url = self.base + f"sendMessage?chat_id={chat_id}&text={text}"
        r = requests.post(url)
        return json.loads(r.content)

    def read_config_file(self,config):
        '''
        reads the token info from config file
        :return:
        returns the token
        '''
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')

