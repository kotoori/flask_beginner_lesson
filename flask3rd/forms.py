from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

#フォームクラスを定義する
class ContactForm(FlaskForm): #FlaskFormを継承する
  #name:1行テキストフィールド（入力必須、2文字以上50文字以下）
  name = StringField('Name', validators=[DataRequired(),Length(min=2,max=50)])

  #email:1行テキストフィールド（入力必須、email形式）
  email = StringField('Email', validators=[DataRequired(),Email()])

  #subject:1行テキストフィールド（入力必須、100文字以下）
  subject = StringField('Subject', validators=[DataRequired(),Length(max=100)])

  #message:テキストエリア（入力必須、10文字以上500文字以下）
  message = TextAreaField('Message', validators=[DataRequired(),Length(min=10,max=500)])

  #submit:送信ボタン
  submit = SubmitField('Send')