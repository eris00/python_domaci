
# 5

datas = [{"naziv":"Español para principiantes", "br_pozitivni":1000,"br_negativni":10},
{"naziv":"Philophize This!", "br_pozitivni":500, "br_negativni": 30}, {"naziv":"Science VS. ",
"br_pozitivni":600,"br_negativni": 45}]


worst = None
worst_temp = float("inf")

for podcast in datas:
    val = podcast["br_pozitivni"] / podcast["br_negativni"]
    
    if val < worst_temp:
        worst_temp = val
        worst = podcast["naziv"]

print("Najgori je:", worst)



# 7

class Book:
  def __init__(self, title, author, publish_year, copies):
      self._title = title
      self._author = author
      self._publish_year = publish_year
      self._copies = copies

  def get_title(self):
      return self._title

  def get_author(self):
      return self._author

  def get_publish_year(self):
      return self._publish_year

  def get_copies(self):
      return self._copies

  def set_title(self, title):
      self._title = title

  def set_author(self, author):
      self._author = author

  def set_publish_year(self, year):
      self._publish_year = year

  def set_copies(self, n):
      self._copies = n

  def __str__(self):
      return f"{self._title} — {self._author} ({self._publish_year}), copies: {self._copies}"


class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def _find_first_by_title(self, title):
    title_lower = title.lower().strip()
    for b in self.books:
        if b.get_title().lower().strip() == title_lower:
            return b
    return None

  def _find_index_by_title(self, title):
    title_lower = title.lower().strip()
    for i, b in enumerate(self.books):
        if b.get_title().lower().strip() == title_lower:
            return i
    return -1

  def delete_book_by_title(self, title):
    idx = self._find_index_by_title(title)
    if idx != -1:
        del self.books[idx]
        return True
    return False

  def edit_book(self, old_title, new_title=None, new_author=None, new_year=None, new_copies=None):
    b = self._find_first_by_title(old_title)
    if not b:
      return False
    if new_title is not None and new_title.strip() != "":
      b.set_title(new_title)
    if new_author is not None and new_author.strip() != "":
      b.set_author(new_author)
    if new_year is not None:
      b.set_publish_year(new_year)
    if new_copies is not None:
      b.set_copies(new_copies)
    return True

  def search_by_title(self, query):
    q = query.lower()
    return [b for b in self.books if q in b.get_title().lower()]

  def search_by_author(self, query):
    q = query.lower()
    return [b for b in self.books if q in b.get_author().lower()]

  def show_all(self):
    if not self.books:
      print("No books")
    else:
      for i, b in enumerate(self.books, start=1):
        print(f"{i}. {b.get_title()} — {b.get_author()} ({b.get_publish_year()})")


def input_int(prompt, allow_empty=False):
  while True:
    s = input(prompt).strip()
    if allow_empty and s == "":
        return None
    try:
        return int(s)
    except ValueError:
        print("Please enter integer")


def menu():
  print("Choose options:")
  print("Add new book")
  print("Show all books")
  print("Search from title")
  print("Search from author")
  print("Edit book")
  print("Delete book")
  print("Exit")


def main_program():
  lib = Library()

  lib.add_book(Book("Book1", "Author1", 2001, 3))
  lib.add_book(Book("Book2", "Autor2", 2021, 2))
  lib.add_book(Book("Book3", "Author3", 2015, 1))

  recent_added_books = []

  while True:
    menu()
    choice = input("Choose option: ").strip()

    if choice == "1":
      title = input("Title: ").strip()
      author = input("Author: ").strip()
      year = input_int("Publish year: ")
      copies = input_int("Number of copies: ")
      lib.add_book(Book(title, author, year, copies))
      print("Book added!")

    elif choice == "2":
      lib.show_all()

    elif choice == "3":
      q = input("Enter part of the title: ").strip()
      res = lib.search_by_title(q)
      if res:
          print("Found from title:")
          for b in res:
            print(" -", b)
      else:
          print("No results for given title.")

    elif choice == "4":
      q = input("Enter part of the author name: ").strip()
      res = lib.search_by_author(q)
      if res:
        print("Found by author:")
        for b in res:
          print(" -", b)
      else:
        print("No results for given author.")

    elif choice == "5":
      old = input("Enter that title to edit: ").strip()
      if not lib._find_first_by_title(old):
          print("There is no that book")
          continue

      print("Leave field empty")
      new_title = input("New title: ")
      new_author = input("New author: ")
      new_year = input_int("New publish year: ", allow_empty=True)
      new_copies = input_int("New number of copies: ", allow_empty=True)

      ok = lib.edit_book(
        old_title=old,
        new_title=new_title if new_title != "" else None,
        new_author=new_author if new_author != "" else None,
        new_year=new_year,
        new_copies=new_copies
      )
      if ok:
        print("Book updated")
      else:
          print("Error while editing ")

    elif choice == "6":
        title = input("Enter that title to delete: ").strip()
        if lib.delete_book_by_title(title):
            print("Book deleted.")
        else:
            print("Book not found check the title.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Non-existing option, choose again.")


if __name__ == "__main__":
    main_program()


# 12
class Company:
  def __init__(self, name, area, balance, max_num_of_employees):
    self.__name = name
    self.__area = area
    self.__employees = []
    self.__balance = balance
    self.__max_num_of_employees = max_num_of_employees

  def get_name(self):
    return self.__name

  def set_name(self, value):
    self.__name = value

  def get_area(self):
    return self.__area

  def set_area(self, value):
    self.__area = value

  def get_balance(self):
    return self.__balance

  def set_balance(self, value):
    if value < 0:
        return
    self.__balance = value

  def get_max_num_of_employees(self):
    return self.__max_num_of_employees

  def set_max_num_of_employees(self, value):
    if value < 0:
      return
    self.__max_num_of_employees = value

  def add_employee(self, employee):
    new_employee = True
    if len(self.__employees) < self.__max_num_of_employees:
      self.__employees.append(employee)
      return True
    return False

  def remove_employee(self, employee_name, employee_surname):
    i = 0
    while i < len(self.__employees):
      emp = self.__employees[i]
      if emp.get("name") == employee_name and emp.get("surname") == employee_surname:
        del self.__employees[i]
        return True
      i += 1
    return False

  def __str__(self):
    return f'"name": "{self.__name}", "area": "{self.__area}", "balance": "{self.__balance}"'

  def can_pay_employees(self):
    total = 0.0
    for emp in self.__employees:
      s = emp.get("salary", 0)
      total = total + s
    return self.__balance > total

  def __gt__(self, other):
    return len(self.__employees) >= len(other.__employees) 


c1 = Company("TechNova", "Software", 12000.0, 4)
c2 = Company("DataForge", "Analytics", 8000.0, 3)

print(str(c1))
print(str(c2))

c1.add_employee({"name": "John", "surname": "Doe", "salary": 3000})
c1.add_employee({"name": "Ana", "surname": "Ilic", "salary": 2800})
c1.add_employee({"name": "Mira", "surname": "Kovac", "salary": 2500})

c2.add_employee({"name": "Luka", "surname": "Peric", "salary": 4000})
c2.add_employee({"name": "Sara", "surname": "Nikic", "salary": 3500})

print(c1.can_pay_employees())
print(c2.can_pay_employees())

print(c1 > c2)

c1.remove_employee("Ana", "Ilic")
print(c1.can_pay_employees())
print(c1 > c2)

c1.set_balance(8300.0)
print(c1.get_balance())
c1.set_max_num_of_employees(5)
print(c1.get_max_num_of_employees())
