# api/__init__.py
from wsgi import application

def handler(event, context):
    print(event, context)
    return application
