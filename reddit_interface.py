# Extras

import praw

r = praw.Reddit(user_agent='RedditPapers')

def main(subreddit = 'earthporn'):
    print "--Reddit Interface--"
    print "Getting submissions from " + subreddit
    submissions = r.get_subreddit(subreddit).get_top(limit=100)
    print "Submissions retrieved succesfully"
    photo_links = []
    for submission in submissions:
        data = {}
        data['img_url'] = submission.url
        data['source_url'] = submission.permalink
        photo_links += [data]
    return photo_links

if __name__ == "__main__":
     main('earthporn')