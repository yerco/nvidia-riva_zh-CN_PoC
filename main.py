import ssl

from myapp import create_app, socketio

app = create_app()

if __name__ == "__main__":
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('cert.pem', 'key.pem')
    print("Starting server")
    socketio.run(app, debug=True, port=5001, use_reloader=True)
