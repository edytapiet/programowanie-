from magazine.product import Product
from magazine.library import Library
from magazine.employee import Employee
from magazine.student import Student
from magazine.book import Book
from magazine.order import Order


def main():
    p = Product("Czekolada")
    print(p.show())

    print("-" * 30)


    lib1 = Library("Kraków", "Floriańska 12", "31-001", "10:00-18:00", "444-333-567")
    book1 = Book(lib1, 1945, "George", "Orwell", 120)
    emp1 = Employee("Karol", "Poleski", "2019-03-29", "1998-06-11", "Kraków", "Floriańska 12", "00-003", "987-645-754")
    stu1 = Student("Ola", "Zając", "Warszawa")


    order1 = Order(emp1, stu1, [book1], "2024-10-10")
    print(order1)


if __name__ == "__main__":
    main()