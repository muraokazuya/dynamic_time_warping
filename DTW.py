# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:24:53 2018

@author: Kazuya
"""

import numpy as np

def DTW(a,b): # Arrays a and b are 1D-time-series
    matrix=np.zeros((len(a)+1,len(b)+1)) #Cost matrix
    #Initialize cost map
    for i in range(1,len(a)+1):
        matrix[i,0]=np.inf
    for j in range(1,len(b)+1):
        matrix[0,j]=np.inf
    #Calculate cost map
    for i in range(len(a)):
        for j in range(len(b)):
            matrix[i+1,j+1]=abs(a[i]-b[j])+min(matrix[i,j],matrix[i+1,j],matrix[i,j+1])
    return matrix[len(a),len(b)]/(len(a)+len(b))
