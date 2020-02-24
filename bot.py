import praw
from datetime import datetime
import time

client_id = '' 
client_secret = ''
reddit_user = ''
reddit_pass = ''
user_agent = ''
target_sub = '' # Subreddit

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=reddit_user,
                     password=reddit_pass)

sub = reddit.subreddit(target_sub)
mod = sub.mod

then = datetime(2020, 2, 29, 18, 30, 00) # Countdown Date [YEAR, MONTH, DAY, HOUR, MINUTE, SECOND]

counting = -2
while counting < -1:
    now = datetime.now()
    duration = then - now
    time1 = duration.total_seconds()

    day = round(time1 // (24 * 3600))
    time1 = time1 % (24 * 3600)
    hour = round(time1 // 3600)
    time1 %= 3600
    minutes = round(time1 // 60)
    time1 %= 60
    seconds = time1
    
    new_content = '**[{}](#DAYS) DAYS** **[{}](#HOURS) HOURS** **[{}](#MINUTES) MINUTES**'.format(day, hour, minutes) # Sidebar Content for Countdown

    mod.update(description='{}'.format(new_content)) # Update Sidebar

    time.sleep(10)
