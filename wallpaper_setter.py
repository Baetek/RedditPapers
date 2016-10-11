# Default Imports

import ctypes
import os
import time

# Sets current Windows wallpaper to wallpaper in cache folder with passed name

def main(image_name):
    print "--Wallpaper Setter--"
    image_name = str(image_name)
    try:
        folder = "cache"
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),folder,image_name)
        SPI_SETDESKWALLPAPER = 20 
        print "Path is: " + image_path
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        print "Wallpaper changed succesfully"
        return False
    except:
        print "Failed to change wallpaper\nWallpaper name: " + unicode(image_name)
        return True

if __name__ == "__main__":
    # Independent Test
    main("fmkybPo.jpg")
    # Module Dependent Test
    # import imgur_inteface
    # image_name = imgur_inteface.main("CkAU5Nv",(2560,1440))
    # main("image_name")