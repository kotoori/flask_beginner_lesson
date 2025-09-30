from flask import Flask

app = Flask(__name__)

@app.route('/') #直接ドメインでアクセスがあった場合
def flasklang():
  return '<h1>Created by Flask</h1>'

@app.route('/list/<value>')
def list(value:str): #Flaskが自動的にstrにキャストしてくれる
  return f'{value}が渡された(list)'

@app.route('/detail/<int:number>') #<number>は整数が入ってくる必要がある。整数以外だとここには引っかからず404にルーティングされる
def detail(number:int):
  return f'{number}が渡された(detail)'

@app.route('/double/<value>/<int:number>')
def double(value:str, number:int): #複数のパラメータを受け取る
  return f'{value}と{number}が渡された(double)'

if __name__ == "__main__":
  app.run()