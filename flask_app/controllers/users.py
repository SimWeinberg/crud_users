from flask_app import app

from flask import Flask, render_template, request, redirect

from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", all_users = users)

@app.route('/users/new')
def new():
    return render_template('/users_new.html')

@app.route('/users/create', methods=["POST"])
def create():
        print(request.form)
        id = User.save(request.form)
        return redirect(f'/users/show/{id}')

@app.route('/users/show/<int:id>')
def show(id):
    data ={"id":id}
    user = User.get_one(data)
    return render_template("users_show.html", user = user)

@app.route('/users/update/<int:id>')
def update(id):
    data ={"id":id}
    return render_template("users_edit.html", user = User.get_one(data))

@app.route('/users/edit/<int:id>', methods=["POST"])
def edit(id):
    print(request.form)
    User.edit(request.form)
    return redirect(f'/users/show/{id}')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data ={"id":id}
    User.destroy(data)
    return redirect('/users')