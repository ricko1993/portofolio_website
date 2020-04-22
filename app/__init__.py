from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# sakrij kredencijale u env var...
app.config['MAIL_USERNAME'] = 'mijatovski@gmail.com'
app.config['MAIL_PASSWORD'] = 'qsvmyyttlsoiuvre'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# takodje i secret key...
app.config['SECRET_KEY'] = 'drowssap'

mail = Mail(app)

if __name__=='__main__':
    app.run()

from app import routes