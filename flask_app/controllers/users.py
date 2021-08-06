from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html', users = User.get_all_users())

@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "handle": request.form['handle'],
        "birthday": request.form['birthday']
    }
    # Calling the create_user class method and passing data
    User.create_user(data)

    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        "id":id
    }

    return render_template('edit.html', user=User.get_user(data))

@app.route ('/user/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        "id": id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "handle": request.form['handle'],
        "birthday": request.form['birthday']
    }
    User.update_user(data)
    return redirect('/')
