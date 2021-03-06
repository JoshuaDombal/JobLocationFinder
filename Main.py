# Created by Josh Dombal
# Created August 22, 2018
#
#  This programs purpose is to display a list of the best locations to live based on the salary of
#    your job compared to the cost of living in a city.
#  Salary and Cost of Living data is scraped from the internet so that it is updated.



import csv
import os

from Job import Job
from Scraper import scraper
import re
from Location import Location
from Locations import Locations

# Calculates moving average
def movingAverage(avg, new_sample, n):
    avg -= avg / n
    avg += new_sample / n
    return avg

if __name__ == "__main__":



    # Saves locations and cost information
    colLocations = Locations()
    try:
        myFile = open('C:\\Users\\josh.dombal\\PycharmProjects\\JobLocationFinder\\costOfLiving', mode='r')

        f = open('locationInfo.txt', 'w')
        count = 0
        job1 = None
        # Runs through each line costOfLiving.txt and scrapes info about jobs for each location
        for line in myFile:
            count += 1
            locat = Location()
            #print(line)
            new = [x.strip() for x in line.split(',')]
            #print(new)
            # Splits the line by \t to extract data more easily
            for s in new:
                n = s.split('\t')
                if (len(n) == 2):
                    locat.setCity(n[1])
                    print("CITY *****: " + n[1])
                elif (len(n) == 1):
                    locat.setState(n[0])
                    print(" STATE +++++++++ "  + n[0])
                else:
                    if (n[0] == 'United States') :
                        locat.setCountry(n[0])
                        locat.setCostofLivingIndex(n[1])
                        #print(n[0])

                        print("ADDED ******************" + n[0])


                        # Retrieves job data and puts it in a CSV file
                        # print(l.getCity())

                        jobPlace = scraper(locat.getCity())
                        # If information regarding a city was able to be scraped from web
                        if (not (jobPlace[1] == -1)):
                            job1 = jobPlace[0]
                            loc = jobPlace[1]

                            current_loation = os.getcwd()
                            #location = Location()
                            averageSalary = 0
                            count = 0
                            average = 0

                            # Loops through each line in the CSV file
                            # Creates a Job object per line and adds each job to the specific Location object
                            with open(current_loation + '\\' + job1 + '-' + loc + '-job-results.csv') as csvfile:
                                readCSV = csv.reader(csvfile, delimiter=',')
                                for row in readCSV:

                                    numValueofSalary = re.findall(r'\d+', row[4])
                                    if (len(numValueofSalary) > 1):
                                        count += 1
                                        avg = (float(numValueofSalary[0]) + float(numValueofSalary[1])) / 2
                                        # print(avg)
                                        averageSalary = movingAverage(averageSalary, avg, count)
                                    job = Job(row[0], row[1], row[2], row[3], numValueofSalary)
                                    locat.addJob(job)
                                    locat.setAverageSalary(averageSalary)
                                locat.setSalaryCostRatio()
                                f.write(
                                    locat.getCity() + "," + str(locat.getAverageSalary()) + "," + str(locat.getCostOfLivingIndex()) + "," + str(locat.getSalaryCostRatio()))
                                f.write('\n')
                                print("Average salary: " + str(averageSalary))

                        colLocations.addLocation(locat)

        print("TOPS")
        fName = 'top10' + "-" + job1 + ".txt"
        topPicks = open(fName, 'w')
        colLocations.getTop10().sort(key=lambda a: a.salaryCostRatio, reverse=True)
        for top in colLocations.getTop10():
            topPicks.write(top.getCity() + ", " + top.getState() + ", " + str(top.getSalaryCostRatio()) + "             Average Salary: " + str(top.getAverageSalary()) + "            Cost of Living Index: " + str(top.getCostOfLivingIndex()))
            topPicks.write('\n')

            print("City: " + top.getCity() + ", " + top.getState() + "         Ratio: " + str(top.getSalaryCostRatio()) + "               Average Salary: " + str(top.getAverageSalary()) + "               Cost of Living Index: " + str(top.getCostOfLivingIndex()))

        print("_______________________________________________________________________")

        colLocations.getLocations().sort(key=lambda x: x.salaryCostRatio, reverse=True)
        for loc in colLocations.getLocations():
            print(loc.getCity() + ", " + str(loc.getSalaryCostRatio()) + "               Average Salary: " + str(top.getAverageSalary()))


        '''
        for l in colLocations.getLocations():
            if (count == 10):
                break
        '''

    except IOError:
        print("File not found")







