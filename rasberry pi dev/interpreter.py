#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Alex Fan [8:22 PM]
# {“n”:0,“nModified”:0,“ok”:1}
# GET: localhost:3000/remaining?roomId=1
# 返回一个数字 (edited)
# POST: localhost:3000/usage
# parameter: key: roomId; value=数字
# 返回一个JSON {“n”:0,“nModified”:0,“ok”:1} (edited)

import requests

url_base = 'http://192.168.43.75:3000/'


def getNum(room_number):
    url = url_base + 'remaining?roomId=' + str(room_number)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
    except Exception as e:
        print(e)


def sendData(roomId):
    url = url_base + 'usage?roomId=' + str(roomId)
    try:
        r = requests.post(url, data={'roomId': roomId})
        if r.status_code == 200:
            print('Data sent.')
    except Exception as e:
        print(e)
