class Vehicle:

    num_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model}. It runs on {self.fuel}"

class Car(Vehicle):

    num_of_wheels = 4

class Truck(Vehicle):
    # Overriding default value

    num_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

class GitHubRepo:

    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"{self.name} is a {self.language} repo with {self.num_stars}"

daily = Vehicle("Subaru", "Crosstrek")
print(daily)
daily.num_of_wheels = 3

print("for Class", Vehicle.num_of_wheels)
print("Instance", daily.num_of_wheels)
