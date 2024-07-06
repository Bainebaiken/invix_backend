from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from invix_app.extensions import db

class Content(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    user = db.relationship('User', backref='contents')
    article = db.relationship('Article', back_populates='content')
    posts = db.relationship('Posts', backref='content')

    def __init__(self, name, description, user_id, article_id, slug, category):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.article_id = article_id
        self.slug = slug
        self.category = category

    def __repr__(self):
        return f'<Content {self.name}>'


# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from invix_app.extensions import db

# class Content(db.Model):
#     __tablename__ = "content"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False, unique=True)
#     description = db.Column(db.String(100), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)
#     slug = db.Column(db.String(100), nullable=False)
#     category = db.Column(db.String(100), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

#     user = db.relationship('User', backref='contents')
#     article = db.relationship('Article', back_populates='content')
#     sports = db.relationship('Sports', backref='content')
#     business = db.relationship('Business', backref='content')
#     education = db.relationship('Education', backref='content')
#     adverts = db.relationship('Adverts', backref='content')
#     general = db.relationship('General', backref='content')
#     posts = db.relationship('Posts', backref='content')

#     def __init__(self, name, description, user_id, article_id, slug, category):
#         self.name = name
#         self.description = description
#         self.user_id = user_id
#         self.article_id = article_id
#         self.slug = slug
#         self.category = category

#     def __repr__(self):
#         return f'<Content {self.name}>'

# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from invix_app.extensions import db

# class Content(db.Model):
#     __tablename__ = "content"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False, unique=True)
#     description = db.Column(db.String(100), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     article = db.Column(db.String(100),ForeignKey("article") nullable=False)
#     slug = db.Column(db.String(100), nullable=False)
#     category = db.Column(db.String(100), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

#     user = db.relationship('User', backref='contents')
#     technology = db.relationship('Technology', backref='content')
#     sports = db.relationship('Sports', backref='content')
#     business = db.relationship('Business', backref='content')
#     accidents = db.relationship('Accidents', backref='content')
#     education = db.relationship('Education', backref='content')
#     adverts = db.relationship('Adverts', backref='content')
#     general = db.relationship('General', backref='content')
#     posts = db.relationship('Posts', backref='content')


#     def __init__(self, id,name, description,user_id,article,slug,category):
#         self.id = id 
#         self.name = name
#         self.description =description
#         self.user_id = user_id
#         self. article = article
#         self.slug = slug
#         self.category =category

#     def __repr__(self):
#         return f'<Content {self.name}>'

