# Default Imports

import urllib
import os

# RedditPapers Files

import photo_validity_checker

# Extras

from imgurpython import ImgurClient

# API Login & Creation

client_id = '2ceac47e186d179'
client_secret = '5892bd97f585e7d2290547c5cee4010aa3538b71'
client = ImgurClient(client_id, client_secret)

## Interface

def main(object_id,desired_size):
    print "--IMGUR Interface--"
    print "Getting photo " + object_id
    try:
        photo = client.get_image(object_id)
    except:
        return False
    if not photo_validity_checker.main(photo, desired_size):
        print "Imgur interface failed to retrieve photo."
        return False
    photo_link = photo.link
    folder = "cache"
    photo_save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder, object_id) + ".jpg"
    print "Saving photo to cache"
    urllib.urlretrieve(photo_link, photo_save_path)
    return object_id + ".jpg"

def url_to_id(url):
    ID = url[url.rfind("/") + 1 :]
    if ID.find(".") != -1:
        ID = ID[:ID.find(".")]
    return ID

if __name__ == "__main__":
    main("CkAU5Nv",(2560,1440))