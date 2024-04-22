from flask import Blueprint

bp = Blueprint('audio_streaming', __name__, template_folder='templates')

from myapp.audio_streaming import routes
