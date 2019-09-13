import requests
import os
import os.path
import urllib3


DIR_NAME = 'images'


def get_photos_from_hubble_collection(url):
    res = requests.get(url)
    images_info = res.json()
    
    for image_info in images_info:
        image_id = image_info['id']
        response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}').json()
        image_link = 'https:' + response['image_files'][-1]['file_url']
        _, file_extension = os.path.splitext(image_link)
        image_name = f'{image_id}{file_extension}'
        save_image(image_link, image_name, path_to_file)
   

def save_image(url, img_name, file_path):
    res = requests.get(url, verify=False)
    image = res.content
    
    with open(os.path.join(file_path, img_name), 'wb') as file_image:
        file_image.write(image)



if __name__ == '__main__':
    
    urllib3.disable_warnings()
    
    os.makedirs(DIR_NAME, exist_ok=True)
    path_to_file = os.path.join(os.getcwd(), DIR_NAME)
    
    hubble_collection_name = 'wallpaper'
    
    hubble_url = f'http://hubblesite.org/api/v3/images/{hubble_collection_name}'
    get_photos_from_hubble_collection(hubble_url)
