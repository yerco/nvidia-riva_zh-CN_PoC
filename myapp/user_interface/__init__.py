from flask import Blueprint

bp = Blueprint('user_interface', __name__)

from myapp.user_interface import routes
