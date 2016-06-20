""" Plots the theoretical SIR curve """

import sys
import os.path as path

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

thisdir = path.dirname(path.realpath(__file__))
sys.path.append(path.join(thisdir, "../"))

N = 100
beta = 0.1
gamma = 0.01

# Y=(S_1, I_1, R_1)
def solver(Y, t):
    return [- beta / N * Y[1] * Y[0],
            beta / N * Y[1] * Y[0] - gamma * Y[1],
            gamma * Y[1] ]

start_infection = 10
t = np.arange(0, 365, 0.01)
asol = integrate.odeint(solver, [N - start_infection,
                                 start_infection,
                                 0], t)
plt.figure(figsize=(12, 8))
plt.plot(t, asol[:, 0], ls='-', color='g')
plt.plot(t, asol[:, 1], ls='-', color='r')
plt.plot(t, asol[:, 2], ls='-', color='b')
plt.legend(["Susceptible", "Infected", "Recovered"], loc=7)
plt.title("Theorical SIR. N={0:d}, Beta={1:.2f}, Gamma={2:.2f}".format(
    N, beta, gamma
))
plt.xlabel("Time")
plt.ylabel("# of individuals")
plt.savefig(path.join(thisdir, '../../report/plots/sir_one_region.pdf'),
            format='pdf', dpi=1000, bbox_inches='tight')
