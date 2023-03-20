from flask import Flask, abort, request #載入Flask
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai
import os

app=Flask(__name__) #建立application 物件
line_bot_api = LineBotApi("cjdsY5UFfcFL5iFWtKGBgZA5XuRNimer8zhHqGWGg4pDzzVIBEe+CahXeBYQQm9oN6JoVhgUhw0rxSEgJ4Fz1x9lNBv4cTMrEMfAJtNs4mFXTOlDcFnKNikw4VDDMT0gImC875xyja2RRbCTBropEgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("ae1838d725d0d9321c4336c7ffda695f")


#建立網站首頁的回應方式
@app.route("/") 
def index(): #用來回應網頁首頁連線的函式
    return "hello flasklab!!<br>"

@app.route("/page1")
def info():
    return "相關資訊<br>"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
    retrun reply+"<br>"

#啟動伺服器
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
