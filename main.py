from myapp import create_app, socketio

app = create_app()

if __name__ == "__main__":
    print("Starting server")
    socketio.run(app, debug=True, port=5001, use_reloader=True)
