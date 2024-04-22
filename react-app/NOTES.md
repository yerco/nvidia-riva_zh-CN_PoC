# Developing Notes

## While developing
```
$ npm start
```

## Proxy API Requests to Flask
Check .env file for the proxy settings.

## Build and Integrate with Flask for Poduction
```
$ npm run build
$ cp -r build/* ../myapp/user_interface/static
```

!!! TODO In MAC do not use localhost but 127.0.0.1

Timeout used for socketio is default