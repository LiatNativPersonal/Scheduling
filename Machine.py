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
        self.type1_jobs = []
        self.type2_jobs = []
        self.index = index

    def allocateJob(self, job):
        self.load += job.proc_time
        if job.job_type == JobType.TYPE_1:
            self.type1_jobs.append(job)
        elif job.job_type == JobType.TYPE_2:
            self.type2_jobs.append(job)
        self.is_legal = (len(self.type1_jobs) == len(self.type2_jobs))