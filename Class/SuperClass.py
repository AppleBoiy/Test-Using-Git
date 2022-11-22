# - Encapsulation
class Employee:
    # - Class variables
    __minSalary = 1200
    __maxSalary = 5000
    __companyName = 'XYZ'

    # - Private attributes (Cannot be edited)
    def __init__(self, name, salary, department):

        # - Protected (Can be edited)
        # self._name = name

        # - Private (Cannot be edited)
        # - Instance variables
        self.__name = name
        self.__salary = salary
        self.__department = department

    # - Protected attributes
    def _showData(self):
        print(f'Employee name : {self.getName()}')
        print(f'Employee salary : {self.getSalary()}')
        print(f'Employee department : {self.getDepartment()}')

    # - Setter attributes
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, newdepartment):
        self.__department = newdepartment

    # - Getter attributes
    def getName(self):
        return self.__name

    def getSalary(self):
        if self.__salary < self.__minSalary:
            return self.__minSalary
        elif self.__salary > self.__maxSalary:
            return self.__maxSalary
        else:
            return self.__salary

    def getDepartment(self):
        return self.__department

    # - Calculate annual income
    # - Overloading calculate
    def _annualIncome(self, bonus=0, overtime=0):
        sal = self.getSalary()
        return sal * 12 + bonus + overtime

    def getData(self):
        data = {
            'Name': self.getName(),
            'Salary': self.getSalary(),
            'Department': self.getDepartment(),
            'Annual Income': self._annualIncome(bonus=0, overtime=0)
        }

        return data

    # - Object constructor to string
    def __str__(self) -> str:
        return f'Name : {self.__name} \nDepartment : {self.__department} \nSalary : {self.__salary} \nAnnual income : {self._annualIncome()}'

    def __delattr__(self) -> None:
        del self.__name
        del self.__salary
        del self.__department

        pass
