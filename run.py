from re import DEBUG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user

app=Flask(__name__)
app.secret_key = b'_4#y2L"F4Q8z\n\xec]/'
bc = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'userasd098@gmail.com'
app.config['MAIL_PASSWORD'] = ' yusif!@#123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
mail = Mail(app)
db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="admin_index"
from models import *
migrate = Migrate(app, db)

#app routes

from app.routes import *

#admin routes

from admin.routes import *

if __name__=="__main__":
    app.run(debug=True)