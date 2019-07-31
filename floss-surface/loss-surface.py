import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import os
EPS = np.float(1e-6)
THIS_DIR = os.path.abspath(os.path.dirname(__file__))

def sigmoid(x):
    return np.float(1) / (1 + np.exp(-x))

def floss(x, y, GT):
    TP = GT[0]*x + GT[1]*y
    FP = (1-GT[0])*x + (1-GT[1])*y
    FN = GT[0]*(1-x) + GT[1]*(1-y)
    p = TP / (TP + FP + EPS)
    r = TP / (TP + FN + EPS)
    return 1 - 2*p*r/(p+r)

def log_floss(x, y, GT):
    TP = GT[0]*x + GT[1]*y
    FP = (1-GT[0])*x + (1-GT[1])*y
    FN = GT[0]*(1-x) + GT[1]*(1-y)
    p = TP / (TP + FP + EPS)
    r = TP / (TP + FN + EPS)
    
    return -np.log(2*p*r/(p+r))

def celoss(x, y, GT):
    def loss(y1, gt1):
        return -(gt1*np.log(y1) + (1 - gt1) * np.log(1 - y1))
    return loss(x, GT[0]) + loss(y, GT[1])
    
        

# y = 1
# x = np.arange(-0.1, 1.1, 0.01)

# tp = y*x
# fp = y*(1-x)
# fn = (1-y) * x
# p = tp / (tp+fp)
# r = tp / (tp + fn)
# f = 2*p*r/(p+r)
# plt.plot(1-f, x)
# plt.hold(True)
# plt.plot(np.arange(0.01, 1, 0.01), -np.log(np.arange(0.01, 1, 0.01)))
# plt.grid(True)

#=====================================================================
# loss function surface
#=====================================================================
def set_spines(ax, lw=2):
    ax.spines['top'].set_linewidth(lw)
    ax.spines['right'].set_linewidth(lw)
    ax.spines['bottom'].set_linewidth(lw)
    ax.spines['left'].set_linewidth(lw)
colormap = cm.jet
fontsiz = 25
fig = plt.figure(figsize=(60, 36))
# GT 1 0
GT = np.array([1, 0])
x0 = np.arange(-5, 5, 0.5)
x1 = np.arange(-5, 5, 0.5)
x0 = sigmoid(x0)
x1 = sigmoid(x1)
X0, X1 = np.meshgrid(x0, x1)
fl = np.array([floss(x0, x1, GT) for x0,x1 in zip(np.ravel(X0), np.ravel(X1))])
fl = fl.reshape(X0.shape)

# GT = [1, 0]  FLoss
ax = fig.add_subplot(231, projection='3d')
ax.set_zlim(0, 1.01)
ax.set_xlabel("$\\hat{y}[1]$", fontsize=fontsiz+4, labelpad=28)
ax.set_ylabel("$\\hat{y}[0]$", fontsize=fontsiz+4, labelpad=28)
ax.set_zlabel("$FLoss$", fontsize=fontsiz, labelpad=10)
surf_fl = ax.plot_surface(X0, X1, fl, cmap=colormap)
ax.tick_params(axis='x', labelsize=fontsiz)
ax.tick_params(axis='y', labelsize=fontsiz)
ax.tick_params(axis='z', labelsize=fontsiz)

# # GT = [1, 0] Log-Floss
ax = fig.add_subplot(232, projection='3d')
logfl = np.array([log_floss(x0, x1, GT) for x0,x1 in zip(np.ravel(X0), np.ravel(X1))])
logfl = logfl.reshape(X0.shape)
ax.tick_params(axis='x', labelsize=fontsiz)
ax.tick_params(axis='y', labelsize=fontsiz)
ax.tick_params(axis='z', labelsize=fontsiz)
ax.set_zlim(0, 5)
ax.set_xlabel("$\\hat{y}[1]$", fontsize=fontsiz+4, labelpad=28)
ax.set_ylabel("$\\hat{y}[0]$", fontsize=fontsiz+4, labelpad=28)
ax.set_zlabel("$Log-Floss$", fontsize=fontsiz, labelpad=10)
surf_logfl = ax.plot_surface(X0, X1, logfl, cmap=colormap)


# GT = [1, 0] CELoss
ax = fig.add_subplot(233, projection='3d')
cel = np.array([celoss(x0, x1, GT) for x0,x1 in zip(np.ravel(X0), np.ravel(X1))])
cel = cel.reshape(X0.shape)
ax.tick_params(axis='x', labelsize=fontsiz)
ax.tick_params(axis='y', labelsize=fontsiz)
ax.tick_params(axis='z', labelsize=fontsiz)
ax.set_zlim(0, 10)
ax.set_xlabel("$\\hat{y}[1]$", fontsize=fontsiz+4, labelpad=28)
ax.set_ylabel("$\\hat{y}[0]$", fontsize=fontsiz+4, labelpad=28)
ax.set_zlabel("$CELoss$", fontsize=fontsiz, labelpad=10)
surf_cel = ax.plot_surface(X0, X1, cel, cmap=colormap)

# GT 1 1
GT = np.array([1, 1])
x0 = np.arange(-5, 5, 0.5)
x1 = np.arange(-5, 5, 0.5)
x0 = sigmoid(x0)
x1 = sigmoid(x1)
X0, X1 = np.meshgrid(x0, x1)
fl = np.array([floss(x0, x1, GT) for x0,x1 in zip(np.ravel(X0), np.ravel(X1))])
fl = fl.reshape(X0.shape)
cel = np.array([celoss(x0, x1, GT) for x0,x1 in zip(np.ravel(X0), np.ravel(X1))])
cel = cel.reshape(X0.shape)

# GT 1 1 FLoss
ax = fig.add_subplot(234, projection='3d')
ax.set_zlim(0, 1.01)
ax.set_xlabel("$\\hat{y}[1]$", fontsize=fontsiz+4, labelpad=28)
ax.set_ylabel("$\\hat{y}[0]$", fontsize=fontsiz+4, labelpad=28)
ax.set_zlabel("$FLoss$", fontsize=fontsiz, labelpad=10)
ax.tick_params(axis='x', labelsize=fontsiz)
ax.tick_params(axis='y', labelsize=fontsiz)
ax.tick_params(axis='z', labelsize=fontsiz)
surf_fl = ax.plot_surface(X0, X1, fl, cmap=colormap)

# # GT = [1, 1] Log-Floss
ax = fig.add_subplot(235, projection='3d')
logfl = np.array([log_floss(x0, x1, GT) for x0,x1 in zip(np.ravel(X0), np.ravel(X1))])
logfl = logfl.reshape(X0.shape)
ax.tick_params(axis='x', labelsize=fontsiz)
ax.tick_params(axis='y', labelsize=fontsiz)
ax.tick_params(axis='z', labelsize=fontsiz)
ax.set_zlim(0, 5)
ax.set_xlabel("$\\hat{y}[1]$", fontsize=fontsiz+4, labelpad=28)
ax.set_ylabel("$\\hat{y}[0]$", fontsize=fontsiz+4, labelpad=28)
ax.set_zlabel("$Log-Floss$", fontsize=fontsiz, labelpad=10)
surf_logfl = ax.plot_surface(X0, X1, logfl, cmap=colormap)


# GT 1 1  CELoss
ax = fig.add_subplot(236, projection='3d')
ax.set_xlabel("$\\hat{y}[1]$", fontsize=fontsiz+4, labelpad=28)
ax.set_ylabel("$\\hat{y}[0]$", fontsize=fontsiz+4, labelpad=28)
ax.set_zlabel("$CELoss$", fontsize=fontsiz, labelpad=10)
ax.set_xticks(np.arange(0, 1.1, 0.2))
ax.set_yticks(np.arange(0, 1.1, 0.2))
ax.set_zlim(0, 10)
ax.tick_params(axis='x', labelsize=fontsiz)
ax.tick_params(axis='y', labelsize=fontsiz)
ax.tick_params(axis='z', labelsize=fontsiz)
surf_cel = ax.plot_surface(X0, X1, cel, cmap=colormap)



plt.tight_layout(pad=20)
fig.savefig(os.path.join(THIS_DIR, 'loss-surface.pdf'))
