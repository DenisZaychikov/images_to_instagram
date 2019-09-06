import requests
import os
import os.path
from instabot import Bot
from dotenv import load_dotenv


DIR_NAME = 'images'




if __name__ == '__main__':
        
    if not os.path.exists(DIR_NAME):
        print('You have not downloaded any images')
    else:
        load_dotenv()
        instagram_login = os.getenv('INSTAGRAM_LOGIN')
        instagram_password = os.getenv('INSTAGRAM_PASSWORD')

        bot = Bot()
        bot.login(username=instagram_login, password=instagram_password)
        images_from_file = os.listdir(DIR_NAME)
        for image in images_from_file:
            bot.upload_photo(f'{DIR_NAME}/{image}', caption=f'{image}')




