"""
This module contains the Client class, which represents a client of the gym.

Daniel Zapata - 2024
"""


class Client:
    """
    Represents a client of the gym.

    Attributes:
    ----------
        id : int
            The unique identifier for the client.
        name : str
            The first name of the client.
        last_name : str
            The last name of the client.
        membership : str
            The type of membership the client has.

    Methods:
    -------
        __str__:
            Returns a string representation of the client.
    """

    def __init__(self, id: int = None, name: str = None, last_name: str = None, membership: int = None):
        """
        Initializes a new instance of the Client class.

        :param:
            id (int): The unique identifier for the client.
            name (str): The first name of the client.
            last_name (str): The last name of the client.
            membership (str): The type of membership the client has.
        """
        self.id = id
        self.name = name
        self.last_name = last_name
        self.membership = membership

    def __str__(self):
        """
        Returns a string representation of the client.

        :return:
            str: A string that contains the client's ID, name, last name, and membership type.
        """
        return f'ID: {self.id}, Name: {self.name}, Last name: {self.last_name}, Membership N°: {self.membership}'


if __name__ == '__main__':
    client = Client(1, 'Daniel', 'Zapata', 345)
    print(client)
