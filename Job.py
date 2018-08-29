
class Job:
    name = None
    company = None
    state = None
    city = None
    salary = None



    def __init__(self, name, company, state, city, salary):
        self.name = name
        self.company = company
        self.state = state
        self.city = city
        self.salary = salary


    def getState(self):
        return self.state

    def getCity(self):
        return self.city

    def getSalary(self) :
        return self.salary




