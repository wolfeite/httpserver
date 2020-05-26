from flask import Flask, Blueprint, request, render_template, redirect, current_app, flash, make_response, abort
import time
class FlaskServer():
    kwArgs = {
        "request": request,
        "render_template": render_template,
        "redirect": redirect,
        "current_app": current_app,
        "flash": flash,
        "make_response": make_response
        , "abort": abort
    }

    args = [request, make_response, render_template, redirect, current_app, flash]
    def __init__(self, root, **config):
        print("???<>", root, config)
        # "/", template_folder="appData/view", static_folder="appData/statics"
        self.app = Flask(root, **config)
        self.bps = {}

    def register_filter(self, filter):
        print(FlaskServer.kwArgs)
        # filter(self.app)
        filter(self.app, **FlaskServer.kwArgs)

    def register_router(self, name, position, addRoute, **config):
        # "bg", __name__, url_prefix="/bg"
        has = name in self.bps
        bp = Blueprint(name, position, **config) if not has else self.bps[name]
        addRoute(bp, **FlaskServer.kwArgs)
        # addRoute(bp, *FlaskServer.args)
        self.bps[name] = bp
        not has and self.app.register_blueprint(bp)

    @property
    def config(self):
        return self.app.config

    @config.setter
    def config(self, args=()):
        args = (args) if isinstance(args, str) else args
        for path in args:
            self.app.config.from_object(path)

    @property
    def attr(self):
        return FlaskServer.kwArgs

    @attr.setter
    def attr(self, args=()):
        key, val = args[0], args[1]
        FlaskServer.kwArgs[key] = val

    # def addRoute(self, name, fn):
    #     fn(self.bps[name], **FlaskApp.kwArgs)

    def run(self, **kwargs):
        # host="0.0.0.0", debug=app.config["DEBUG"], port=app.config["PORT"]
        self.app.run(**kwargs)
