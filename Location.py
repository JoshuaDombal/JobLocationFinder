

class Location:

    city = None
    state = None
    country = None
    averageSalary = None
    numberOfJobs = None
    jobs = []

    costOfLivingIndex = None
    salaryCostRatio = None



    def __init__(self):
        self.city = None
        self.state = None
        self.country = None
        self.averageSalary = 0
        self.numberOfJobs = 0
        self.jobs = []
        self.costOfLivingIndex = 0
        self.salaryCostRatio = 0

    def getCity(self):
        return self.city

    def getNumberOfJobs(self):
        return self.numberOfJobs

    def getJobs(self):
        return self.jobs

    def getAverageSalary(self):
        return self.averageSalary

    def getCostOfLivingIndex(self):
        return self.costOfLivingIndex

    def getSalaryCostRatio(self):
        return self.salaryCostRatio

    # ************************   SETTERS    *************************** #

    def addJob(self, job):
        self.jobs.append(job)
        self.numberOfJobs += 1

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.state = state

    def setCountry(self, country):
        self.country = country

    def setAverageSalary(self, avgSalary):
        self.averageSalary = avgSalary

    def setCostofLivingIndex(self, colIndex):
        self.costOfLivingIndex = colIndex

    def setSalaryCostRatio(self):
        print(self.averageSalary)
        print(self.costOfLivingIndex)
        print("RATIO" + str(float(self.averageSalary)/float(self.costOfLivingIndex)))
        self.salaryCostRatio = float(self.averageSalary)/float(self.costOfLivingIndex)