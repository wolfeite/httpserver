from flask import Blueprint, request, render_template, redirect, flash, current_app as app
# import os ,sys
# print(">>>>>>",__name__,__path__,__file__,__doc__,__package__,os.sep,sys.argv[0])
# 1.定义蓝图
web = Blueprint("web", __name__)
# 2.为蓝图添加路由
# from app.web import test_route
__import__(__name__ + ".test_route")
test_route.add_route(web, request, render_template, redirect, app, flash)
