from flask import Flask, render_template
from project_gym.client_dao import ClientDAO

app = Flask(__name__)

app_title = 'Gym Admin'


@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html')  # url: http://localhost:5000/index.html
def index():
    app.logger.debug('index() called')
    # Get clients from database
    clients_db = ClientDAO.select()

    return render_template('index.html', title=app_title,
                           clients=clients_db)


if __name__ == '__main__':
    app.run(debug=True)
