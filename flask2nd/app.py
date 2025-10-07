from flask import Flask, render_template

app = Flask(__name__)

#商品データ
items = [
  {
    "itemid": 1,
    "itemname": "リンゴ",
    "itemtype": "果物",
    "itemprice": 300
  },
  {
    "itemid": 2,
    "itemname": "トマト",
    "itemtype": "野菜",
    "itemprice": 200
  },
  {
    "itemid": 3,
    "itemname": "鮭",
    "itemtype": "魚",
    "itemprice": 400
  },
]

@app.route('/')
def index():
  toppage = 'とっぷぺーじ'
  return render_template('top.html', word1 = toppage)

@app.route('/list')
def itemlist():
  return render_template('list.html', items = items)

@app.route('/detail/<int:number>')
def detail(number:int):
  item = next((item for item in items if item["itemid"] == number), None)
  #1.条件に合致する最初の要素を返す
  #2.next()は条件に合致した要素の最初の要素を取り出す。ただし要素がなかった場合、第2引数の値を渡す
  if item:
    #合致する商品が存在する場合
    return render_template('detail.html', item = item)
  else:
    #合致する商品がない場合
    return render_template('error404.html', message = '商品が見つかりませんでした')

if __name__ == "__main__":
  app.run()
