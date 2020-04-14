import sys
import json
import os

class Path():
    def __init__(self):
        self.path = {"sep": os.sep}
        self.set_path_root()

    def set_path_root(self):
        pathArr = sys.argv[0].split(self.path["sep"])
        self.path["enter"] = pathArr.pop()
        self.path["root"] = "{}{}".format(self.path["sep"].join(pathArr), self.path["sep"])

    def set_path_base(self, dir):
        self.set_path("base", dir)

    def set_path_json(self, dir):
        self.set_path("json", dir, self.path["base"])

    def set_path(self, name, dir, root=""):
        path = self.path
        root = root or path["root"]
        self.path[name] = "{1}{2}{0}".format(path["sep"], root, dir)


class Json():
    def __init__(self, url):
        self.url = url
        pass
    def read(self):
        pass
    def write(self):
        pass
    def __enter__(self):

        pass
    def __exit__(self):
        pass

class upFile():
    pass
