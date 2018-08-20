

class Location:

    city = None
    averageSalary = None
    numberOfJobs = None
    jobs = []



    def __init__(self):
        self.city = None
        self.averageSalary = 0
        self.numberOfJobs = 0
        self.jobs = []


    def addJob(self, job):
        self.jobs.append(job)
        self.numberOfJobs += 1


    def getNumberOfJobs(self):
        return self.numberOfJobs

    def getJobs(self):
        return self.jobs

    def getAverageSalary(self):
        return self.averageSalary/len(self.jobs)






    # ************************   SETTERS    *************************** #

    def setAverageSalary(self, avgSalary):
        self.averageSalary = avgSalary

