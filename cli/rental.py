from helper import get_valid_input
import requests
import json

class Rental():

    LOCAL_URL = "http://127.0.0.1:5000"
    URL = "https://calm-ridge-59728.herokuapp.com"

    def __init__(self):
        self.fields = ["customer_id", "video_id"]
        self.field_names = ["Customer ID", "Video ID"]
        self.endpoint = "/rentals"

    RENT = 1
    RETURN = 2
    EXIT = 3

    def menu(self):
        while(True):
            self.print_menu()
            result = get_valid_input(int, range(1, 4))
            if result == self.EXIT:
                return
            else:
                self.handle_option(result)

    def print_menu(self):
        print(" ")
        print(f"Please choose from the following Rental menu options:")
        print(f"To rent a movie to a customer, type 1")
        print(f"To check in a rental, type 2")
        print("To return to the main menu, type 3")

    def handle_option(self, option):
        if option == self.RENT:
            self.rent_video()
        if option == self.RETURN:
            self.return_video()

    def rent_video(self):
        print(f"To rent a video to a customer please input the following information:")
        data = self.get_rental_data()
        url = self.URL + self.endpoint + "/check-out"
        result = requests.post(url, json=data)
        if result.status_code == requests.codes.ok:
            due_date = result.json()["due_date"]
            print(f"Successfully rented the video.  The due date is {due_date}")
        else:
            print(f"Unable to rent the video.")

    def return_video(self):
        print(f"To return a video please input the following information:")
        data = self.get_rental_data()
        url = self.URL + self.endpoint + "/check-in"
        result = requests.post(url, json=data)
        if result.status_code == requests.codes.ok:
            # due_date = result.json()["due_date"]
            print(f"Successfully returned the video.")
        else:
            print(f"Unable to return the video.")

    def get_rental_data(self):
        data = {}
        for i in range(len(self.fields)):
            print(self.field_names[i] + "?")
            data[self.fields[i]] = get_valid_input(str)
        return data