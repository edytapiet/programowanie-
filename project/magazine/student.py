class Student:
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def __str__(self):
        return f"Student: {self.first_name}, {self.last_name}, city: {self.city}"