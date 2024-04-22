import os

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder='../react-app/build', static_url_path='', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    CORS(app)

    socketio.init_app(app, cors_allowed_origins="*")  # for development

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # The instance folder is a Flask convention for storing instance-specific data
    # (like a local database file, configuration files that shouldn't be committed to version control, etc.).
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import audio_streaming
    app.register_blueprint(audio_streaming.bp)
    from . import user_interface
    app.register_blueprint(user_interface.bp)
    from . import riva_interaction
    app.register_blueprint(riva_interaction.bp)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        if path != "" and os.path.exists(app.static_folder + '/' + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')

    return app
