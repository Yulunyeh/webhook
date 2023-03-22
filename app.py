from flask import Flask, abort, request #載入Flask
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai
import configparser
import requests

app=Flask(__name__) #建立application 物件
line_bot_api = LineBotApi("cjdsY5UFfcFL5iFWtKGBgZA5XuRNimer8zhHqGWGg4pDzzVIBEe+CahXeBYQQm9oN6JoVhgUhw0rxSEgJ4Fz1x9lNBv4cTMrEMfAJtNs4mFXTOlDcFnKNikw4VDDMT0gImC875xyja2RRbCTBropEgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("ae1838d725d0d9321c4336c7ffda695f")
openai.api_key = "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"
OPENAI_KEY = openai.api_key
CHATGPT_URL = "https://api.openai.com/v1/completions"

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

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    generated_text = response.choices[0].text 
    return geterated_text
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.user_id != "ae1838d725d0d9321c4336c7ffda695f":
         # model parameter
        data = {
                "model": "text-davinci-003",
                "prompt": event.message.text,
                 "max_tokens": 4000,
                 "temperature": 0.9,
                 # "top_p": 1,
                 # "n": 1,
                 # "stream": False,
                 # "logprobs": None,
                 # "stop": "\n"
                }

        # API from open ai
        response = requests.post(
                CHATGPT_URL,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': " ".join(["Bearer", OPENAI_KEY])
                    },
            json=data)
        res_json = response.json()
        reply_text = res_json.get("choices")[0].get("text").replace("\n", "").replace("?", "")
    
        # Reply the text to client
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text))
         line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=geterated_text))
    
   

#啟動伺服器
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
