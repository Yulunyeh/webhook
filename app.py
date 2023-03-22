from flask import Flask, abort, request #載入Flask
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai


app=Flask(__name__) #建立application 物件
line_bot_api = LineBotApi("cjdsY5UFfcFL5iFWtKGBgZA5XuRNimer8zhHqGWGg4pDzzVIBEe+CahXeBYQQm9oN6JoVhgUhw0rxSEgJ4Fz1x9lNBv4cTMrEMfAJtNs4mFXTOlDcFnKNikw4VDDMT0gImC875xyja2RRbCTBropEgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("ae1838d725d0d9321c4336c7ffda695f")
openai.api_key = "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"

#建立網站首頁的回應方式
@app.route("/") 
def index(): #用來回應網頁首頁連線的函式
    return "hello flask!!!!!吃早餐了"

@app.route("/page1")
def info():
    return "相關資訊"

@app.route("/callback", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello World!!"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body) 

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"

 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=event.message.text,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
                )
    
        
    # if event.source.user_id != "ae1838d725d0d9321c4336c7ffda695f":       
    # Send To Line 
    reply = response.choices[0].text 
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
        
    
#啟動伺服器
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
