
class Job:
    name = None
    state = None
    city = None
    salary = None



    def __init__(self, name, company, state, city, salary):
        self.name = name
        self.company = company
        self.state = state
        self.city = city
        self.salary = salary


    def getSalary(self) :
        return self.salary
