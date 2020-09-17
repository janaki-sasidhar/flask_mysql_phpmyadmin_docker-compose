from flask import render_template  , redirect , url_for
from flask_blog import app , db
from flask_blog.forms import ProfileForm
from flask_blog.models import Profile

@app.route('/')
def home():
    title = {'title':'Home'}
    profile =  Profile.query.first()
    name = profile.name
    country = profile.country
    email = profile.email
    hobbies = profile.hobbies
    return render_template('index.html',title=title , name = name , country = country , email = email , hobbies = hobbies)

@app.route('/update',methods=['GET','POST'])
def update():
    form=ProfileForm()
    if form.validate_on_submit():
        if profile == Profile.query.first():
            profile.name = form.name.data
            profile.email = form.email.data
            profile.country = form.country.data
            profile.hobbies= form.hobbies.data
            db.session.add(profile)
            db.session.commit()
        else:
            name = form.name.data
            email = form.email.data
            country = form.country.data
            hobbies= form.hobbies.data
            profile = Profile(name=name,email=email,country=country,hobbies=hobbies)
            db.session.add(profile)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html',form=form , title='Update profile')
