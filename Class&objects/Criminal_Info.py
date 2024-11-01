class Criminal:
    def __init__(self, name_class, age_class, height_class, weight_class, gender_class, id_number_class, crime_class, date_of_registration_class, date_of_release_class, time_to_serve_class):
        self.name = name_class
        self.age = age_class
        self.height = height_class
        self.weight = weight_class
        self.gender = gender_class
        self.id_number = id_number_class
        self.date_of_registration = date_of_registration_class
        self.crime = crime_class
        self.date_of_release = date_of_release_class
        self.time_to_serve = time_to_serve_class




    def show_details(self):
        print(f"Name: {self.name} \nID: {self.id_number} \nDate of Registration: {self.date_of_registration} \nDate of Release: {self.date_of_release} \nGender: {self.gender} \nCrime: {self.crime} \nTime to Serve: {self.time_to_serve}")

name = input("Enter Full Name: ")
age = input("Enter Age: ")
id_number = input("Enter ID Number: ")
height = input("Enter Height (in inches): ")
weight = input("Enter Weight (in pounds): ")
gender = input("Gender: ")
crime = input("Crime: ")
date_of_registration = input("Date of Registration: ")
date_of_release = input("Date of Release: ")
time_to_serve = input("Time to Serve: ")


c1 = Criminal(name, age, height, weight, gender, id_number, crime, date_of_registration, date_of_release, time_to_serve)

c2 = Criminal(name, age, height, weight, gender, id_number, crime, date_of_registration, date_of_release, time_to_serve)

c3 = Criminal(name, age, height, weight, gender, id_number, crime, date_of_registration, date_of_release, time_to_serve)

c1.show_details()
c2.show_details()
c3.show_details()
