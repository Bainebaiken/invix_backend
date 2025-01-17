from datetime import datetime
from invix_app.extensions import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.Integer, unique=True)
    user_type = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=True)
    user_posts = db.relationship('Posts', backref='author', lazy=True)
    content = db.relationship('Content', backref='author', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, first_name, last_name, email, contact, password, user_type, biography=None, image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_type = user_type
        self.contact = contact  
        self.image = image  
        self.biography = biography 
        self.password = password

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


