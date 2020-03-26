# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:31:58 2020

@author: liatn
"""

from JobType import JobType

class Job:
    
    def __init__(self, job_type, processing_time):
        self.job_type = job_type
        self.proc_time = processing_time
        
    def printJob(self):
        print("Job Type: {}, processing time: {} \n".format((self.job_type).name), self.proc_time)
        
    
        