from .SuperClass import Employee

class Sale(Employee):
    __department = 'Sale'
      
    def __init__(self, name, salary, area):
        """
        Purpose: value
        """
        super().__init__(name, salary, self.__department)
        self.__area = area
        
    def _showData(self):
        super()._showData()
        print(f'Employee area : {self.__area}')
        
    def getData(self):
        data = super().getData()
        area = {'Area': self.__area }
        data.update(area)
        return data
        
        
    def __str__(self) -> str:
        return super().__str__() + f'\nArea : {self.__area}'
