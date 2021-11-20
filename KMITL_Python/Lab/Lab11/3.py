class Name:
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
    
    def setName(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l
    
    def getFullName(self):
        return f"Full name = {self.title}.{self.firstName} {self.lastName}"


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
    
    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    def getDateBC(self):
        return f"{self.day}/{self.month}/{self.year + 543}"


class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
    
    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
    
    def getAddress(self):
        return f"House No: {self.houseNo} Street: {self.street} District: {self.district} City: {self.city} Country: {self.country} Postcode: {self.postcode}"


class Department:
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList
    
    def addEmployee(self, e):
        self.employeeList.append(e)
        e.Department = self
    
    def deleteEmployee(self, e):
        self.list.remove(e)
        e.Department = None
    
    def setManager(self, e):
        if type(e) == PermEmployee and e in self.employeeList:
            self.manager = e

    def printInfo(self):
        print(f"Department: {self.description}\n" +
              f"Manager: {self.manager.firstName} {self.manager.lastName}\n" +
              f"Employees: {self.employeeList}")


class Person:
    def __init__(self, name, date, address):
        self.name = name
        self.birthdate = date
        self.address = address
    
    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()} Address: {self.address.getAddress()}")
    

class Employee(Person):
    def __init__(self, name, date, address, startDate , startMonth, startYear, department):
        super().__init__(name, date, address)

        self.startDate = startDate
        self.startMonth = startMonth
        self.startYear = startYear
        self.department = department
    
    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()} Address: {self.address.getAddress()} " +
              f"Start date: {self.startDate}/{self.startMonth}/{self.startYear} Department: {self.department}")


class TempEmployee(Employee):
    def __init__(self, name, date, address, startDate , startMonth, startYear, department, wage):
        super().__init__(name, date, address, startDate , startMonth, startYear, department)

        self.wage = wage
    
    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()} Address: {self.address.getAddress()} " +
              f"Start date: {self.startDate}/{self.startMonth}/{self.startYear} Department: {self.department} Wage: {self.wage}")


class PermEmployee(Employee):
    def __init__(self, name, date, address, startDate , startMonth, startYear, department, salary):
        super().__init__(name, date, address, startDate , startMonth, startYear, department)

        self.salary = salary
    
    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()} Address: {self.address.getAddress()} " +
              f"Start date: {self.startDate}/{self.startMonth}/{self.startYear} Department: {self.department.description} Salary: {self.salary}")

name = Name("Mr", "John", "Smith")
address = Address("111", "345", "long street", "test city", "test1", "test2")
date = Date("06", "03", "2003")
person = Person(name, date, address)
person.printInfo()
emptyList = []
department = Department("best department", person, emptyList)
employee = PermEmployee(name, date, address, 22, 3, 2021, department, 15000)
employee.printInfo()
