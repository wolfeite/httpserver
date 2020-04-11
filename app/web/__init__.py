from flask import Blueprint
web = Blueprint("web", __name__)
# import os ,sys
# print(">>>>>>",__name__,__path__,__file__,__doc__,__package__,os.sep,sys.argv[0])
__import__(__name__ + ".test_route")
# from app.web import test_route
