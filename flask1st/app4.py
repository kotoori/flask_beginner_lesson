from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #直接ドメインでアクセスがあった場合
def index():
  toppage = 'トップページ'
  submessage = 'トップページに記述する文言'
  return render_template('top2.html')

@app.route('/list')
def itemlist():
  return render_template('list2.html')

@app.route('/detail')
def detail():
  return render_template('detail2.html')

if __name__ == "__main__":
  app.run()
