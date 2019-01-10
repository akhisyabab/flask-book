from . import app

from app.home.views import home_blueprint
from app.users.views import users_blueprint
from app.members.views import members_blueprint
from app.my_api.views import api_blueprint

# register the blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(api_blueprint)
