# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:24:41 2022

@author:Akhil R Kurup
"""
import pickle, requests
import datetime

with open("urls.pickle", "rb") as f:
    urls = pickle.load(f)
with open("titles.pickle", "rb") as g:
    titles = pickle.load(g)
with open("counter.txt", "r") as t:
    a = t.read()
    i = int(a)
print(urls)
"""res = requests.get(urls[i])
if res.status_code == 200:
    title = titles[i] + ".gif"
    with open(r"gifs/" + title, "wb") as out:
        out.write(res.content)
    with open("counter.txt", "w") as counter_txt:
        counter_txt.write(str(i + 1))
else:
    with open("logfile.txt", "a") as logf:
        logf.write("FAIL on " + datetime.datetime.now())
"""