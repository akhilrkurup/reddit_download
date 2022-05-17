# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:06:59 2022

@author:Akhil R Kurup
"""
import praw, pickle

reddit = praw.Reddit(
    client_id="mlCV4KaLVVmrOj6nz2ULZQ",
    client_secret="DC0wvImgiUPixsQR2FrJvkvdr1JOew",
    user_agent="my user agent",
)

sr = reddit.subreddit("whenthe")
python_subr = sr.top(limit=60)
urls = []
titles = []

for submission in python_subr:
    titles.append(submission.title)
    a = submission.url
    if a[-3:] != "gif":
        a = submission.media["reddit_video"]["fallback_url"]
    urls.append(a)
with open("urls.pickle", "wb") as f:
    pickle.dump(urls, f, pickle.HIGHEST_PROTOCOL)
with open("titles.pickle", "wb") as g:
    pickle.dump(titles, g, pickle.HIGHEST_PROTOCOL)
