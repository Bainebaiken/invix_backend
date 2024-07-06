from flask import Blueprint, jsonify, request
from datetime import datetime
from . import db  # Assuming db is your SQLAlchemy object
from invix_app.models import Content  # Assuming Content is your SQLAlchemy model

# Define a Blueprint for content-related routes
content_bp = Blueprint('content', __name__ ,url_prefix='/api/v1/content')



# Create a new content
@content_bp.route('/content', methods=['POST'])
def create_content():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    article_id = data.get('article_id')
    slug = data.get('slug')
    category = data.get('category')

    new_content = Content(name=name, description=description, article_id=article_id,
                          slug=slug, category=category)

    try:
        db.session.add(new_content)
        db.session.commit()
        return jsonify({'message': 'Content created successfully', 'id': new_content.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create content', 'error': str(e)}), 500

# Get all content
@content_bp.route('/content', methods=['GET'])
def get_all_content():
    try:
        contents = Content.query.all()
        content_list = []
        for content in contents:
            content_list.append({
                'id': content.id,
                'name': content.name,
                'description': content.description,
                'article_id': content.article_id,
                'slug': content.slug,
                'category': content.category,
                'created_at': content.created_at,
                'updated_at': content.updated_at
            })
        return jsonify(content_list), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve content', 'error': str(e)}), 500

# Get a single content by ID
@content_bp.route('/content/<int:id>', methods=['GET'])
def get_content(id):
    try:
        content = Content.query.get(id)
        if not content:
            return jsonify({'message': 'Content not found'}), 404

        return jsonify({
            'id': content.id,
            'name': content.name,
            'description': content.description,
            'article_id': content.article_id,
            'slug': content.slug,
            'category': content.category,
            'created_at': content.created_at,
            'updated_at': content.updated_at
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve content', 'error': str(e)}), 500

# Update a content by ID
@content_bp.route('/content/<int:id>', methods=['PUT'])
def update_content(id):
    data = request.get_json()
    try:
        content = Content.query.get(id)
        if not content:
            return jsonify({'message': 'Content not found'}), 404

        content.name = data.get('name', content.name)
        content.description = data.get('description', content.description)
        content.article_id = data.get('article_id', content.article_id)
        content.slug = data.get('slug', content.slug)
        content.category = data.get('category', content.category)
        content.updated_at = datetime.now()

        db.session.commit()
        return jsonify({'message': 'Content updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update content', 'error': str(e)}), 500

# Delete a content by ID
@content_bp.route('/content/<int:id>', methods=['DELETE'])
def delete_content(id):
    try:
        content = Content.query.get(id)
        if not content:
            return jsonify({'message': 'Content not found'}), 404

        db.session.delete(content)
        db.session.commit()
        return jsonify({'message': 'Content deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete content', 'error': str(e)}), 500

# Other custom routes or actions related to content can be added as needed
