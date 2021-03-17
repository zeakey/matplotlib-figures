import numpy as np 
import matplotlib.pyplot as plt
import os
from os.path import dirname, join
THIS_DIR = dirname(__file__)
#Resnet56 cifar10 0.1-0.7
da_acc_mean = np.array([94.363, 94.097, 94.222, 93.86, 93.622, 92.68])
da_acc_std = np.array([0.158, 0.075, 0.243, 0.19, 0.160, 0.15])
slimming_acc_mean = np.array([93.778, 93.650, 93.604, 93.330, 92.897, 91.940])#, 41.326])
slimming_acc_std = np.array([0.185, 0.188, 0.126, 0.136, 0.139, 0.102])#, 38.367])


fig = plt.figure(figsize=(7,4))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0)

plt.grid(which='both', color="black", linestyle="dotted", linewidth=1, alpha=0.8)

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

plt.ylabel('Accuracy', fontsize=14)

plt.plot(x, da_acc_mean - da_acc_std, color="darkblue",linewidth=1,linestyle='--')
plt.plot(x, da_acc_mean + da_acc_std, color="darkblue",linewidth=1,linestyle='--')
y0 = plt.plot(x, da_acc_mean, color="darkblue",linewidth=1,linestyle='-', marker='o', label='Ours')
plt.fill_between(x, da_acc_mean - da_acc_std, da_acc_mean + da_acc_std, facecolor='darkblue', alpha=0.2)

plt.plot(x, slimming_acc_mean - slimming_acc_std, color="forestgreen",linewidth=1,linestyle='--')
plt.plot(x, slimming_acc_mean + slimming_acc_std, color="forestgreen",linewidth=1,linestyle='--')
y1 = plt.plot(x, slimming_acc_mean, color="forestgreen",linewidth=1,linestyle='-', marker='o', label='Slimming')
plt.fill_between(x, slimming_acc_mean - slimming_acc_std, slimming_acc_mean + slimming_acc_std, facecolor='forestgreen', alpha=0.2)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.legend(loc='lower left', fontsize=14)

plt.tight_layout()
save_path = join(THIS_DIR, "sensitivity.svg")
plt.savefig(save_path)
