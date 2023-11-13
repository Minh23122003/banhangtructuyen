from app.models import Category, Product
from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name="Quản trị bán hàng", template_mode='bootstrap4')

class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['id', 'name', 'products']

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))