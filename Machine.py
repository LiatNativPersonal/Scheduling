# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:39:26 2020

@author: liatn
"""
from JobType import JobType

class Machine:
    
    def __init__(self, index):
        self.load = 0
        self.is_legal = True
        self.j1_jobs = {}
        self.j2_jobs = {}
        self.index = index

    def allocateJob(self, job):        
        if job.job_type == JobType.J1:
            self.j1_jobs[job.index] = job
        elif job.job_type == JobType.J2:
            self.j2_jobs[job.index] = job
        self.setIsLegal()
        self.updateLoad(job.proc_time)
        
    def removeJob(self,job):        
        if job.job_type == JobType.J1:
            self.j1_jobs.pop(job.index)
        elif job.job_type == JobType.J2:
            self.j2_jobs.pop(job.index)
        self.setIsLegal()
        self.updateLoad((-1)*job.proc_time)
        
    def setIsLegal(self):
        if  (2*(len(self.j1_jobs.keys()))) == len(self.j2_jobs.keys()):
            self.is_legal = True
        else:
            self.is_legal = False
    
    def printJobs(self):
        for job in self.j1_jobs.values():
            job.printJob()
        for job in self.j2_jobs.values():
            job.printJob()
        
    def updateLoad(self, update):
        self.load += update
        

        
            
        