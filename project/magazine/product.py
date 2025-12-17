from . import utils

class Product:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"Produkt: {self.name}, {utils.helper()}"