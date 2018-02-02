import os
from livereload import Server


if __name__ == '__main__':
    server = Server()
    server.serve(root='/site/')
