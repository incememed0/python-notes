# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# sabahları günaydın mesajı atan program

import requests
import time
import schedule

def send_message():
    resp=requests.post("https://textbelt.com/text",{
        "phone": 9999999999999,
        "message": "good morning",
        "key": "textbelt"
    })
    print(resp.json())

schedule.every().day.at("06:00").do(send_message())