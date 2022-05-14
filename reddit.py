# -*- coding: utf-8 -*-
"""
Created on Sat May 14 20:08:29 2022

@author:Akhil R Kurup
"""
import praw, json

reddit = praw.Reddit(
    client_id="mlCV4KaLVVmrOj6nz2ULZQ",
    client_secret="DC0wvImgiUPixsQR2FrJvkvdr1JOew",
    user_agent="my user agent",
)

sr = reddit.subreddit("memes")
for subm in sr.hot(limit=1):
    with open("vars.txt", "w") as f:
        f.write(str(vars(subm)))
