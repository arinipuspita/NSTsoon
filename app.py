from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
import re

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Thh0U29j4Q41zOxwiwWN0OqRpFAQfpyh4cEfBb4UQJlDefa2r+tIGMQMlZqFCdW6G7V/Dln4AcVtitVmOy4yuORb0T75x1HanlnOijX5xsRWP252rKY2tpG5ryka/nWVDPvLvoAxhuu6scGaeSQEyAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a69b96ed2f7d23b13f05e45bfb019499')
#===========[ NOTE SAVER ]=======================
notes = {}

def carilirik(artist, judul):
    URLlirik = "https://orion.apiseeds.com/api/music/lyric/" + artist + "/" + judul + "?apikey=v3mwDfvdEaG64MTSHgm2Rtw4l00bfwLFhcWlymLV2bul7qQaASGSFeHAV85TjyYd"

    r = requests.get(URLlirik)
    data = r.json()
    err= "Lyric no found, try again later."

    if 'error' not in data:
        yey = data['result']['track']['name']
        lirik = data['result']['track']['text']
        print(lirik)
        return lirik

    if 'error' in data:
        err = data['error'];
        print(err)
        return err


# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    data=text.split('/')
    # line_bot_api.reply_message(event.reply_token,TextSendMessage(text="masuk"))
    #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=carimhs("Alan Walker","Alone")))
    if(data[0]=='cari'):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=carilirik(data[1], data[2])))
    else :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="keyword yang anda masukkan salah, tulis keyword dengan format : cari/nama artis/ judul lagu"))
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
