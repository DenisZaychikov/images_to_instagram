import requests
import os
import os.path
from instabot import Bot
from dotenv import load_dotenv
from PIL import Image


DIR_NAME = 'images'


def make_square_image(image):
    picture = Image.open(f'{DIR_NAME}/{image}') 
    horizontal_size, vertical_size = picture.size
    if horizontal_size < vertical_size:
        offset = (vertical_size - horizontal_size)//2
        coordinates = (0, offset, picture.width, picture.height - offset)
        cropped_image = picture.crop(coordinates)
        cropped_image.save(f'{DIR_NAME}/{image}')
    elif vertical_size < horizontal_size:
        offset = (horizontal_size - vertical_size)//2
        coordinates = (offset, 0, picture.width - offset, picture.height)
        cropped_image = picture.crop(coordinates)
        cropped_image.save(f'{DIR_NAME}/{image}')
        

def is_jpeg_format(image):
    picture = Image.open(f'{DIR_NAME}/{image}')
    return picture.format == 'JPEG'
        


if __name__ == '__main__':
        
    if not os.path.exists(DIR_NAME):
        print('You have not downloaded any images')
    else:
        load_dotenv()
        instagram_login = os.getenv('INSTAGRAM_LOGIN')
        instagram_password = os.getenv('INSTAGRAM_PASSWORD')

        bot = Bot()
        bot.login(username=instagram_login, password=instagram_password)
        images_from_file_path = os.listdir(DIR_NAME)
        
        for image in images_from_file_path:
            make_square_image(image)
            if is_jpeg_format(image):
                bot.upload_photo(f'{DIR_NAME}/{image}', caption=f'{image}')
            


