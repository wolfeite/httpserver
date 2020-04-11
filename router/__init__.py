def register_route(app):
    from app.web import web
    app.register_blueprint(web)



