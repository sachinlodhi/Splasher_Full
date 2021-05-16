import requests
import time
import os
import ctypes
from datetime import datetime
import argparse
import random
import struct
# Parsing essential arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("-s", "--source", required=True, choices = ["random", "collection"],
#                     help ="Source of the wallpapers i.e. collection or random")
# parser.add_argument("-i", "--interval", required =False, default=10, type=int,
#                     help = "Time interval in seconds to change the wallpaper. Default is 30 seconds")
# parser.add_argument("-t1", "--tag1", required=False, default="India",
#                     help = "First tag to select wallpapers from random source. Default is India.")
# parser.add_argument("-t2", "--tag2", required=False, default= "Punjab",
#                     help = "Second tag to select wallpapers from random source")
# parser.add_argument("-c_id", "--c_id", required=False, default= str(random.randint(1,999999)),
#                     help = "Collection id to select the wallpapers from. Default is any random number.")
# parser.add_argument("-r", "--resolution", required= False, default="3840x2160",
#                     help="Resolution of the images to be downloaded. Default is 4K i.e.3840x2160 ")
# parser.add_argument("-v" ,"--verbose", required=False, help= "Turn verbosity ON or OFF. Default is OFF")
# args = vars(parser.parse_args())



def downloader(path, image_Source, params):
    url =''
    if image_Source == "Random":
        if len(params['tags']) > 0:
            url = "https://source.unsplash.com/" + params['resolution'] + "/?" + params['tags']
        else:
            print("[INFO] No tags were supplied. Wallpapers be totally random. Tags can be supplied separated by comma")
            print('E.g. california,usa')
            url =  "https://source.unsplash.com/random/" + params['resolution']
        print(f"URL : {url}")



    elif image_Source == "Collection":
        url = r"https://source.unsplash.com/collection/"+str(random.randint(1,99999)) + "/" + params["resolution"]
    try:
        response = requests.get(url)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("[ERROR] Some error occurred! Check Internet Connection.")
        return 0
    image_name = path + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpeg"
    file = open(image_name, "wb")
    file.write(response.content)
    file.close()

    if os.stat(image_name).st_size == 42912 : # this is the size of the error image : if the image is not found
        os.remove(image_name) # removing teh error image
        return 0
    return image_name


def begin(params):
    print("[INFO] Splasher. Developed by Sachin Lodhi.")
    print("[INFO] Splasher Started!!!!")
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
    wallpapers_Source = params["source"]
    # tags = str(params['tags']).split(",")
    # kwrd1,kwrd2 = 'california', 'usa'
    # try:
    #     kwrd1 = tags[0]
    #     kwrd2 = tags[1]
    # except:
    #     pass
    collection_id = params['collectionID']
    time_Interval = int(params['time'])
    resolution = params['resolution']
    verbosrity = params['verbose_ON']
    if  wallpapers_Source == "Random":
        path = path_r
        print("[INFO] Wallpaper SOURCE is {}".format(wallpapers_Source))
        print("[INFO] Wallpaper TAGS are  {}".format(params['tags']))
    elif wallpapers_Source == "Collection":
        path = path_c
        print("[INFO] Wallpaper SOURCE is {}".format(wallpapers_Source))
        print("[INFO] Wallpaper COLLECTION ID is {}".format(collection_id))
    # checking windows bit size

    system_type = struct.calcsize("P") * 8 # checking the windows bit size
    print("[INFO] Wallpaper INTERVAL is {} seconds".format(time_Interval))
    print("[INFO] Wallpaper RESOLUTION is {}".format(resolution))
    print("[INFO] Verbosity is {}".format(verbosrity))

    while True:

        img_path = downloader(path,wallpapers_Source,params)
        if img_path == 0: # if image could not be found in that case
            continue
        SPI_SETDESKWALLPAPER = 20
        if system_type == 64:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, 0)
        elif system_type == 32:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, img_path, 0)

        if verbosrity == True:
            print(f"[INFO] Wallpaper has been set and saved at location : {img_path}")

        time.sleep(time_Interval)
