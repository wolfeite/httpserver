from libs.request import Params
def add_route(web, request, make_response, render_template, redirect, app, flash):
    @web.route("/index")
    def index():
        with Params(request, ["branches", "leaves"]) as res:
            pass
        print(">>>", app.config["ASIDE"])
        headers = {
            # 默认为 text/html
            # 'content-type':'text/plain utf-8',
            'content-type': 'application/json',  # 以接口JSON数据方式响应浏览器
            'location': 'http://www.bing.com'
        }
        return render_template("templates/error.html", error=res.result) if res.result["error"] else render_template(
            "templates/index.html")
