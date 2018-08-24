

class Location:

    city = None
    state = None
    averageSalary = None
    numberOfJobs = None
    jobs = []

    costOfLivingIndex = None
    salaryCostRatio = None



    def __init__(self):
        self.city = None
        self.state = None
        self.averageSalary = 0
        self.numberOfJobs = 0
        self.jobs = []
        self.costOfLivingIndex = 0
        self.salaryCostRatio = 0



    def getNumberOfJobs(self):
        return self.numberOfJobs

    def getJobs(self):
        return self.jobs

    def getAverageSalary(self):
        return self.averageSalary/len(self.jobs)

    # ************************   SETTERS    *************************** #

    def addJob(self, job):
        self.jobs.append(job)
        self.numberOfJobs += 1

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.city = state

    def setAverageSalary(self, avgSalary):
        self.averageSalary = avgSalary

    def setCostofLivingIndex(self, colIndex):
        self.costOfLivingIndex = colIndex

    def setSalaryCostRatio(self):
        self.salaryCostRatio = self.averageSalary/self.costOfLivingIndex