# Gym App

Gym App is a graphical user interface (GUI) built using Python and Tkinter. The application allows users to manage client information, including adding, updating, and deleting client records. The client data is stored in a MySQL database, and the app includes features such as form validation, data display in a table, and user notifications.

## Features

- Add new clients
- Update existing clients
- Delete clients
- Display client information in a table
- Form validation
- User notifications

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DnelZpt/gui-with-mySQL.git
    cd gym-app
    ```

4. Set up the MySQL database:
    - Create a MySQL database named `gym_db`.
    - Execute the SQL script `schema.sql` to create the necessary tables.

5. Configure the database connection:
    - Update the `connections_pool.py` file with your MySQL database credentials.

## Usage
Run the application:
```sh
python project_gym/gym_app_gui.py
```
## Project Structure
  - project_gym/client_cls.py: Contains the Client class.
  - project_gym/client_dao.py: Contains the ClientDAO class for database operations.
  - project_gym/gym_app_gui.py: Contains the GymApp class for the GUI.
  - project_gym/connections_pool.py: Manages the connection pool for MySQL.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

