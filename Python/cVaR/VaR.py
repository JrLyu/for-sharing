import numpy as np
import pandas as pd
import xlrd as xlrd
from scipy.stats import norm
from scipy.stats import norm
import yfinance as yf


## S_{t+1}=S_t+S_t(\mu\Delta t+\varepsilon\sigma\sqrt{\Delta t})
def VolTime(t, vol):
    if t == time3:
        vol_time = vol * np.sqrt(time3)
    elif t == time5:
        vol_time = vol * np.sqrt(time5)
    elif t == time7:
        vol_time = vol * np.sqrt(time7)
    elif t == time2:
        vol_time = vol * np.sqrt(time2)
    elif t == time1:
        vol_time = vol * np.sqrt(time1)
    else:
        vol_time = vol * np.sqrt(time6mo)
    return vol_time

def MeanTime(t, mean):
    if t == time3:
        mean_time = mean * time3     
    elif t == time5:
        mean_time = mean * time5
    elif t == time7:
        mean_time = mean * time7 
    elif t == time2:
        mean_time = mean * time2
    elif t == time1:
        mean_time = mean * time1
    else:
        mean_time = mean * time6mo
    return mean_time
    
# Define several delta t
time3 = 1 / (252 * 3)  
time5 = 1 / (252 * 5)
time7 = 1 / (252 * 7)
time2 = 1 / (252 * 2)
time1 = 1 / (252)
time6mo = 1 / (126)