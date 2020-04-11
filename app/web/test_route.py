from . import web
from flask import render_template, request
@web.route("/test")
def test():
    print("method:", request.method)
    # return render_template("templates/layout.html")
    return render_template("templates/dataTable.html")
