from helper import get_valid_input
import requests
import json

class Management():
    LOCAL_URL = "http://127.0.0.1:5000"
    URL = "https://calm-ridge-59728.herokuapp.com"
    
    # RESOURCES:
    CUSTOMERS = 1
    VIDEOS = 2

    def __init__(self):
        pass

    def menu(self, resource):
        if resource == self.CUSTOMERS:
            self.endpoint = "/customers"
            self.fields = ["name", "phone", "postal_code"]
            self.field_names = ["Name", "Phone Number", "Postal Code"]
            self.resource_name = "Customer"
            self.display_fields = ["videos_checked_out_count"]
            self.display_fields_names = ["Current Rentals"]
        elif resource == self.VIDEOS:
            self.endpoint = "/videos"
            self.fields = ["title", "release_date", "total_inventory"]
            self.field_names = ["Title", "Release Date", "Total Inventory"]
            self.display_fields = ["available_inventory"]
            self.display_fields_names = ["Available Inventory"]
            self.resource_name = "Video"

        while(True):
            self.print_menu()
            result = get_valid_input(int, range(1, 7))
            if result == 6:
                return
            else:
                self.handle_option(result)


    def print_menu(self):
        print(" ")
        print(f"Please choose from the following {self.resource_name} menu options:")
        print(f"To list all {self.resource_name}s, type 1")
        print(f"To see information for one {self.resource_name}, type 2")
        print(f"To add a new {self.resource_name}, type 3")
        print(f"To edit a {self.resource_name}, type 4")
        print(f"To delete a {self.resource_name}, type 5")
        print("To return to the main menu, type 6")

    LIST_ALL = 1
    LIST_ONE = 2
    ADD_NEW = 3
    EDIT = 4
    DELETE = 5

    def handle_option(self, option):
        if option == self.LIST_ALL:
            self.list_all()
        if option == self.LIST_ONE:
            self.list_one()
        if option == self.ADD_NEW:
            self.add_one()
        if option == self.EDIT:
            self.edit()
        if option == self.DELETE:
            self.delete()

    
    def list_all(self):
        data = requests.get(self.URL + self.endpoint)
        for element in data.json():
            self.print_resource(element)
            print(" ")
    
    def list_one(self):
        print(f"Please input the ID of the {self.resource_name} that you want to view")
        id = get_valid_input(int)
        data = requests.get(self.URL + self.endpoint + "/" + str(id) )
        if data.status_code == requests.codes.ok:
            self.print_resource(data.json())
        else:
            print(f"There is no {self.resource_name} with ID {id}.")

    def delete(self):
        print(f"Please input the ID of the {self.resource_name} that you want to delete")
        id = get_valid_input(int)
        data = requests.delete(self.URL + self.endpoint + "/" + str(id) )
        if data.status_code == requests.codes.ok:
            print(f"Successfully deleted {self.resource_name} with ID {id}.")
        else:
            print(f"Unable to delete {self.resource_name} with ID {id}.")
    
    def add_one(self):
        print(f"To create a {self.resource_name} please input the following information:")
        data = {}
        for i in range(len(self.fields)):
            print(self.field_names[i] + "?")
            data[self.fields[i]] = get_valid_input(str)
        
        url = self.URL + self.endpoint
        result = requests.post(url, json=data)
        if result.status_code == requests.codes.created:
            id = result.json()["id"]
            print(f"Successfully created a new {self.resource_name} with ID {id}.")
        else:
            print(f"Unable to create a new {self.resource_name}.")

    def edit(self):
        print(f"Please input the ID of the {self.resource_name} that you want to edit")
        id = get_valid_input(int)
        data = requests.get(self.URL + self.endpoint + "/" + str(id) )
        if data.status_code == requests.codes.ok:
            resource = data.json()
            id = resource["id"]
            print(f"To edit the {self.resource_name} pleae input the following information.  To keep the curent information press enter:")
            new_data = {}
            for i in range(len(self.fields)):
                current_value = resource[self.fields[i]]
                print(self.field_names[i] + " (" + str(current_value) + ") ?")
                new_value = get_valid_input(str)
                if(new_value == ""):
                    new_data[self.fields[i]] = current_value
                else:
                    new_data[self.fields[i]] = new_value
                
            url = self.URL + self.endpoint + "/" + str(id)
            print(new_data)
            result = requests.put(url, json=new_data)
            if result.status_code == requests.codes.ok:
                print(f"Successfully created updated a {self.resource_name} with ID {id}.")
            else:
                print(f"Unable to edit {self.resource_name} with ID {id}.")
        else:
            print(f"There is no {self.resource_name} with ID {id}.")


    def print_resource(self, resource):
        id = resource["id"]
        print(f"ID: {id}")
        fields = self.fields + self.display_fields
        field_names = self.field_names + self.display_fields_names
        for i in range(len(fields)):
            field_name = field_names[i]
            value = resource[fields[i]]
            print(f"{field_name}: {value}")
        
