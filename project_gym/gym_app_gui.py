"""
This module contains the GUI for the Gym App.

Daniel Zapata - 2024
"""

from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from project_gym.client_cls import Client
from project_gym.client_dao import ClientDAO
import tkinter as tk


class GymApp(tk.Tk):
    WINDOW_COLOR = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.frame_buttons = None
        self.frame_form = None
        self.name_entry = None
        self.table = None
        self.table_frame = None
        self.client_id = None
        self.styles = ttk.Style()
        self.configure_window()
        self.configure_grid()
        self.show_title()
        self.show_form()
        self.load_table()
        self.show_buttons()

    def configure_window(self):
        """
        Configures the main window of the Gym App.

        This method sets the title, size, background color, and styles for the main window.
        It uses the 'clam' theme and customizes the background, foreground, and field background colors.
        """
        self.title('Gym App')
        self.geometry('900x600')
        self.configure(background=GymApp.WINDOW_COLOR)
        self.styles.theme_use('clam')
        self.styles.configure(self,
                              background=GymApp.WINDOW_COLOR,
                              foreground='white',
                              fieldbackground='black')

    def configure_grid(self):
        """
        Configures the grid for the main window of the Gym App.

        This method creates a grid layout for the main window.
        """
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def show_title(self):
        """
        Displays the title of the Gym App.

        This method creates a label with the title of the Gym App and displays it on the main window.
        """
        title_label = ttk.Label(self, text='Gym App', font=('Arial', 30, 'bold'), background=GymApp.WINDOW_COLOR,
                                foreground='white')
        title_label.grid(row=0, column=0, columnspan=2, pady=30)

    def show_form(self):
        """
        Displays the form to add a new client to the Gym App.

        This method creates the form to add a new client to the Gym App and displays it on the main window.
        """
        self.frame_form = ttk.Frame(self)

        # Name
        name_label = ttk.Label(self.frame_form, text='Name:', background=GymApp.WINDOW_COLOR, foreground='white')
        name_label.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.name_entry = ttk.Entry(self.frame_form)
        self.name_entry.grid(row=0, column=1)

        # Last Name
        last_name_label = ttk.Label(self.frame_form, text='Last Name:', background=GymApp.WINDOW_COLOR,
                                    foreground='white')
        last_name_label.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.last_name_entry = ttk.Entry(self.frame_form)
        self.last_name_entry.grid(row=1, column=1)

        # Membership
        membership_label = ttk.Label(self.frame_form, text='Membership N°:', background=GymApp.WINDOW_COLOR,
                                     foreground='white')
        membership_label.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membership_entry = ttk.Entry(self.frame_form)
        self.membership_entry.grid(row=2, column=1)

        # Show the frame
        self.frame_form.grid(row=1, column=0)

    def load_table(self):
        """
        Displays the table of clients in the Gym App.

        This method creates a table to display the clients in the Gym App and displays it on the main window.
        """
        # Create a frame to hold the table
        self.table_frame = ttk.Frame(self)
        # Define the table style
        self.styles.configure('Treeview',
                              background='black', foreground='white', fieldbackground='black', rowheight=30)

        # Create the table
        columns = ('ID', 'Name', 'Last Name', 'Membership N°')
        self.table = ttk.Treeview(self.table_frame, columns=columns,
                                  show='headings')
        # Set the column headings
        self.table.heading('ID', text='ID', anchor='center')
        self.table.heading('Name', text='Name', anchor=tk.W)
        self.table.heading('Last Name', text='Last Name', anchor=tk.W)
        self.table.heading('Membership N°', text='Membership N°', anchor=tk.E)

        # Define the column widths
        self.table.column('ID', width=50, anchor='center')
        self.table.column('Name', width=120, anchor=tk.W)
        self.table.column('Last Name', width=120, anchor=tk.W)
        self.table.column('Membership N°', width=105, anchor='center')

        # Load the table with data from the database
        clients = ClientDAO.select()
        for client in clients:
            self.table.insert(parent='', index='end',
                              values=(client.id, client.name, client.last_name, client.membership))

        # Add the scrollbar
        scrollbar = ttk.Scrollbar(self.table_frame, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Show the table
        self.table.grid(row=0, column=0)

        # Associate the selection event with the table
        self.table.bind('<<TreeviewSelect>>', self.load_client)
        # Show the frame
        self.table_frame.grid(row=1, column=1, padx=30)

    def load_client(self, event):
        """
        Loads the data of a client into the form.

        This method loads the data of a client into the form when the user selects a row in the table.

        :param event: The event that triggered the method.
        """
        # Get the selected row
        selected_row = self.table.selection()[0]
        # Get the values of the selected row
        values = self.table.item(selected_row, 'values')
        # Load the values into the form
        self.client_id = values[0]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])
        self.last_name_entry.delete(0, tk.END)
        self.last_name_entry.insert(0, values[2])
        self.membership_entry.delete(0, tk.END)
        self.membership_entry.insert(0, values[3])

    def show_buttons(self):
        """
        Displays the buttons to interact with the Gym App.

        This method creates the buttons to interact with the Gym App and displays them on the main window.
        """
        self.frame_buttons = ttk.Frame(self)

        # Create the buttons
        add_button = ttk.Button(self.frame_buttons, text='Save', command=self.validate_client)
        add_button.grid(row=0, column=0, padx=30)

        delete_button = ttk.Button(self.frame_buttons, text='Delete', command=self.delete_client)
        delete_button.grid(row=0, column=1, padx=30)

        clean_button = ttk.Button(self.frame_buttons, text='Clean', command=self.clear_data)
        clean_button.grid(row=0, column=2, padx=30)

        # Apply the style to the buttons
        self.styles.configure('TButton', background='#005f73')
        self.styles.map('TButton', background=[('active', '#0a9396')])

        # Show the frame
        self.frame_buttons.grid(row=2, column=0, columnspan=2, pady=40)

    def validate_client(self):
        """
        Validates the data for a new client.
        :return: None
        """
        # Validate the data for every entry
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        membership = self.membership_entry.get()

        if name and last_name and membership:
            # Create a new client
            if self.validate_membership():
                self.save_client()

            else:
                # Show an error message
                showerror('Invalid Membership', 'The membership number must be a number.')
                # Clear the entry
                self.membership_entry.delete(0, tk.END)
                self.membership_entry.focus_set()
        else:
            # Show an error message
            showerror('Empty Fields', 'All fields are required.')
            self.name_entry.focus_set()

    def validate_membership(self):
        """
        Validates the membership entry.
        :return: True if the membership entry is a number, False otherwise.
        """
        try:
            int(self.membership_entry.get())
            valid = True

        except ValueError:
            valid = False

        return valid

    def save_client(self):
        """
        Saves the client data to the database.

        This method retrieves the data from the form entries, validates the client ID, and either updates an existing
        client or inserts a new client into the database. It also updates the table and shows a confirmation message.
        """
        # Get the data from the entries
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        membership = int(self.membership_entry.get())
        # Validate the client ID value
        if self.client_id:
            # Create a new client
            client = Client(self.client_id, name, last_name, membership)
            # Update the client in the database
            ClientDAO.update(client)
            showinfo('Client Updated', 'The client has been updated successfully.')
        else:
            # Create a new client
            client = Client(name=name, last_name=last_name, membership=membership)
            # Insert the client into the database
            ClientDAO.insert(client)
            showinfo('Client Saved', 'The client has been saved successfully.')
            # Update the table
        self.update_table()

    def update_table(self):
        # Load the table with data from the database
        self.load_table()
        # Clean the entries
        self.clear_data()

    def clear_data(self):
        """
        Clears the form data.

        This method clears the form entries and sets the client ID to None.
        """
        # Clear the entries
        self.clear_entries()
        # Set the client ID to None
        self.client_id = None

    def clear_entries(self):
        """
        Clears the form entries.

        This method deletes the text in the name, last name, and membership entries,
        and sets the focus on the name entry.
        """
        self.name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.membership_entry.delete(0, tk.END)
        self.name_entry.focus_set()

    def delete_client(self):
        if self.client_id:
            # Create a new client
            client = Client(id=self.client_id)
            # Delete the client from the database
            ClientDAO.delete(client)
            showinfo('Client Deleted', 'The client has been deleted successfully.')
            # Update the table
            self.update_table()
        else:
            showerror('No Client Selected', 'Please select a client to delete.')


if __name__ == '__main__':
    app = GymApp()
    app.mainloop()
