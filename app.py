"""
This is the main file of the project. It contains the Flask application
and the route to the index page.

Daniel Zapata - 2024
"""

from flask import Flask, render_template, redirect, url_for
from project_gym.form_client import ClientForm
from project_gym.client_dao import ClientDAO
from project_gym.client_cls import Client

app = Flask(__name__)

app_title = 'Gym Admin'
app.config['SECRET_KEY'] = 'mysecret'  # Secret key for CSRF protection (obviously, change this value)


@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html')  # url: http://localhost:5000/index.html
def index():
    app.logger.debug('index() called')
    # Get clients from database
    clients_db = ClientDAO.select()

    # Create an empty client object
    client = Client()
    form_client = ClientForm(obj=client)

    return render_template('index.html', title=app_title,
                           clients=clients_db, form=form_client)


@app.route('/save', methods=['POST'])  # url: http://localhost:5000/save
def save():
    app.logger.debug('save() called')
    client = Client()
    form = ClientForm(obj=client)
    if form.validate_on_submit():
        # Populate the client object with the form data
        form.populate_obj(client)
        if client.id:
            # If the client has an id, update it
            ClientDAO.update(client)
        else:
            ClientDAO.insert(client)
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET'])  # url: http://localhost:5000/edit/1
def edit(id):
    app.logger.debug('edit() called')
    client = ClientDAO.select_by_id(id)
    form = ClientForm(obj=client)
    clients_db = ClientDAO.select()
    return render_template('index.html', title=app_title, form=form, clients=clients_db)


@app.route('/delete/<int:id>', methods=['GET'])  # url: http://localhost:5000/delete/1
def delete(id):
    print(id)
    app.logger.debug('delete() called')
    client = ClientDAO.select_by_id(id)
    ClientDAO.delete(client)
    return redirect(url_for('index'))


@app.route('/clear')  # url: http://localhost:5000/clear
def clear():
    app.logger.debug('clear() called')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
