# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:24:41 2022

@author:Akhil R Kurup
"""
import pickle, requests
import datetime
import send_mail

with open("urls.pickle", "rb") as f:
    urls = pickle.load(f)
with open("titles.pickle", "rb") as g:
    titles = pickle.load(g)
with open("counter.txt", "r") as t:
    a = t.read()
    i = int(a)
if i > len(titles):
    send_mail.prob_mail()
else:
    if urls[i][-3:] == "gif":
        res = requests.get(urls[i])
        if res.status_code == 200:
            title = titles[i] + ".gif"
            with open(r"gifs/" + title, "wb") as out:
                out.write(res.content)
            print("downloaded")
            send_mail.send_mail(r"gifs/" + title, titles[i])
            with open("counter.txt", "w") as counter_txt:
                counter_txt.write(str(i + 1))
        else:
            with open("logfile.txt", "a") as logf:
                logf.write("FAIL on " + datetime.datetime.now())
    else:
        res = requests.get(urls[i])
        if res.status_code == 200:
            title = titles[i] + ".mp4"
            with open(r"gifs/" + title, "wb") as out:
                out.write(res.content)
            print("downloaded")
            send_mail.send_mail(r"gifs/" + title, titles[i])
            with open("counter.txt", "w") as counter_txt:
                counter_txt.write(str(i + 1))
        else:
            with open("logfile.txt", "a") as logf:
                logf.write("FAIL on " + datetime.datetime.now())
