import csv
import os
from Scraper import scraper

if __name__ == "__main__":

    # Retrieves job data and puts it in a CSV file
    jobPlace = scraper()
    job = jobPlace[0]
    location = jobPlace[1]

    current_loation = os.getcwd()
    with open(current_loation + '\\' + job + '-' + location + '-job-results.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
