from flask import Blueprint, request, render_template, redirect, flash, current_app as app, make_response, abort
import os, sys
print(">>>>>>", __name__, __path__, __file__, __doc__, __package__, os.sep, sys.argv[0])
# 1.定义蓝图
web = Blueprint("web", __name__, url_prefix="/")
@web.before_app_request
def auther():
    print("web模块请求前置处理器》》》》")
    # 各个模块权限判断
    pass

@web.after_app_request
def excp(res):
    print("《《《《web模块请求结果处理器", res)
    return res
# 2.为蓝图添加路由
# from app.web import test_route
test = __import__(__name__ + ".test_route", fromlist=('test_route'))
test.add_route(web, request, make_response, render_template, redirect, app, flash)
index = __import__(__name__ + ".index", fromlist="index")
index.add_route(web, request, make_response, render_template, redirect, app, flash)

#2.table蓝图
tableView = Blueprint("table", __name__, url_prefix="/table")
__import__(__name__ + ".table", fromlist="table").add_route(tableView, request, make_response, render_template, redirect, app, flash)

#3.form蓝图
formView = Blueprint("form", __name__, url_prefix="/form")
__import__(__name__ + ".form", fromlist="form").add_route(formView, request, make_response, render_template, redirect, app, flash)