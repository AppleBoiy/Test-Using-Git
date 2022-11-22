from Class.SuperClass import Employee


class Programming(Employee):
    __department = 'Programming'

    def __init__(self, name, salary, experience, skill):
        """
        Purpose: 
        """
        super().__init__(name, salary, self.__department)
        self.__experience = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print(f'Employee experience : {self.__experience}')
        print(f'Employee skill : {self.__skill}')

    def getData(self):
        data = super().getData()
        data['Experiment'] = self.__experience
        data['Skill'] = self.__skill
        return data

    # - Object to string && Overwriting(OO)
    def __str__(self) -> str:
        return super().__str__() + f'\nExperiment : {self.__experience}\nSkill : {self.__skill}'

        # end default constructor
