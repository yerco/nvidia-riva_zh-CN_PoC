from flask import Blueprint

from myapp.riva_interaction import routes
from myapp import socketio
from myapp.riva_interaction.st_factory import create_st

bp = Blueprint('riva_interaction', __name__, template_folder='templates')

speech_translator = create_st(1, socketio)
