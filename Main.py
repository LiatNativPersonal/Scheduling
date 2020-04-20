# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:46:50 2020

@author: liatn
"""

from LocalSearchScheduler import LocalSearchScheduler
import csv
from Job import Job
from JobType import JobType


JOBS_INPUT_FILE = "inputs/jobs.csv"

def Main():
    
    
    scheduler = LocalSearchScheduler(4)
#    scheduler.printStatus()
    with open(JOBS_INPUT_FILE) as jobs_file:
        reader = csv.reader(jobs_file, delimiter=',')
        for line in reader:
            job = Job(JobType.getJobTypeFromInt(int(line[0])), int(line[2]), int(line[1]))
            scheduler.addJobToDict(job)
        scheduler.scheduleAllOnOneMachine()
    scheduler.printStatus()
    
    current_makespan = scheduler.makespan
    scheduler.moveJobs()
    tries = 0
    while tries < 10 :
        current_makespan = scheduler.makespan
        scheduler.moveJobs()
        if not scheduler.isLegal():
            print("Ilegal schedule")
           
        if current_makespan <= scheduler.makespan:
            tries += 1
            print("next try")
            scheduler.printStatus()
    
   



if __name__ == '__main__':
    Main()