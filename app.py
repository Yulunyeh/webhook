from flask import Flask, abort, request #載入Flask
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai
import os

app=Flask(__name__) #建立application 物件

#建立網站首頁的回應方式
@app.route("/") 
def index(): #用來回應網頁首頁連線的函式
    return "hello flasklab!!<br>"

@app.route("/page1")
def info():
    return "相關資訊<br>"
#啟動伺服器
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
