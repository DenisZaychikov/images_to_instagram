import requests
import os
import os.path


DIR_NAME = 'images'

def get_file_extension(link):
    file_ext = link[link.rfind('.'):]
    return file_ext


def get_spacex_last_launch(url):
    res = requests.get(url).json()
    links_with_images = res["links"]["flickr_images"]
    
    for index, link in enumerate(links_with_images, 1):
        file_extension = get_file_extension(link)
        image_name = f'spacex{index}{file_extension}'
        save_image(link, image_name, path_to_file)


def save_image(url, img_name, file_path):
    res = requests.get(url, verify=False)
    image = res.content
    
    with open(f'{file_path}{img_name}', 'wb') as file_image:
        file_image.write(image)



if __name__ == '__main__':
        
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)
    path_to_file = os.getcwd() + '\\' + DIR_NAME + '\\'
    
    spacex_launch = 'latest'
        
    spacex_url = f'https://api.spacexdata.com/v3/launches/{spacex_launch}'
    get_spacex_last_launch(spacex_url)
