from libs.request import Params
def add_route(bp, request, make_response, render_template, redirect, app, flash):
    @bp.route("/input")
    def input():
        with Params(request, ["branches", "leaves"]) as res:
            pass
        return render_template("templates/form.html")

    @bp.route("/other")
    def other():
        with Params(request, ["branches", "leaves"]) as res:
            pass
        return render_template("templates/jsTable.html")