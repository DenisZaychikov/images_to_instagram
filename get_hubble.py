import requests
import os
import os.path
import urllib3


DIR_NAME = 'images'

def get_file_extension(link):
    file_ext = link[link.rfind('.'):]
    return file_ext


def get_photos_from_hubble_collection(url):
    res = requests.get(url)
    images_info = res.json()
    
    for image_info in images_info:
        image_id = image_info['id']
        response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}').json()
        image_link = 'https:' + response['image_files'][-1]['file_url']
        file_extension = get_file_extension(image_link)
        image_name = f'{image_id}{file_extension}'
        save_image(image_link, image_name, path_to_file)
   

def save_image(url, img_name, file_path):
    res = requests.get(url, verify=False)
    image = res.content
    
    with open(f'{file_path}{img_name}', 'wb') as file_image:
        file_image.write(image)



if __name__ == '__main__':
    
    urllib3.disable_warnings()
    
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)
    path_to_file = os.getcwd() + '\\' + DIR_NAME + '\\'
    
    hubble_collection_name = 'wallpaper'
    
    hubble_url = f'http://hubblesite.org/api/v3/images/{hubble_collection_name}'
    get_photos_from_hubble_collection(hubble_url)
