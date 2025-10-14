from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/post', methods=['POST']) #POSTで送られてくるデータを受け取るためにmethodsを指定
def post_data():
  #フォームデータを取得
  name =request.form.get('name')
  email =request.form.get('email')

  if name and email:
    #両方ともデータがあるとき、メッセージを表示
    return f"Received: Name={name}, Email={email}"
  else:
    #データがないとき、エラーメッセージを表示
    return "No Data Received",400

if __name__ == "__main__":
  app.run()