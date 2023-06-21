from flask import render_template, redirect, request, session
from flask_app.model.user_model import Users


from flask_app import app







@app.route('/')
def newUsers():
    return redirect ('/users')


@app.route('/users')
def users():
    return render_template('users.html', users=Users.get_all())

@app.route('/users/new')
def new():
    return render_template('new_users.html')


@app.route('/users/added', methods=['POST'])
def add():
    print("Got Post Info")
    Users.save(request.form)
    
    # data = {
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     'email': request.form['email']
    # }
    # Users.save(data)
    return redirect('/users')


@app.route("/users/edit/<int:id>")
def edit(id):
    print('edited user')
    users = Users.get_one({ "id" : id })
    return render_template("edit_user.html", users = users)

@app.route('/users/update', methods=['POST'])
def update():
    Users.update(request.form)
    return redirect ('/users')

@app.route("/users/show/<int:id>")
def show(id):
    print('showUser')
    users = Users.get_one({ "id" : id })
    return render_template ('show_user.html', users = users)



@app.route("/users/delete/<int:id>")
def delete(id):
    users = Users.delete({ "id" : id })
    return redirect ('/users')








