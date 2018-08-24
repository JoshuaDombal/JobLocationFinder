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

    # Retrieves job data and puts it in a CSV file
    jobPlace = scraper()
    job = jobPlace[0]
    loc = jobPlace[1]

    current_loation = os.getcwd()
    location = Location()
    averageSalary = 0
    count = 0
    average = 0

    # Loops through each line in the CSV file
    # Creates a Job object per line and adds each job to the specific Location object
    with open(current_loation + '\\' + job + '-' + loc + '-job-results.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:

            numValueofSalary = re.findall(r'\d+', row[4])
            if (len(numValueofSalary) > 1):
                count += 1
                avg = (float(numValueofSalary[0]) + float(numValueofSalary[1]))/2
                print(avg)
                averageSalary = movingAverage(averageSalary, avg, count)
            job = Job(row[0], row[1], row[2], row[3], numValueofSalary)
            location.addJob(job)
            location.setAverageSalary(averageSalary)
            #print("Average salary" + str(averageSalary))

    # Saves locations and cost information
    try:
        myFile = open('C:\\Users\\josh.dombal\\PycharmProjects\\JobLocationFinder\\costOfLiving', mode='r')
        colLocations = Locations()
        for line in myFile:
            locat = Location()
            print(line)
            new = [x.strip() for x in line.split(',')]
            print(new)
            for s in new:
                n = s.split('\t')
                if (len(n) == 2):
                    locat.setCity(n[1])
                    print(n[1])
                elif (len(n) == 1):
                    locat.setState(n[0])
                    print(n[0])
                else:
                    locat.setCostofLivingIndex(n[1])
                    print(n[1])
            colLocations.addLocation(locat)
            #n = [x.strip() for x in new.split('\t')]
            #print(n)

    except IOError:
        print("File not found")




