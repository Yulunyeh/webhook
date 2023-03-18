from flask import Flask #載入Flask
app=Flask(__name__) #建立application 物件

#建立網站首頁的回應方式
@app.route("/") 
def index(): #用來回應網頁首頁連線的函式
    return "hello flask!!!!!吃早餐了"

@app.route("/page1")
def info():
    return "相關資訊"
#啟動伺服器
app.run()
