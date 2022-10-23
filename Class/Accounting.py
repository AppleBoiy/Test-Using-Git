from .SuperClass import Employee
 
#- Inheritance classes
class Accounting(Employee):
    __department = 'Accounting'
    
    # Inherited attributes from Employee
    def __init__(self, name, salary, age):
        """
        Purpose: value
        """
        super().__init__(name, salary, self.__department)
        self.__age = age
        
        
    def _showData(self):
        super()._showData()
        print(f'Employee age : {self.__age }')
        
    def getData(self):
        data = super().getData()
        data['Age'] = self.__age
        return data
    
    def __str__(self) -> str:
        return super().__str__() + f'\nAge : {self.__age}'
    # end alternate constructor
