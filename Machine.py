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
        self.type1_jobs = {}
        self.type2_jobs = {}
        self.index = index

    def allocateJob(self, job):
        self.load += job.proc_time
        if job.job_type == JobType.TYPE_1:
            self.type1_jobs[job.index] = job
        elif job.job_type == JobType.TYPE_2:
            self.type2_jobs[job.index] = job
        self.setIsLegal()
        self.updateLoad(self, job.proc_time)
        
    def removeJob(self,job):
        self.load -= job.proc_time
        if job.job_type == JobType.TYPE_1:
            self.type1_jobs.pop(job.index)
        elif job.job_type == JobType.TYPE_2:
            self.type2_jobs.pop(job.index)
        self.setIsLegal()
        self.updateLoad(self, (-1)*job.proc_time)
        
    def setIsLegal(self):
        self.is_legal = (len(self.type1_jobs.keys) == len(self.type2_jobs.keys))
        
    def updateLoad(self, update):
        self.load += update
        

        
            
        