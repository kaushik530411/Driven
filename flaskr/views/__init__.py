from flask import Blueprint
from flaskr.views import index
from flaskr.views import users
from flaskr.views import address

blueprint = Blueprint('views', __name__)
index.views(blueprint)
users.views(blueprint)
address.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')
