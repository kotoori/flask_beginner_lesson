from forms import ContactForm #forms.pyをインポート
from flask import Flask, request, render_template, flash, session

app = Flask(__name__)
app.secret_key = 'a0hHbnEEF6P04GnaQ8ErTo61GbHA' #暗号化に利用する値（秘密鍵）

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm() #ContactFormクラスのインスタンスを作成
  username = session.get('username') #ユーザー名をセッションから取得する

  if form.validate_on_submit():
    flash('正しくデータが送信できました','success')
    session['username'] = form.name.data
    return render_template('contact.html', form=form, username=form.name.data)

  return render_template('contact.html', form=form,username=username)



if __name__ == "__main__":
  app.run()