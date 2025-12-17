from . import utils

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n  ".join([str(book) for book in self.books])

        return (
            f"STATUS: {utils.helper()}\n"
            f"Order date: {self.order_date}\n"
            f"Employee: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Books:\n  {book_list}"
        )