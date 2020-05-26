from libs.request import Params
def add_route(bp, request, make_response, render_template, redirect, app, flash):
    @bp.route("/input")
    def input():
        print("input 参数》》",request.role.params)
        return render_template("templates/form.html")

    @bp.route("/other")
    def other():
        print("other 参数》》",request.role.params)
        return render_template("templates/jsTable.html")