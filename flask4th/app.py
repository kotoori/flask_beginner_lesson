from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.instance_path, 'items.db') #どこにDBがあるかパス指定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #データベースの変更追跡はfalse
db = SQLAlchemy(app) #DBを使える状態にする

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True) #整数値の主キー
  name = db.Column(db.String(50), nullable=False) #Null許容なしの文字列
  category = db.Column(db.String(50), nullable=False) #Null許容なしの文字列
  price = db.Column(db.Integer, nullable=False) #Null許容なしの整数値

@app.route('/items')
def get_items():
  items = Item.query.all() #DBからすべてのアイテムを取得
  return render_template('items.html', items=items)

@app.route('/items/<int:item_id>')
def get_item(item_id):
  item = Item.query.get_or_404(item_id) #idをキーにして取得する
  return render_template('item.html', item=item)

@app.route('/items/add',methods=['GET', 'POST'])
def add_item():
  if request.method == 'POST':
    name = request.form['name']
    category = request.form['category']
    price = int(request.form['price'])
    new_item = Item(name=name, category=category, price=price)
    db.session.add(new_item)#データを挿入
    db.session.commit() #コミットして確定する
    return redirect(url_for('get_items')) #itemsページにリダイレクトする
  return render_template('add_item.html') #登録用のフォームを表示する

@app.route('/items/update/<int:item_id>', methods=['GET', 'POST']) #データの更新
def update_item(item_id):
  item = Item.query.get_or_404(item_id) #idをキーにして取得する
  if request.method == 'POST':
    item.price = int(request.form['price']) #データを置き換える
    db.session.commit() #コミットして確定する
    return redirect(url_for('get_items', item_id=item_id)) #itemページにリダイレクトする
  return render_template('update_item.html', item=item) #更新用のフォームを表示する

@app.route('/items/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
  item = Item.query.get_or_404(item_id) #idをキーにして取得する
  db.session.delete(item) #データを削除する
  db.session.commit() #コミットして確定する
  return redirect(url_for('get_items')) #itemsページにリダイレクトする



def initialize_database():
  #instanceフォルダを作る
  os.makedirs(app.instance_path, exist_ok=True)

  db_path = os.path.join(app.instance_path, 'items.db')
  if not os.path.exists(db_path): #パスが存在しなかったら（=データベースが存在しなかったら）
    with app.app_context():
      db.create_all() #テーブルが作成される
      print("テーブルが作成されました")

      initial_items = [
        {'name': 'リンゴ', 'category': '果物', 'price': 300},
        {'name': 'トマト', 'category': '野菜', 'price': 200},
        {'name': '鮭', 'category': '魚', 'price': 400}
      ]

      for val in initial_items:
        db.session.add(Item(name=val['name'], category=val['category'], price=val['price'])) #初期データを挿入
      db.session.commit() #コミットして確定する
      print("データベースにデータを格納した")
  else:
    print("すでにデータベースが存在します")

if __name__ == "__main__":
  initialize_database()
  app.run()
