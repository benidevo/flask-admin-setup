from flask_admin.contrib.sqla import ModelView

from config.database import db
from config.settings import admin
from .models import User

class UserView(ModelView):
    column_exclude_list = ['password']
    column_searchable_list = ['username', 'email']

admin.add_view(UserView(User, db.session, name="users",
               menu_icon_type="fa", menu_icon_value="fa-users"))
