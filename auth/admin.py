from flask_admin.contrib.sqla import ModelView

from config.database import db
from config.settings import admin
from .models import User


admin.add_view(ModelView(User, db.session, name="users",
               menu_icon_type="fa", menu_icon_value="fa-users"))
