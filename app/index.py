from flask import render_template, request
import dao
from app import app,models


@app.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    prods = dao.get_products(kw)
    return render_template('index.html', categories=cates, products=prods)

def load_user(user_id):
    return dao.ge

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
