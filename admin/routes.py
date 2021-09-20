#admin routes

from werkzeug.utils import redirect
from run import app,db,bc
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager
from flask import render_template,request,url_for
import os
#login

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(user_id)

@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for("admin_index"))

@app.route("/admin", methods=["GET", "POST"])
def admin_index():
    from models import User
    from run import db
    login = User(
        username = "huseynn",
        password = "salam!@#123",
        loginStatus=False
    )
    db.session.add(login)
    db.session.commit()
    if request.method=="POST":
        if login.username == request.form["username"] and login.password == request.form["password"]:
            login_user(login, remember=login.loginStatus)
            return redirect(url_for("admin_service"))
        else:
            return redirect(url_for("admin_index"))
    return render_template("admin/index.html", login=login)



@app.route("/admin/services", methods=['GET', 'POST'])
@login_required
def admin_service():
    from models import Service,User
    services=Service.query.all()
    if request.method=='POST':
        service=Service(
            service_title=request.form["service_title"],
            service_icon=request.form["service_icon"],
            service_desc=request.form["service_desc"]
        )
        db.session.add(service)
        db.session.commit()
        return redirect("/admin/services")
    return render_template('admin/service.html', services=services)

@app.route("/admin/services/delete/<int:id>")
@login_required
def admin_service_delete(id):
        from models import Service
        service=Service.query.filter_by(id=id).first()
        db.session.delete(service)
        db.session.commit()
        return redirect('/admin')

@app.route("/admin/services/update/<int:id>", methods=["GET", "POST"])
@login_required
def admin_service_update(id):
    from models import Service
    service=Service.query.filter_by(id=id).first()
    if request.method=="POST":
        service=Service.query.filter_by(id=id).first()
        service.service_title=request.form["service_title"]
        service.service_desc=request.form["service_desc"]
        service.service_icon=request.form["service_icon"]
        db.session.commit()
        return redirect('/admin')
    return render_template('admin/update.html', service=service)


@app.route("/admin/testimotionals", methods=['GET', 'POST'])
@login_required
def admin_testimotionals():
    from models import Testimotional
    testimotionals=Testimotional.query.all()
    if request.method=='POST':
        file=request.files['writer_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        testimotional=Testimotional(
            testimotional_content=request.form["testimotional_content"],
            testimotional_writer=request.form["testimotional_writer"],
            writer_img=filename
        )
        db.session.add(testimotional)
        db.session.commit()
        return redirect('/admin/testimotionals')
    return render_template('admin/testimotionals.html', testimotionals=testimotionals)

@app.route("/admin/testimotional/delete/<int:id>")
@login_required
def admin_testimotionals_delete(id):
        from models import Testimotional
        user=Testimotional.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return redirect('/admin/testimotionals')

@app.route("/admin/testimotional/update/<int:id>", methods=["GET", "POST"])
@login_required
def admin_feedback_update(id):
    from models import Testimotional
    feedback=Testimotional.query.filter_by(id=id).first()
    if request.method=="POST":
        feedback=Testimotional.query.filter_by(id=id).first()
        feedback.testimotional_content=request.form["testimotional_content"]
        feedback.testimotional_writer=request.form["testimotional_writer"]
        db.session.commit()
        return redirect('/admin/testimotionals')
    return render_template('admin/feedbackupdate.html',feedback=feedback)

@app.route("/admin/education", methods=["GET", "POST"])
@login_required
def admin_education():
    from models import Education
    education=Education.query.all()
    if request.method=='POST':
        education=Education(
            education_year=request.form["education_year"],
            education_place=request.form["education_place"],
            education_title=request.form["education_title"],
            education_desc=request.form["education_desc"]
        )
        db.session.add(education)
        db.session.commit()
        return redirect("/admin/education")
    return render_template('admin/education.html', education=education)

@app.route("/admin/education/delete/<int:id>")
@login_required
def admin_education_delete(id):
        from models import Education
        edu=Education.query.filter_by(id=id).first()
        db.session.delete(edu)
        db.session.commit()
        return redirect('/admin/education')

@app.route("/admin/education/update/<int:id>", methods=["GET", "POST"])
@login_required
def admin_education_update(id):
    from models import Education
    education=Education.query.filter_by(id=id).first()
    if request.method=="POST":
        education=Education.query.filter_by(id=id).first()
        education.education_year=request.form["education_year"]
        education.education_title=request.form["education_title"]
        education.education_desc=request.form["education_desc"]
        education.education_place=request.form["education_place"]
        db.session.commit()
        return redirect('/admin/education')
    return render_template('admin/educationupdate.html', education=education)

@app.route("/admin/experience", methods=["GET", "POST"])
@login_required
def admin_experience():
    from models import Experience
    experience=Experience.query.all()
    if request.method=='POST':
        experience=Experience(
            experience_year=request.form["experience_year"],
            experience_place=request.form["experience_place"],
            experience_title=request.form["experience_title"],
            experience_desc=request.form["experience_desc"]
        )
        db.session.add(experience)
        db.session.commit()
        return redirect("/admin/experience")
    return render_template('admin/experience.html', experience=experience)

@app.route("/admin/experience/delete/<int:id>")
@login_required
def admin_experience_delete(id):
        from models import Experience
        exp=Experience.query.filter_by(id=id).first()
        db.session.delete(exp)
        db.session.commit()
        return redirect('/admin/experience')

@app.route("/admin/experience/update/<int:id>", methods=["GET", "POST"])
@login_required
def admin_experience_update(id):
    from models import Experience
    experience=Experience.query.filter_by(id=id).first()
    if request.method=="POST":
        experience=Experience.query.filter_by(id=id).first()
        experience.experience_year=request.form["experience_year"]
        experience.experience_title=request.form["experience_title"]
        experience.experience_desc=request.form["experience_desc"]
        experience.experience_place=request.form["experience_place"]
        db.session.commit()
        return redirect('/admin/experience')
    return render_template('admin/experienceupdate.html',experience=experience)

@app.route("/admin/portfolio", methods=["GET", "POST"])
@login_required
def admin_portfolio():
    from models import Portfolio
    work=Portfolio.query.all()
    if request.method=='POST':
        file=request.files['work_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        work=Portfolio(
            portfolio_name=request.form["work_name"],
            portfolio_img=filename,
            portfolio_link=request.form["work_link"]
        )
        db.session.add(work)
        db.session.commit()
        return redirect("/admin/portfolio")
    return render_template('admin/portfolio.html', work=work)

@app.route("/admin/portfolio/delete/<int:id>")
@login_required
def admin_work_delete(id):
        from models import Portfolio
        work=Portfolio.query.filter_by(id=id).first()
        db.session.delete(work)
        db.session.commit()
        return redirect('/admin/portfolio')

@app.route("/admin/portfolio/update/<int:id>", methods=["GET", "POST"])
@login_required
def admin_portfolio_update(id):
    from models import Portfolio
    work=Portfolio.query.filter_by(id=id).first()
    if request.method=="POST":
        work=Portfolio.query.filter_by(id=id).first()
        work.portfolio_name=request.form["portfolio_name"]
        work.portfolio_link=request.form["portfolio_link"]
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('admin/portfolioupdate.html', work=work)

@app.route("/admin/blog", methods=["GET", "POST"])
@login_required
def admin_blog():
    from models import Blog
    blog=Blog.query.all()
    if request.method=="POST":
        file=request.files['blog_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        blog=Blog(
            blog_name=request.form["blog_name"],
            blog_img=filename,
            blog_link=request.form["blog_link"]
        )
        db.session.add(blog)
        db.session.commit()
        return redirect("/admin/blog")
    return render_template("admin/blog.html", blog=blog)

@app.route("/admin/blog/delete/<int:id>")
@login_required
def admin_blog_delete(id):
        from models import Blog
        blog=Blog.query.filter_by(id=id).first()
        db.session.delete(blog)
        db.session.commit()
        return redirect('/admin/blog')

@app.route("/admin/blog/update/<int:id>", methods=["GET", "POST"])
@login_required
def admin_blog_update(id):
    from models import Blog
    blog=Blog.query.filter_by(id=id).first()
    if request.method=="POST":
        blog=Blog.query.filter_by(id=id).first()
        blog.blog_name=request.form["blog_name"]
        blog.blog_link=request.form["blog_link"]
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blogupdate.html', blog=blog)

@app.route("/admin/skill", methods=["GET","POST"])
@login_required
def admin_skill():
    from models import Skill
    skill=Skill.query.all()
    if request.method=="POST":
        file=request.files['skill_img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        skill=Skill(
            skill_img=filename
        )
        db.session.add(skill)
        db.session.commit()
        return redirect("/admin/skill")
    return render_template("admin/skill.html", skill=skill)

@app.route("/admin/skill/delete/<int:id>")
@login_required
def admin_skill_delete(id):
        from models import Skill
        skill=Skill.query.filter_by(id=id).first()
        db.session.delete(skill)
        db.session.commit()
        return redirect('/admin/skill')

@app.route("/admin/social", methods=["GET","POST"])
@login_required
def admin_social():
    from models import Social
    social=Social.query.all()
    if request.method=="POST":
        social=Social(
            social_name=request.form["social_name"],
            social_link=request.form["social_link"]
        )
        db.session.add(social)
        db.session.commit()
        return redirect("/admin/skill")
    return render_template("admin/skill.html")

@app.route("/admin/contact", methods=["GET", "POST"])
def admin_contact():
    from models import Contact
    from flask_mail import Mail,Message
    from run import mail
    messages=Contact.query.all()
    if request.method=="POST":
        mail_name=request.form["mail_name"]
        mail_adress=request.form["mail_address"]
        mail_message=request.form["mail_message"]
        salam=Contact(
            mail_name=mail_name,
            mail_message=mail_message,
            mail_address=mail_adress
        )
        msg=Message(mail_message, sender=mail_adress, recipients = ["userasd098@gmail.com"])
        mail.send(msg)
        db.session.add(salam)
        db.session.commit()
        return redirect("/")
    return render_template("admin/contact.html", messages=messages)