from numpy import sum, power, array, pi, exp, subtract, divide, argmin, log, mean, sqrt, logspace, linspace, trace
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.font_manager import FontProperties 
from scipy.optimize import curve_fit
from scipy.ndimage import gaussian_filter
from os import listdir
from os.path import isfile, join
from time import time


# constants of the universe
mu_0 = 4 * pi * 10.**-7
hbar = 1.0545718 * 10.**-34
c = 299792458
mu_b = hbar * 2 * pi * 1.39962460 * 10.**6
k_b = 1.38 * 10**-23

# sodium constants
Isat = 6.26 * 10
Gamma = 2 * pi * 9.7946 * 10.**6
f0 = 508.8487162 * 10.**12
k = 2 * pi * f0 / c
m = 22.989769 * 1.672623 * 10**-27
g_f = 0.5

def two_exp(t, N, tau_1, tau_2, z_0):
    return N * ( exp(-t / tau_1) + exp(-t / tau_2) ) + z_0

def one_exp(t, N, tau_1):
    return N * (1- exp(-t / tau_1) )

def main():
    times = array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
    
    Ns = array([0,326.5,503,650.3,793.8,836.7,943.2,950.8,913,880.9,914.7])
    
    popt, pcov = curve_fit(one_exp, times, Ns, bounds = ( (0, 0), (1500, 1000) ) )
    print(popt, sqrt(pcov[0,0]), sqrt(pcov[1,1]))
    
    time_p = linspace(0, 5)
    
    plt.scatter(times, Ns)
    
    plt.plot( time_p, one_exp( time_p, popt[0], popt[1] ) )
    
    plt.show()

if __name__ == "__main__":
    main()