import requests
import os
import os.path
import urllib3


DIR_NAME = 'images'


def get_spacex_last_launch(url):
    res = requests.get(url).json()
    links_with_images = res["links"]["flickr_images"]
    
    for index, link in enumerate(links_with_images, 1):
        _, file_extension = os.path.splitext(link)
        image_name = f'spacex{index}{file_extension}'
        save_image(link, image_name, path_to_file)


def save_image(url, img_name, file_path):
    res = requests.get(url, verify=False)
    image = res.content
    
    with open(os.path.join(file_path, img_name), 'wb') as file_image:
        file_image.write(image)



if __name__ == '__main__':

    urllib3.disable_warnings()
        
    os.makedirs(DIR_NAME, exist_ok=True)
    path_to_file = os.path.join(os.getcwd(), DIR_NAME)
    
    spacex_launch = 'latest'
        
    spacex_url = f'https://api.spacexdata.com/v3/launches/{spacex_launch}'
    get_spacex_last_launch(spacex_url)
