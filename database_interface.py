import cPickle as pickle
import reddit_interface

MAX_LENGTH = 100
database = {}
database['links'] = []

def main():
    print "--Database Interface--"
    database = open_database()
    add_links(reddit_interface.main())
    size_limiter()
    commit()

def size_limiter():
    print "Checking database size."
    global database
    global MAX_LENGTH
    image_links = database['links']
    if len(image_links) > MAX_LENGTH:
        too_large_by = len(image_links) - MAX_LENGTH
        print "Shortening database, " + unicode(len(image_links)) + "links. Max is " + unicode(MAX_LENGTH) + "."
        image_links = image_links[too_large_by:]
        database['links'] = image_links

def get_photo():
    print "Getting next photo link"
    global database
    database = open_database()
    image_links = database['links']
    try:
        link = image_links[0]
    except:
        main()
        database = open_database()
        image_links = database['links']
        link = image_links[0]
    image_links = image_links[1:]
    database['links'] = image_links
    commit()
    print "Passing link " + unicode(link)
    return link

def open_database():
    global database
    try:
        database = pickle.load( open( "photolinks", "rb" ) )
        print "Database opened succesfully."
    except:
        pass
    return database

def add_links(links):
    global database
    #links_final = []
    # for link in links:
    #     if check_unique(link):
    #         print "Unique, adding " + unicode(link['img_url'])
    #         links_final += [link]
    #     else:
    #         print "NOT unique, moving right along..."
    database['links'] += [link for link in links if check_unique(link)]

def check_unique(link):
    global database
    if "imgur" not in link['img_url']:
        return False
    for link_whole in database['links']:
        if link['img_url'] == link_whole['img_url']:
            return False
    return True
    
def commit():
    global database
    print "Writing database to disk."
    pickle.dump( database, open( "photolinks", "wb" ) )

if __name__ == "__main__":
    ## Run to force update content
    main()
