from flask import Flask

app = Flask(__name__)

@app.route('/') #直接ドメインでアクセスがあった場合
def flasklang():
  return '<h1>Created by Flask</h1>'

if __name__ == "__main__":
  app.run()
