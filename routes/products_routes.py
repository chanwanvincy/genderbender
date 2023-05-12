from flask import Blueprint
from controllers.products_controller import index, new, create, edit, update, delete, reviews, post_review, edit_review, update_review, remove_review, suggest, add_suggest

products_routes = Blueprint('products_routes', __name__)

products_routes.route('')(index)
products_routes.route('/new')(new)
products_routes.route('', methods=["POST"])(create)
products_routes.route('/<id>/edit')(edit)
products_routes.route('/<id>', methods = ["POST"])(update)
products_routes.route('/<id>/delete', methods=["POST"])(delete)
products_routes.route('/<id>/reviews')(reviews)
products_routes.route('/<id>/reviews/post', methods = ["POST"])(post_review)
products_routes.route('/<id>/edit_review')(edit_review)
products_routes.route('/<id>/update_review', methods=["POST"])(update_review)
products_routes.route('/<id>/delete_review', methods=["POST"])(remove_review)
products_routes.route('/suggest')(suggest)
products_routes.route('/suggest/post', methods=["POST"])(add_suggest)
