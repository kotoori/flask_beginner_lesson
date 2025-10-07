from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter('truncate') #truncateがカスタムフィルタの名前
def str_truncate(value, length = 10):
  #lengthで指定した文字数よりも長い場合、後ろを切って…を足す
  return value[:length] + '…' if len(value) > length else value

@app.route('/filter')
def show_filter():
  word = 'Python'
  long_word = 'Python Programming with Flask!!!'
  return render_template('filter.html', show_word = word, long_show_word = long_word)

if __name__ == "__main__":
  app.run()