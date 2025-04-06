import os
from flask_admin import Admin
from models import db, Users,Planets,Films,People,Favorites
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm.properties import RelationshipProperty

class AdminView(ModelView):
    def __init__(self, model, *args, **kwargs):
        self.column_list = [c.key for c in model.__table__.columns]
        for attr_name, attr in model.__mapper__.attrs.items():
            if isinstance(attr, RelationshipProperty):
                self.column_list.append(attr_name)
        self.form_excluded_columns = ["ID"]
        self.form_columns = [col for col in self.column_list if col != "ID"]
        super().__init__(model, *args, **kwargs)

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin

    admin.add_view(AdminView(Users, db.session))
    admin.add_view(AdminView(Planets, db.session))
    admin.add_view(AdminView(Films, db.session))
    admin.add_view(AdminView(People, db.session))
    admin.add_view(AdminView(Favorites, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))