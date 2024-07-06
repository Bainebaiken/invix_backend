from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from invix_app.extensions import db

class Article(db.Model):
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=True)
    video = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)

    category = db.relationship('Category', back_populates='articles')
    content = db.relationship('Content', back_populates='article')

    def __init__(self, text, video, image=None, category_id=None, content_id=None):
        self.text = text
        self.video = video
        self.image = image
        self.category_id = category_id
        self.content_id = content_id

    def __repr__(self):
        return f'<Article {self.text}>'

# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from invix_app.extensions import db

# class Article(db.Model):
#     __tablename__ = "article"

#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(50), nullable=False, unique=True)
#     image = db.Column(db.String(255), nullable=True)
#     video = db.Column(db.String(100), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

#     category = db.relationship('Category', back_populates='articles')

#     def __init__(self, text, video, image=None, category_id=None):
#         self.text = text
#         self.video = video
#         self.image = image
#         self.category_id = category_id

#     def __repr__(self):
#         return f'<Article {self.text}>'



# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from invix_app.extensions import db

# class Article(db.Model):
#     __tablename__ = "article"

#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(50), nullable=False, unique=True)
#     image = db.Column(db.String(255), nullable=True)
#     video = db.Column(db.String(100), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
#     content = db.relationship('Content', back_populates='article')

#     category = db.relationship('Category', back_populates='articles')

#     def __init__(self, text, video, image=None, category_id=None):
#         self.text = text
#         self.video = video
#         self.image = image
#         self.category_id = category_id

#     def __repr__(self):
#         return f'<Article {self.text}>'

# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from invix_app.extensions import db

# from invix_app.extensions import db

# class Article(db.Model):
#     __tablename__ = "artical"

#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(50), nullable=False, unique=True)
#     image = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=True)
#     video = db.Column(db.String(100), nullable=False)
    
#     def __init__(self, text, video, image=None):
#         self.text = text
#         self.video = video
#         self.image = image

#     def __repr__(self):
#         return f'<Artical {self.text}>'