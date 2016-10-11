import reddit_interface
import time
import schedule
import database_interface
import source_interface_handler

def start():
    print "--RedditPapers--\n"
    main()

def main():
   #database_interface.main()
    change_wallpaper()
    schedule.every(2).hours.do(database_interface.main)
    schedule.every(15).minutes.do(change_wallpaper)
    
def change_wallpaper():
    print "-Changing Wallpaper-"
    object_links = database_interface.get_photo()
    if not source_interface_handler.main(object_links):
        change_wallpaper()

if __name__ == "__main__":
    start()

while True:
    schedule.run_pending()
    time.sleep(1)