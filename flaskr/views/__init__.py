from flask import Blueprint
from flaskr.views import index
from flaskr.views import users

blueprint = Blueprint('views', __name__)
index.views(blueprint)
users.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')
