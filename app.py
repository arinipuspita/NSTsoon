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
line_bot_api = LineBotApi('yedyEQI4iYlgdf6Y1NeXNIPCwtkRxDej+z9N/vn0vU80pGtpUO5UitOcQi98lIeVG7V/Dln4AcVtitVmOy4yuORb0T75x1HanlnOijX5xsSKtQGZoOp9Mt3BvLVntct/WG6kcpMnpVvOFkDRchw7ZQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a4f818fc0c5aa0b0b333c63def153323')
#===========[ NOTE SAVER ]=======================
notes = {}
#REQUEST DATA MHS dibawah notes = {}
def carilirik(artist,judul):
    URLlirik = " https://orion.apiseeds.com/documentation/lyric " + artist +"/" + judul +"?apikey=v3mwDfvdEaG64MTSHgm2Rtw4l00bfwLFhcWlymLV2bul7qQaASGSFeHAV85TjyYd"
    r = requests.get(URLlirik)
    data = r.json()
 
    if 'error' not in data:
        nrp = data['result']['track']['name']
        lirik = data['result']['track']['text'] 
        #print(lirik)
       # name = data['track'][0]['name']
        text = data['track'][0]['text']
        data= "text : "+text
        return data

    if 'error' in the data:
        err = data['error'];
        print(err)
        
    #carimhs("maroon 5","sugar")

 Post Request
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
    text = event.message.text #simplify for receive message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)

    data=text.split('-')
    if(data[0]=='lihat'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=carilirik(data[1], data[2])))
    #line_bot_api.reply_message(event.reply_token,TextSendMessage(text = event.message.text + ' ' + profile.display_name))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
