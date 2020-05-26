
from .routes import form, index, table, test_route, filter

def config_app(app):
    app.config = ("app.config.secure", "app.config.setting")
    app.app.add_template_global(app.config["ASIDE"], 'aside')
    app.register_filter(filter.filter)
    app.register_router("web", __name__, index.add_route)
    # app.register_router("web", __name__, test_route.add_route)
    # app.register_router("table", __name__, form.add_route, url_prefix="/table")
    # app.register_router("form", __name__, table.add_route, url_prefix="/form")
