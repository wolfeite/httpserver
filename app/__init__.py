from flask import Flask
from router import register_route
def create_app():
    app = Flask("/",template_folder="appData/view", static_folder="appData/statics")
    app.config.from_object("appData.config.secure")
    app.config.from_object("appData.config.secure")
    register_route(app)
    return app