# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:17:29 2020

@author: liatn
"""
from Machine import Machine

from JobType import JobType



class Scheduler:
    
    def __init__(self, machines_num):       
        self.createMachineList(machines_num)
        self.j1_jobs = {}
        self.j2_jobs = {}
        self.makespan = 0
        
    def createMachineList(self, machines_num):    
        self.machines = []
        for index in range(machines_num):
            machine = Machine(index)
            self.machines.append(machine)
    
    def isLegal(self):
        for m in self.machines:
            if not m.is_legal:
                return False
        return True
    
    def addJobToDict(self,job):
        if job.job_type == JobType.TYPE_1:
            self.j1_jobs[job.index] = job
        elif job.job_type == JobType.TYPE_2:
            self.j2_jobs[job.index] = job
    
    def printStatus(self):
        i = 1
        for machine in self.machines:
            print("machine m{} : {}, details:".format(i,machine.load, machine.printJobs()))
            i+=1
            
    def isJobsListLegal(self):
        if (2*len(self.j1_jobs.keys())) == len(self.j2_jobs.keys()):
            return True
        return False
            
    
            
            
            
            



        
            
            