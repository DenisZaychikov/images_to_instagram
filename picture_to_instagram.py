import requests
import os
import os.path

DIR_NAME = 'images'
PIC_NAME = 'hubble.jpeg'



def fetch_spacex_last_launch(url):
    
    res = requests.get(url).json()
    links_with_pictures = res["links"]["flickr_images"]
    
    for index, link in enumerate(links_with_pictures, 1):
        picture_name = f'spacex{index}.jpeg'
        save_picture(link, picture_name, path_to_file)
    

def save_picture(url, pic_name, file_path):
    res = requests.get(url)
    picture = res.content

    with open(f'{file_path}{pic_name}', 'wb') as new_picture:
        new_picture.write(picture)



if __name__ == '__main__':
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)
    path_to_file = os.getcwd() + '\\' + DIR_NAME + '\\'
    
    url = 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spacex_last_launch(url)
