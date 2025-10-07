from flask import Flask, render_template

app = Flask(__name__)

@app.route('/color')
@app.route('/color/<target>')
def selectColor(target = "colorless"): #colorlessはデフォルト値で、targetの値が渡されないときに利用される
  return render_template('colors.html', color = target)

if __name__ == "__main__":
  app.run()
