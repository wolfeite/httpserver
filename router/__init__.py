def register_route(app):
    from app.web import web, tableView, formView
    app.register_blueprint(web)
    app.register_blueprint(tableView)
    app.register_blueprint(formView)
