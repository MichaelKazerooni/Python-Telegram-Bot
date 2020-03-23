from telegram_bot import telegram_bot
import os

if __name__ == '__main__':
    update_id = None
    # config_folder = (os.path.abspath(
    #     os.path.join(os.path.dirname(__file__), "Scratches/config.cfg")))
    # print(config_folder)
    bot = telegram_bot('config.cfg')
    while(True):
        updates = bot.get_update(offset = update_id)
        for key,value in updates.items():
            if key == 'result':
                print(value)
                for update_info in value:
                    update_id = update_info['update_id']
                    first_name = update_info['message']['from']['first_name']
                    bot.send_message(first_name)
