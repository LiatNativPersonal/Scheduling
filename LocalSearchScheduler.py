# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:39:32 2020

@author: liatn
"""
from Scheduler import Scheduler

import random


class LocalSearchScheduler(Scheduler):
    
    def __init__(self, machines_num):
        Scheduler.__init__(self, machines_num)
        
    def scheduleAllOnOneMachine(self):
        machine = self.machines[0]
        for job in self.type1_jobs.values():  
            machine.allocateJob(job)
            
        for job in self.type2_jobs.values():
            machine.allocateJob(job)
        self.makespan = self.machines[0].load
        self.max_load = self.machines[0]
        self.min_load = self.machines[1]
            
    def moveJobs(self):       
        jobs_to_move = random.sample(list(self.max_load.type1_jobs.values()),1)
        jobs_to_move += (random.sample(list(self.max_load.type2_jobs.values()),2))
        move_load = sum([x.proc_time for x in jobs_to_move])
        new_makespan = max(self.min_load.load + move_load, self.max_load.load - move_load)
        if (new_makespan < self.makespan):            
            for job in jobs_to_move:
                self.max_load.removeJob(job)
                self.min_load.allocateJob(job)
        self.makespan = new_makespan
       
        self.max_load = max(self.machines, key=lambda item: item.load)
        self.min_load = min(self.machines, key=lambda item: item.load)
        
    def swapJobs(self):
        print("not yet implemented")
        
        
    