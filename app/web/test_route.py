# from . import web
# from flask import render_template, request
from libs.request import Params
def open():
    print("ok")
def add_route(web, request, make_response, render_template, redirect, app, flash):
    @web.route("/test")
    def test():
        print("method:", request.method)
        # return render_template("templates/layout.html")
        # return render_template("templates/dataTable.html")
        print(app.config["PORT"])
        return render_template("templates/dataTable.html")

    @web.route("/width", methods=["get", "post"])
    def width():
        with Params(request, ["name", "age", "sex"]) as res:
            print(">>>>>isGet:", res.isGet)
            # 1 / 0

        return render_template("templates/error.html", error=res.result) if res.result["error"] else render_template(
            "templates/index.html")
