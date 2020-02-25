# Reddit Countdown Bot
Simple Reddit Bot using PRAW to add a countdown to the Sidebar

# Setup 
- Add :code:`**[](#DAYS) DAYS** **[](#HOURS) HOURS** **[](#MINUTES) MINUTES**` anywhere in the Sidebar.
- Replace :code:`NAME = datetime(2020, 2, 29, 9, 30, 00)` with the date to count down to.
- *If you change the :code:`NAME`, change :code:`content_1 = content(NAME)` too.*
- Set the ```client_id```, ```client_secret```, ```reddit_user```, ```reddit_pass```, ```user_agent```, ```target_sub```

*Note, :code:`reddit_user` has to be able to edit the Sidebar.*
- Run the bot.
  
