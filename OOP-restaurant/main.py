class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"Number of customers served : {self.number_served}")

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"Number of customers served : {self.number_served}")


class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts = 0

    def describe_user(self):
        username = f"{self.first_name} {self.last_name}"
        print(f"Username: {username}")
        return username

    def greet_user(self):
        username = f"{self.first_name} {self.last_name}"
        print(f"Hello {username}")

    def increment_login_attempts(self, increment):
        self.login_attempts += increment
        print(f"User has logged in {self.login_attempts} times")

    def reset_login_attempts(self):
        self.login_attempts = 0


class IceCreamStand(Restaurant):
    """"Represents an ice cream stand that inherits from the Restaurant Class"""

    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['chocolate', 'strawberry', 'vanilla']

    def get_flavors(self):
        print("Available Flavors")
        num = 1
        for flavor in self.flavors:
            print(f"{num}. {flavor.title()}")
            num += 1


class Administrator(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Admin privileges")
        num = 1
        for privilege in self.privileges:
            print(f"{num}. {privilege.capitalize()}")
            num += 1


stand = IceCreamStand("Pinkberry", "Ice Cream Stand")
stand.describe_restaurant()
stand.get_flavors()

admin = Administrator("Jeffrey", "Asante")
admin.show_privileges()
