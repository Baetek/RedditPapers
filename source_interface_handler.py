import imgur_inteface
import re
import wallpaper_setter

def main(object_links):
    print "--Source Interface Handler--"
    img_url = object_links['img_url']
    if "imgur" in img_url:
        id = imgur_inteface.url_to_id(img_url)
        image_name = imgur_inteface.main(id,(2560,1440))
        if not image_name:
            return False
        wallpaper_setter.main(image_name)
        return True

if __name__ == "__main__":
    main()