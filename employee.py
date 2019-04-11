# Employee Class


class Employee:
    maxhours = 28

    def __init__(self, name, fulltime=False):
        self.name = name

        if fulltime == True:
            self.maxhours = 40

    def info(self):
        print(f"Name: {self.name} and max is: {self.maxhours}.")


john = Employee("john")


john.info()
