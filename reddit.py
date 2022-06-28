# -*- coding: utf-8 -*-
"""
Created on Sat May 14 20:08:29 2022

@author:Akhil R Kurup
"""
import praw
import requests

reddit = praw.Reddit(
    client_id="##",
    client_secret="##",
    user_agent="my user agent",
)

sr = reddit.subreddit("whenthe")
python_subr = sr.top(limit=50)
urls = []
titles = []
for submission in python_subr:
    urls.append(submission.url)
    titles.append(submission.title)
res = requests.get(urls[0])
print(res.status_code)
with open(titles[0] + ".gif", "wb") as out:
    out.write(res.content)
with open("counter.txt", "w") as counter_txt:
    counter_txt.write(i)
