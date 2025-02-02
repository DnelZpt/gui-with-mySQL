from project_gym.client_cls import Client
from project_gym.connections_pool import ConnectionPool


class ClientDAO:
    SELECT_ALL = "SELECT * FROM clients"
    SELECT_ID = "SELECT * FROM clients WHERE id = %s"
    INSERT = "INSERT INTO clients (name, last_name, membership) VALUES (%s, %s, %s)"
    DELETE = "DELETE FROM clients WHERE id = %s"
    UPDATE = "UPDATE clients SET name = %s, last_name = %s, membership = %s WHERE id = %s"

    @classmethod
    def select(cls):
        """
        Retrieves all clientes from the database.

        This method fetches all clientes from the database and returns them as a list of Client objects.

        :return:
            list: A list of Client objects, representing all clientes in the database.
        """
        connection = None
        try:
            connection = ConnectionPool.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.SELECT_ALL)
            records = cursor.fetchall()
            clientes = []
            for record in records:
                clientes.append(Client(record[0], record[1], record[2], record[3]))

            return clientes

        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                cursor.close()
                ConnectionPool.release_connection(connection)

    @classmethod
    def select_by_id(cls, client_id):
        """
        Retrieves a client from the database by its ID.

        This method fetches a client from the database using the provided client ID and returns it as a Client object.

        :param: client_id (int): The ID of the client to retrieve from the database.

        :return:
            Client: A Client object representing the client with the provided ID.
        """
        connection = None
        try:
            connection = ConnectionPool.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.SELECT_ID, (client_id,))
            record = cursor.fetchone()
            if record is not None:
                return Client(record[0], record[1], record[2], record[3])
        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                cursor.close()
                ConnectionPool.release_connection(connection)

    @classmethod
    def insert(cls, client):
        """
        Inserts a new client into the database.

        This method inserts a new client into the database using the provided client object.

        :param: client (Client): The client object to insert into the database.
        """
        connection = None
        try:
            connection = ConnectionPool.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.INSERT, (client.name, client.last_name, client.membership))
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                cursor.close()
                ConnectionPool.release_connection(connection)

    @classmethod
    def delete(cls, client: Client):
        """
        Deletes a client from the database.

        This method deletes a client from the database using the provided client ID.

        :param: client_id (int): The ID of the client to delete from the database.
        """
        connection = None
        try:
            connection = ConnectionPool.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.DELETE, (client.id,))
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                cursor.close()
                ConnectionPool.release_connection(connection)

    @classmethod
    def update(cls, client):
        """
        Updates a client in the database.

        This method updates a client in the database using the provided client object.

        :param: client (Client): The client object with the updated information.
        """
        connection = None
        try:
            connection = ConnectionPool.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.UPDATE, (client.name, client.last_name, client.membership, client.id))
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                cursor.close()
                ConnectionPool.release_connection(connection)


if __name__ == '__main__':
    # Insert a new client
    # client_1 = Client(name='John', last_name='Doe', membership=123)
    # inserted_client = ClientDAO.insert(client_1)
    # print(f'Inserted client: {inserted_client}')

    # Delete a client
    # client = Client(id=4)
    # deleted_client = ClientDAO.delete(client)
    # print(f'Deleted client: {deleted_client}')

    clients = ClientDAO.select()
    for client in clients:
        print(client)
