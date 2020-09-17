from flask_blog import db

class Profile(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=False)
    country = db.Column(db.String(30),unique=False)
    email = db.Column(db.String(30),unique=False)
    hobbies = db.Column(db.String(500),unique=False)

    def __repr__(self):
        return f"This is the profile of {self.name}"
