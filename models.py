from run import db
from flask_login import UserMixin

class Service(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    service_title=db.Column(db.String(100))
    service_desc=db.Column(db.String(100))
    service_icon=db.Column(db.String(50))

class Testimotional(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    testimotional_content=db.Column(db.String(100))
    testimotional_writer=db.Column(db.String(100))
    writer_img=db.Column(db.String(100))

class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education_year=db.Column(db.String(100))
    education_place=db.Column(db.String(100))
    education_title=db.Column(db.String(100))
    education_desc=db.Column(db.String(100))

class Experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    experience_year=db.Column(db.String(100))
    experience_place=db.Column(db.String(100))
    experience_title=db.Column(db.String(100))
    experience_desc=db.Column(db.String(100))

class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_img=db.Column(db.String(100))
    portfolio_name=db.Column(db.String(100))
    portfolio_link=db.Column(db.String(100))

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_img=db.Column(db.String(100))
    blog_name=db.Column(db.String(100))
    blog_link=db.Column(db.String(100))

class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_img=db.Column(db.String(100))

class Social(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    social_name=db.Column(db.String(100))
    social_link=db.Column(db.String(100))

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    mail_name=db.Column(db.String(100))
    mail_message=db.Column(db.String(100))
    mail_address=db.Column(db.String(100))

class User(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
    loginStatus=db.Column(db.Boolean)
