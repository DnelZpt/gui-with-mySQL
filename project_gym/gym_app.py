from client_cls import Client
from client_dao import ClientDAO

print('*** Gym Client Management System ***')
option = None

while option != 5:
    print('\nMain Menu:')
    print('1. Add a new client')
    print('2. Delete a client')
    print('3. Update a client')
    print('4. List all clients')
    print('5. Exit')
    option = int(input('Enter an option (1-5): '))

    if option == 1:  # Add a new client
        name = input('Enter the client name: ')
        last_name = input('Enter the client last name: ')
        membership = int(input('Enter the client membership: '))
        client = Client(name=name, last_name=last_name, membership=membership)
        inserted_client = ClientDAO.insert(client)
        print(f'Inserted clients: {inserted_client}')
        # Clean the output
        print()

    elif option == 2:
        id = int(input('Enter the client ID: '))
        client = Client(id=id)
        deleted_client = ClientDAO.delete(client)
        print(f'Deleted clients: {deleted_client}')
        print()
    elif option == 3:
        id = int(input('Enter the client ID: '))
        name = input('Enter the new client name: ')
        last_name = input('Enter the new client last name: ')
        membership = int(input('Enter the new client membership: '))
        client = Client(id=id, name=name, last_name=last_name, membership=membership)
        updated_client = ClientDAO.update(client)
        print(f'Updated clients: {updated_client}')
        print()
    elif option == 4:
        clients = ClientDAO.select()
        print('\n*** Clients ***')
        for client in clients:
            print(client)

        print('*** End of List ***\n')
    elif option == 5:
        print('Exiting...')
    else:
        print('Invalid option. Please try again.\n')
