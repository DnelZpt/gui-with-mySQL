"""
Module to create the connection pool to the database

This module creates a connection pool to the database using the mysql-connector-python library.
The connection pool is created based on the configuration parameters and the pool size.

Daniel Zapata - 2024
"""

from mysql.connector import pooling, Error


class ConnectionPool:
    DATABASE = 'gym_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'gym_pool'
    pool = None

    @classmethod
    def get_pool(cls):
        """
        Retrieves or creates a connection pool for the database.

        This method checks if a connection pool has already been created for the database.
        If not, it creates a new connection pool using the configuration parameters defined
        in the class attributes. The connection pool allows for efficient management of
        database connections, enabling reuse and reducing the overhead of establishing
        connections repeatedly.

        :returns:
            MySQLConnectionPool: An instance of the MySQLConnectionPool class, representing
            the connection pool for the database.

        :raises:
            Error: If there is an issue creating the connection pool, an error is caught
            and printed to the console.
        """
        if cls.pool is None:  # If the pool is not created
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    port=cls.DB_PORT
                )
                return cls.pool
            except Error as e:
                print(e)
        else:
            return cls.pool

    @classmethod
    def get_connection(cls):
        """
        Retrieves a connection from the pool.

        This method fetches an available connection from the connection pool. If the pool has not been
        initialized, it will raise an AttributeError due to the absence of the pool.

        :return:
               MySQLConnection: An instance of the MySQLConnection class, representing a connection to the database.

        :raises:
               AttributeError: If the connection pool has not been initialized.
        """
        return cls.get_pool().get_connection()

    @classmethod
    def release_connection(cls, connection):
        """
        Closes the given database connection.

        This method closes the provided database connection, releasing it back to the connection pool or
        closing the connection entirely. It's important to close connections to prevent database resource
        leakage.

        :param: connection (MySQLConnection): The database connection to close.
        """
        connection.close()


if __name__ == '__main__':
    # Pool object creation
    # pool = ConnectionPool.get_pool()
    # print(pool)
    # Connection object creation
    connection_1 = ConnectionPool.get_connection()
    print(connection_1)
    ConnectionPool.release_connection(connection_1)  # Close the connection
