from flask import Blueprint, jsonify, request
from . import db  
from invix_app.models.article import Article  
from flask_jwt_extended import jwt_required
from functools import wraps
# Define a Blueprint for article-related routes
article_bp = Blueprint('article', __name__, url_prefix='/api/v1/articles')

# Admin required
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_info = get_jwt_identity()
        if user_info['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper

# Create a new article
@article_bp.route('/register', methods=['POST'])
def create_article():
    data = request.get_json()
    text = data.get('text')
    video = data.get('video')
    image = data.get('image')  # Optional field

    new_article = Article(text=text, video=video, image=image)

    try:
        db.session.add(new_article)
        db.session.commit()
        return jsonify({'message': 'Article created successfully', 'id': new_article.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create article', 'error': str(e)}), 500

# Get all articles
@article_bp.route('/', methods=['GET'])
def get_all_articles():
    try:
        articles = Article.query.all()
        article_list = []
        for article in articles:
            article_list.append({
                'id': article.id,
                'text': article.text,
                'video': article.video,
                'image': article.image
            })
        return jsonify(article_list), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve articles', 'error': str(e)}), 500

# Get a single article by ID
@article_bp.route('/<int:id>', methods=['GET'])
def get_article(id):
    try:
        article = Article.query.get(id)
        if not article:
            return jsonify({'message': 'Article not found'}), 404

        return jsonify({
            'id': article.id,
            'text': article.text,
            'video': article.video,
            'image': article.image
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve article', 'error': str(e)}), 500

# Update an article by ID
@article_bp.route('/<int:id>', methods=['PUT'])
def update_article(id):
    data = request.get_json()
    try:
        article = Article.query.get(id)
        if not article:
            return jsonify({'message': 'Article not found'}), 404

        article.text = data.get('text', article.text)
        article.video = data.get('video', article.video)
        article.image = data.get('image', article.image)

        db.session.commit()
        return jsonify({'message': 'Article updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update article', 'error': str(e)}), 500

# Delete an article by ID
@article_bp.route('/<int:id>', methods=['DELETE'])
@admin_required
def delete_article(id):
    try:
        article = Article.query.get(id)
        if not article:
            return jsonify({'message': 'Article not found'}), 404

        db.session.delete(article)
        db.session.commit()
        return jsonify({'message': 'Article deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete article', 'error': str(e)}), 500
