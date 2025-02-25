import ctypes
import os
import requests
from pathlib import Path

username = os.getlogin()
# Check if the request was successful (status code 200)
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
            print("İşlem başarıyla gerçekleşti.")
    else:
        print("İşlem başarısız")


def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# yarın da bunun köpekli versiyonunu yapıcam
selection = input("Köpekli arkaplan istiyorsanız 1, kedili istiyorsanız 2'ye basın. \n")

if selection == "2":
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cat_image_url = data[0]['url']
        home_dir = Path.home()
        image_name = cat_image_url.split('/')[-1]
        save_path = str(home_dir.joinpath(image_name))
        download_image(cat_image_url, save_path)

        set_wallpaper(save_path)
    else:
        print("eror")
elif selection == "1":
    url = "https://api.thedogapi.com/v1/images/search"
    response2 = requests.get(url)
    if response2.status_code == 200:
        data2 = response2.json()
        dog_image_url = data2[0]['url']

        home_dir = Path.home()
        image_name = dog_image_url.split('/')[-1]
        save_path = str(home_dir.joinpath(image_name))
        download_image(dog_image_url, save_path)

        set_wallpaper(save_path)