#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:13:48 2022

@author: jose
"""

import numpy as np

def minimo(a, b):
    return np.minimum(a, b)

def algebrico(a, b):
    return a * b

def limitado(a, b):
    return np.maximum(0, a + b - 1)

def drastico(a, b):
    mu = np.zeros(shape = a.shape)
    # for i in range(len(a)):
    #     if a[i] == 1:
    #         mu[i] = b[i]
    #     elif b[i] == 1:
    #         mu[i] = a[i]
    #     else:
    #         continue
    azero = (a == 1) # era pra chamar aum, ne? mas aproveitei do uniao xd
    bzero = (b == 1)
    mu[azero] = b[azero]
    mu[bzero] = a[bzero]
    
    return mu
