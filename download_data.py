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
python_subr = sr.top(limit=25)
urls = []
titles = []
for submission in python_subr:
    urls.append(submission.url)
    titles.append(submission.title)
"""with open("urls.pickle", "wb") as f:
    pickle.dump(urls, f, pickle.HIGHEST_PROTOCOL)
with open("titles.pickle", "wb") as g:
    pickle.dump(titles, g, pickle.HIGHEST_PROTOCOL)"""
