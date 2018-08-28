import heapq


class Locations:

    locations = []
    numberOfLocations = 0
    top10 = []
    min = None
    max = None



    def __init__(self):
        self.locations = []
        self.numberOfLocations = 0

    def __lt__(self, other):
        return self.getSalaryCostRatio() < other.getSalaryCostRatio()


    def addLocation(self, location):
        self.locations.append(location)


        if (self.numberOfLocations == 0):
            self.min = location
            self.max = location

        elif (len(self.top10) < 10):
            self.top10.append(location)
            if (location.getSalaryCostRatio() > self.max.getSalaryCostRatio()):
                self.max = location
            if (location.getSalaryCostRatio() < self.min.getSalaryCostRatio()):
                self.min = location
        else:
            if (location.getSalaryCostRatio() > self.min.getSalaryCostRatio()):
                if (location.getSalaryCostRatio() > self.max.getSalaryCostRatio()):
                    self.max = location
                self.top10.remove(self.min)
                self.top10.append(location)
                tmin = self.max
                for i in self.top10:
                    if (i.getSalaryCostRatio() < tmin.getSalaryCostRatio()):
                        tmin = i
                self.min = tmin
        self.numberOfLocations += 1
    def getLocations(self):
        return self.locations


    def getNumberOfLocations(self):
        return self.numberOfLocations


    def getTop10(self):
        return self.top10



'''
        print(location.getSalaryCostRatio())
        heapq.heappush(self.top10, location)
        self.top10 = self.top10[:10]
'''




'''
        if (len(self.top10) < 10):
            self.top10.append(location)
            if (location.getCostOfLivingIndex() > self.max.getSalaryCostRatio()):
                self.max = location
            if (location.getCostOfLivingIndex() < self.min.getSalaryCostRatio()):
                self.min = location
        else:
            if (location.getCostOfLivingIndex() > self.min.getSalaryCostRatio()):
                self.top10.remove(min)
                self.top10.append(location)
                tmin = self.max.getSalaryCostRatio()
                for i in self.top10:
                    if (i.getSalaryCostRatio()):



            if (location.getCostOfLivingIndex() < self.min):
                self.min = location.getCostOfLivingIndex()
        '''


