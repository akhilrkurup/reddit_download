# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:55:55 2022

@author:Akhil R Kurup
"""
import praw, yaml

reddit = praw.Reddit(
    client_id="mlCV4KaLVVmrOj6nz2ULZQ",
    client_secret="DC0wvImgiUPixsQR2FrJvkvdr1JOew",
    user_agent="my user agent",
)

sr = reddit.subreddit("whenthe")
python_subr = sr.top(limit=2)
urls = []
titles = []
i = 0
for submission in python_subr:
    if i == 0:
        i += 1
        continue
    d = submission.media["reddit_video"]["fallback_url"]
    print(d)
