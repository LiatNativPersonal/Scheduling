# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:29:20 2020

@author: liatn
"""

from enum import Enum

class JobType(Enum):
    J1 = 1
    J2 = 2
    
    def getJobTypeFromInt(intJobType):
        if intJobType == 1:
            return JobType.J1
        elif intJobType == 2:
            return JobType.J2
        else:
            return 0