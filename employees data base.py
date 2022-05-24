# import csv
# from termcolor import colored
from msvcrt import getch
import sqlite3
import re


def match_date(date):
    re_date = re.search(r'^((?:(?:[0-2][0-9])|(?:[3][0-1]))/(?:(?:[0][0-9])|(?:[1][0-2]))/[0-9]{4})$', date)
    if re_date:
        return re_date.group(1)
    else:
        return bool(re_date)


def match_phone(phone):
    re_phone = re.search(r'^(\d{11})$', phone)
    if re_phone:
        return re_phone.group(1)
    else:
        return bool(re_phone)


def match_email(email):
    re_email = re.search(r'^(\w+@\w+.(?:com|org|net))$', email)
    if re_email:
        return re_email.group(1)
    else:
        return bool(re_email)


# class to create employees objects
class person:
    count = 0

    def __init__(self, first, last, title, birthdate, hiredate, phone, email):
        self.first = first
        self.last = last
        self.title = title
        self.birthdate = birthdate
        self.hiredate = hiredate
        self.phone = phone
        self.email = email
        person.count += 1


# connect to database
db = sqlite3.connect('Employees.db')
cr = db.cursor()
cr.execute(
    "CREATE TABLE IF NOT EXISTS employees(id INTEGER, first TEXT,last TEXT,title TEXT,birth NUMERIC, hire NUMERIC, phone TEXT, email TEXT, PRIMARY KEY(id))")


# show name for all employees
def show_all():
    data = cr.execute("SELECT id,first,last FROM employees")
    for _ in data.fetchall():
        print(_[0], _[1], _[2])
    save_and_quit()


# add new employee
def add_new():
    # Taking DATA
    xfname = input("First name: ").strip().capitalize()
    xlname = input("Last name: ").strip().capitalize()
    xtitle = input("Title: ").strip().capitalize()
    xbirthdate = match_date(input("Birthdate 01/01/2001: ").strip())
    xhiredate = match_date(input("Hiredate 01/01/2001: ").strip())
    xphone = match_phone(input("Phone 01?????????: ").strip())
    xemail = match_email(input("username@domain.(com|org|net): ").strip())
    # Checking DATA
    if (bool(xbirthdate) & bool(xhiredate) & bool(xphone) & bool(xemail)):
        x = person(xfname, xlname, xtitle, xbirthdate, xhiredate, xphone, xemail)
        id = cr.execute(
            f"INSERT INTO employees (first,last,title,birth,hire,phone,email) VALUES ('{x.first}','{x.last}','{x.title}','{x.birthdate}','{x.hiredate}','{x.phone}','{x.email}')")
        print(f"Employee ID is {id.lastrowid} remember it\U0001F60A")
        save_and_quit()
    else:
        print("Something wrong with your inputed data, check your data and try again")
        save_and_quit()


# delete an employee
def delet_by_id():
    Id = int(input("ID: "))
    deleted = cr.execute(f"DELETE FROM employees WHERE id ='{Id}'")

    if deleted.rowcount == 1:
        print("Deleted")
    else:
        print("ID entered not exists")
    save_and_quit()


def update_name():
    pass


def update_title():
    pass


# get all DATA of one employee
def show_specific_by_id():
    Id = input("ID: ")
    data = cr.execute(f"SELECT * FROM employees WHERE id ='{Id}'")
    print(data.fetchall())


# search for all employee data by his name
def search_by_name():
    pass


# save changes and then cut connection with database
def save_and_quit():
    db.commit()
    db.close()
    print("Press any key to exit\U0001F60A...")
    junk = getch()


def update_phone():
  pass


def case(x):
    if x == "s":
        show_all()
    elif x == "a":
        add_new()
    elif x == "d":
        delet_by_id()
    elif x == "g":
        update_phone()
    elif x == "n":
        update_title()
    elif x == "p":
        show_specific_by_id()
    else:
        save_and_quit()
    return 0


# print catalog then take input from user
print('''What do you want to do?
      "s" Show all employees
      "a" Add new employee
      "d" Delet by id
      "g" Update phone for an employee
      "n" Update title for an employee
      "p" show all data for an employee
      "q" Quit''')
x = input("").lower()
if x in "sadgnpq":
    case(x)
else:
    print("See catalog above")
    save_and_quit()
