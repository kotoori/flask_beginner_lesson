from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #直接ドメインでアクセスがあった場合
def index():
  toppage = 'トップページ'
  submessage = 'トップページに記述する文言'
  return render_template('top.html', word1=toppage, word2=submessage)

@app.route('/list')
def itemlist():
  return render_template('list.html')

if __name__ == "__main__":
  app.run()
