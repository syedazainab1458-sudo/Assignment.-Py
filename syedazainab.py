1. #Student Grades Class
class Student:
 def __init__(self):
self.__grade = None  # Private attribute
 def get_grade(self):
     return self.__grade
  def set_grade(self, grade):
        if 0 <= grade <= 100:
     self.__grade = grade
   else:
     print("Invalid grade")
  def is_passed(self):
 if self.__grade is not None and self.__grade >= 50:
    return "Passed"
    else:
    return "Failed"
  # Test Script
  s = Student()
s.set_grade(120)      # Invalid grade
  s.set_grade(85)       # Valid
  print(f"Grade: {s.get_grade()}")
 print(f"Status: {s.is_passed()}")
 
 2.#Product Price Class
 class Product:
  def __init__(self):
  self.__price = 0
  def get_price(self):
  return self.__price
def set_price(self, amount):
      if amount > 0:
 self.__price = amount
else:
 print("Invalid price")
 def apply_discount(self, percent):
     if 0 < percent < 100:
  discount = (percent / 100) * self.__price
  self.__price -= discount
    # Test Script
 p = Product()
p.set_price(-50)      # Invalid price
 p.set_price(1000)
print(f"Price after setting: {p.get_price()}")
p.apply_discount(20)
 print(f"Price after discount: {p.get_price()}")

3.#Employee Salary Class
class Employee:
 def __init__(self):
self.__salary = 0
 def get_salary(self):
 return self.__salary
 def set_salary(self, amount):
  if amount >= 0:
 self.__salary = amount
   else:
print("Invalid salary")
def increase_salary(self, percent):
 increment = (percent / 100) * self.__salary
 self.__salary += increment
# Test Script
emp = Employee()
 emp.set_salary(-1000)
 emp.set_salary(5000)
  print(f"Salary after setting: {emp.get_salary()}")
 emp.increase_salary(10)
   print(f"Salary after increment: {emp.get_salary()}") 

4.#Car Speed Class
class Car:
def __init__(self):
 self.__speed = 0
  def get_speed(self):
return self.__speed
def set_speed(self, value):
if value >= 0:
self.__speed = value
  else:
 print("Invalid speed")
 def accelerate(self, amount):
  self.__speed += amount
def brake(self, amount):
self.__speed -= amount
if self.__speed < 0:
self.__speed =0
 # Test Script
my_car = Car()
my_car.set_speed(-20)
my_car.set_speed(50)
print(f"Speed after setting: {my_car.get_speed()}")
my_car.accelerate(30)
print(f"Speed after acceleration: {my_car.get_speed()}")
 my_car.brake(60)
  print(f"Speed after braking: {my_car.get_speed()}")
  print(f"Final speed: {my_car.get_speed()}")

5.#Bank Account Management
class BankAccount:
 def __init__(self):
self.__balance = 0
 def get_balance(self):
 return self.__balance
def set_balance(self, amount):
if amount >= 0:
self.__balance = amount
else:
print("Invalid balance amount")
def deposit(self, amount):
if amount > 0:
 self.__balance += amount
 def withdraw(self, amount):
if amount <= self.__balance:
self.__balance -= amount
else:
print("Insufficient balance")

 # Test Script
    acc = BankAccount()
    acc.set_balance(-50)
    acc.deposit(500)
 print(f"Balance after deposit: {acc.get_balance()}")
   acc.withdraw(300)
 print(f"Balance after withdrawal: {acc.get_balance()}")
print(f"Final balance: {acc.get_balance()}")
