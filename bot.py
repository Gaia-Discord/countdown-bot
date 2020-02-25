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

then = datetime(2020, 2, 29, 9, 30, 00) # Countdown Date [YEAR, MONTH, DAY, HOUR, MINUTE, SECOND] [PST Timezone]

count = -2
while count < -1:
    now = datetime.now()
    duration = then - now
    timeS = duration.total_seconds()

    day = round(timeS // (24 * 3600))
    timeS = timeS % (24 * 3600)
    hour = round(timeS // 3600)
    timeS %= 3600
    minutes = round(timeS // 60)
    timeS %= 60
    seconds = timeS
    
    new_content = '**[{}](#DAYS) DAYS** **[{}](#HOURS) HOURS** **[{}](#MINUTES) MINUTES**'.format(day, hour, minutes) # Sidebar Content for Countdown

    mod.update(description='{}'.format(new_content)) # Update Sidebar

    time.sleep(10) # Run every 10 seconds
