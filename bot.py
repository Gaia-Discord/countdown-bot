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

def content(t): # Countdown Content Function
    now = datetime.now()
    duration = t - now
    time1 = duration.total_seconds()
    day = round(time1 // (24 * 3600))
    time1 = time1 % (24 * 3600)
    hour = round(time1 // 3600)
    time1 %= 3600
    minutes = round((time1 // 60) + 1) # +1 because seconds are hidden
    time1 %= 60
    seconds = time1
    content = '**[{}](#DAYS) DAYS** **[{}](#HOURS) HOURS** **[{}](#MINUTES) MINUTES**'.format(day, hour, minutes)
    return content

PAX = datetime(2020, 2, 29, 9, 30, 00) # Countdown Date [YEAR, MONTH, DAY, HOUR, MINUTE, SECOND] [PST Timezone]

count = -2
while count < -1:
    content_1 = content(PAX)
    print(content_1)
    mod.update(description='{}'.format(content_1)) # Update Sidebar
    time.sleep(10) # Repeat Every 10 Seconds
