# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:31:58 2020

@author: liatn
"""

class Job:
    
    def __init__(self, job_type, processing_time, index):
        self.job_type = job_type
        self.proc_time = processing_time
        self.index = index
        
    def printJob(self):
        print("Job {}: Job Type={}, processing time={}".format(self.index, (self.job_type).name, self.proc_time))
        
    
        