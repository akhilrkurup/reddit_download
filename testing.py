# -*- coding: utf-8 -*-
"""
Created on Mon May 16 13:26:32 2022

@author:Akhil R Kurup
"""

import requests

url = "https://v.redd.it/nampy3jhalx71/DASH_720.mp4?source=fallback"
res = requests.get(url)
with open("test.mp4", "wb") as out:
    out.write(res.content)
    print("fone")
fall
