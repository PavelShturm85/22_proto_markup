from jinja2 import Template
import json
import os
from livereload import Server


if __name__ == '__main__':
    server = Server()
    server.serve(root='')
