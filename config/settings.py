import os
from flask import Flask, g, url_for, request, redirect, flash
from flask_admin import Admin, AdminIndexView, expose
from flask_migrate import Migrate
from flask_login import LoginManager, current_user


from auth.models import User
from config.database import db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    app = Flask(__name__, static_url_path='/static')
    secret = "jh876867g66236990990909%16777#ff992n623TG33fg545455"
    app.config['JWT_SECRET_KEY'] = secret
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    app.config['SECRET_KEY'] = secret
    app.config['REFRESH_EXP_LENGTH'] = 30
    app.config["ACCESS_EXP_LENGTH"] = 10
    app.config['JWT_SECRET_KEY'] = "Bearer"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
        os.path.join(BASE_DIR, "db.sqlite")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['DEBUG'] = True
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    db.init_app(app)
    return app
app = create_app()


# auth = GraphQLAuth(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

migrate = Migrate(app, db)


@app.before_request
def before_req():
    g.user = current_user
    


@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if g.user.is_authenticated:
            if g.user.is_admin:
                return super(MyAdminIndexView, self).index()
        next_url = request.endpoint
        login_url = '%s?next=%s' % (url_for('login'), next_url)
        flash('Please login as admin  first...', 'error')
        return redirect(login_url)


admin = Admin(app, name='eshop', template_mode='bootstrap4', index_view=MyAdminIndexView(
    name="Dashboard", menu_icon_type="fa", menu_icon_value="fa-dashboard"
))


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db.remove()
