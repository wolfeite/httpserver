def register_route(app):
    from app.web import bps
    for bp in bps:
        app.register_blueprint(bp)

