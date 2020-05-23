from flask import Flask, render_template, request, abort
from router import register_route
from libs.IO import Path
from libs.request import Params

def requester(request):
    with Params(request, ["name", "age", "sex"]) as res:
        request.role = res
        print(">>>>>requester:", request.path, request.role.params["name"], res)

def create_app():
    app = Flask("/", template_folder="appData/view", static_folder="appData/statics")
    app.config.from_object("appData.config.secure")
    app.config.from_object("appData.config.setting")
    p = Path()
    p.set_path_base(app.config["APPDATA"])
    p.set_path_json("json")
    app.config["path"] = p.path
    app.add_template_global(app.config["ASIDE"], 'aside')
    # print("app.config>>>>json:", app.config["path"]["json"])
    # print("app.config>>>>base:", app.config["path"]["base"])
    @app.before_request
    def auther():
        if request.path == "/favicon.ico":
            abort(200)
        if request.path == "/login":
            return None
            print("登入页")
        print("app请求前置处理器auther:》》》》", request.path)
        return None

    @app.before_request
    def params():
        requester(request)
        print("app请求前置处理器》》》》params:", request.path)
        return None

    @app.after_request
    def excp(res):
        print("《《《《app请求结果处理器", res)
        return res
    register_route(app)

    @app.errorhandler(404)
    def error_404(error_info):
        return render_template("templates/error.html", error=error_info)

    @app.errorhandler(Exception)
    def error_500(error):
        """这个handler可以catch住所有的abort(500)和raise exeception."""
        response = dict(status=0, message="500 Error")
        return render_template("templates/error.html", error=error)

    return app
