import requests
import time
import os
import ctypes
from datetime import datetime
import argparse
import random
import struct
# Parsing essential arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", required=True, help ="Source of the wallpapers i.e. collection or random")
parser.add_argument("-i", "--interval", required =False, default=10, type=int,
                    help = "Time interval in seconds to change the wallpaper. Default is 30 seconds")
parser.add_argument("-t1", "--tag1", required=False, default="India",
                    help = "First tag to select wallpapers from random source. Default is India.")
parser.add_argument("-t2", "--tag2", required=False, default= "Punjab",
                    help = "Second tag to select wallpapers from random source")
parser.add_argument("-c_id", "--c_id", required=False, default= str(random.randint(1,999999)),
                    help = "Collection id to select the wallpapers from. Default is any random number.")
parser.add_argument("-r", "--resolution", required= False, default="3840x2160",
                    help="Resolution of the images to be downloaded. Default is 4K i.e.3840x2160 ")
args = vars(parser.parse_args())



def downloader(path, image_Source):
    if image_Source == "random":
        url = "https://source.unsplash.com/" + args["resolution"] + "/?" + args["tag1"] + "," + args["tag2"]
    elif image_Source == "collection":
        url = r"https://source.unsplash.com/collection/"+str(random.randint(1,99999)) + "/" + args["resolution"]
    print(url)
    response = requests.get(url)
    image_name = path + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpeg"
    file = open(image_name, "wb")
    file.write(response.content)
    file.close()
    print(os.stat(image_name).st_size)
    if os.stat(image_name).st_size == 42912 : # this is the size of the error image : if the image is not found
        os.remove(image_name) # removing teh error image
        return 0
    return image_name



if __name__ == '__main__':

    # Creating 2 directories
    username = os.getlogin()
    MAIN_DIR = r"C:/Users/" + username + "/Pictures/"
    mode = 0o666
    # creating splasher and appending two another subfolders
    path_s = os.path.join(MAIN_DIR,"Splasher/")
    path_c = os.path.join(MAIN_DIR,"Splasher/Collection/")
    path_r = os.path.join(MAIN_DIR,"Splasher/Random/")
    if (not (os.path.exists(path_s))):
        os.mkdir(path_s, mode)
    else : pass
    if (not (os.path.exists(path_r))):
            os.mkdir(path_r, mode)
    else: pass

    if (not (os.path.exists(path_c))):
            os.mkdir(path_c, mode)
    else: pass

    # calling function to download and set wallpapers
    wallpapers_Source = args["source"]
    kwrd1 = args["tag1"]
    kwrd2 = args ["tag2"]
    collection_id = "190727"
    if  wallpapers_Source == "random":
        path = path_r
    elif wallpapers_Source == "collection":
        path = path_c
    # checking windows bit size

    system_type = struct.calcsize("P") * 8
    while True:

        img_path = downloader(path,wallpapers_Source)
        if img_path == 0: # if image could not be found in that case
            continue
        SPI_SETDESKWALLPAPER = 20
        if system_type == 64:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, 0)
        elif system_type == 32:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, img_path, 0)
        time.sleep(int(args['interval']))
