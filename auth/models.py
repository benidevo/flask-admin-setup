from flask_login import UserMixin
from config.database import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean())
    verified = db.Column(db.Boolean())

    def __str__(self):
        return f"{self.username}"
    
    # # Flask-Login integration
    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return self.id

    # # Required for administrative interface
    # def __unicode__(self):
    #     return self.username

    def save(self):
        db.session.add(self)
        db.session.commit()