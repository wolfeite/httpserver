from libs.request import Params
def add_route(bp, request, make_response, render_template, redirect, app, flash):
    @bp.route("/data")
    def dataTable():
        with Params(request, ["branches", "leaves"]) as res:
            pass
        return render_template("templates/dataTable.html")

    @bp.route("/js")
    def jsTable():
        with Params(request, ["branches", "leaves"]) as res:
            pass
        return render_template("templates/jsTable.html")