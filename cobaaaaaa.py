# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:20:14 2018

@author: ismai
"""
import requests, json




def carimhs(artist, judul):
    URL = "https://orion.apiseeds.com/api/music/lyric/" + artist + "/" + judul + "?apikey=v3mwDfvdEaG64MTSHgm2Rtw4l00bfwLFhcWlymLV2bul7qQaASGSFeHAV85TjyYd"

    r = requests.get(URL)
    data = r.json()

    if 'error' not in data:
        nrp = data['result']['track']['name']
        lirik = data['result']['track']['text']
        return lirik
        # print(lirik)

    if 'error' in data:
        err = data['error'];
        return err
        # print(err)

a = carimhs("Alan Walker","Alone")
print(a)
