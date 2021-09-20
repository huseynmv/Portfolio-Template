#app routes

# from models import Blog
from run import app
from flask import render_template,request,url_for


@app.route("/")
def app_index():
    from models import Service,Testimotional
    services=Service.query.all()
    testimotionals=Testimotional.query.all()
    return render_template('app/index.html', services=services, testimotionals=testimotionals)

@app.route("/resume")
def app_about():
    from models import Education,Experience,Skill
    education=Education.query.all()
    experience=Experience.query.all()
    # social=Social.query.all()
    skill=Skill.query.all()
    return render_template("app/resume.html",education=education, experience=experience, skill=skill)

@app.route("/portfolio")
def app_portfolio():
    from models import Portfolio
    work=Portfolio.query.all()
    return render_template("app/portfolio.html", work=work)

@app.route("/blog")
def app_blog():
    from models import Blog
    blog=Blog.query.all()
    return render_template("app/blog.html", blog=blog)

@app.route("/contact")
def app_contact():
    return render_template("app/contact.html")