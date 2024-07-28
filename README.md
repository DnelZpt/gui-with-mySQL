# Gym App

**Note:** This is an introductory project to Tkinter, MySQL, and Flask, aimed at demonstrating basic integration and functionality. It is not intended for production use.

Gym App is a graphical user interface (GUI) built using Python and Tkinter. The application allows users to manage client information, including adding, updating, and deleting client records. The client data is stored in a MySQL database, and the app includes features such as form validation, data display in a table, and user notifications.

Additionally, the project includes a web interface built with Flask and styled using Bootstrap. This web interface provides similar functionality to the desktop application, allowing users to manage client information through a web browser.

## Features

- Add new clients
- Update existing clients
- Delete clients
- Display client information in a table
- Form validation
- Web interface using Flask

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DnelZpt/gui-with-mySQL.git
    cd gui-with-mySQL/project_gym
    ```
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```


3. Set up the MySQL database:
    - Create a MySQL database named `gym_db`.
    - Execute the SQL script `schema.sql` to create the necessary tables.

4. Configure the database connection:
    - Update the `connections_pool.py` file with your MySQL database credentials.

## Usage

### GUI Application
Run the application:
```sh
python project_gym/gym_app_gui.py
```

### Web Interface
Run the Flask app to access the web interface:
```sh
python app.py
```
Open a web browser and go to `http://localhost:5000/` to access the web interface.


## Project Structure
  - `project_gym/client_cls.py`: Contains the Client class.
  - `project_gym/client_dao.py`: Contains the ClientDAO class for database operations.
  - `project_gym/gym_app_gui.py`: Contains the GymApp class for the GUI.
  - `project_gym/connections_pool.py`: Manages the connection pool for MySQL.
  - `app.py`: Contains the Flask app for the web interface.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

