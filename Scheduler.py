# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:17:29 2020

@author: liatn
"""
from Machine import Machine
from JobType import JobType
class Scheduler:
    
    def __init__(self, machines_num):
        self.machines = self.createMachineList(machines_num)
        self.type1_jobs = {}
        self.type2_jobs = {}
        
    def createMachineList(self, machines_num):
        self.machines = []
        for index in range(machines_num):
            machine = Machine(index)
            self.machines.append(machine)
            
    def addJobToDict(self,job):
        if job.job_type == JobType.TYPE_1:
            self.type1_jobs[job.index] = job
        elif job.job_type == JobType.TYPE_2:
            self.type2_jobs[job.index] = job
            

        
            
            