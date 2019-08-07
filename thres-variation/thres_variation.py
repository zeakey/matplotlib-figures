#coding:utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import linecache
from os.path import join, splitext, split, isfile
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
print(THIS_DIR)
if not os.path.isdir(os.path.join(THIS_DIR, 'figures')):
  os.makedirs(os.path.join(THIS_DIR, 'figures'))

def plotErrorbar(numx, mean, std):

    # example data
    x = np.arange(0,numx,1)
    print(numx, x)
    colors = ['b', 'b', "g",'g',  'r', 'r']
    lss = ['--', '-', "--",'-',  '--', '-']
    methods = ["DHS","F-DHS","Almuet","F-Amulet","DSS","F-DSS"]
    fig, ax = plt.subplots(figsize=(10,8))
    plt.grid(True)
    ax = plt.gca() 
    #ax.bar(x, mean, alpha=0.5, color=colors)
    ax.margins(0.05)
    for pos, y, err, ls, color in zip(x, mean, std, lss,colors):
        eb=ax.errorbar(pos, y, err, lw=2, marker='o', elinewidth=6, mew=10, capsize=15, capthick=1,color=color) 
        eb[-1][0].set_linestyle(ls)
    ax.xaxis.labelpad = 0
    plt.xticks(x, methods, rotation=15)
    #plt.xlabel("Methods",fontsize=26)
    plt.ylabel("Threshold Variance",fontsize=26)
    ymin = 0.68
    ymax = 1.03
    ax.set_ylim([ymin, ymax])
    ax.set_xlim([-0.5, 5.5])
    ax.tick_params(axis='x', labelsize=26)
    ax.tick_params(axis='y', labelsize=26)
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    # grid
    xmajor_ticks = np.arange(0, 5.5, 1)
    xminor_ticks = np.arange(0, 5.5, 1)
    ymajor_ticks = np.arange(ymin, ymax, 0.08)
    yminor_ticks = np.arange(ymin, ymax, 0.04)
    ax.set_xticks(xmajor_ticks)
    ax.set_xticks(xminor_ticks, minor=True)
    ax.set_yticks(ymajor_ticks)
    ax.set_yticks(yminor_ticks, minor=True)
    ax.grid(which='minor', alpha=1, linestyle='dotted', linewidth=2, color='black')
    ax.grid(which='major', alpha=1, linestyle='dotted', linewidth=2, color='black')
    plt.tight_layout()
    plt.savefig(join(THIS_DIR, 'thres-variation.svg'))



def drawThs(Result_Root,names,datasets,methods):
  p = np.zeros([len(names),255])
  r = np.zeros([len(names),255])
  f = np.zeros([len(names),255])
  thresmean = np.zeros(len(methods),dtype=np.float32)
  thresE = np.zeros(len(methods),dtype=np.float32)
  ths = np.zeros(255,dtype=np.float32)
  maxfthres=np.zeros([len(names)])
  maxf=np.zeros([len(names)])
  for ni in range(len(names)):
    FmeasureResult=join(Result_Root,names[ni])
    fmlist=open(FmeasureResult,'r')
    fm=fmlist.readlines()

    for i in range(1,256):
      oneline = fm[i].split()
      p[ni,i-1]=oneline[5]
      r[ni,i-1]=oneline[7]
      f[ni,i-1]=oneline[9]
      if f[ni,i-1]>maxf[ni]:
        maxf[ni] = f[ni,i-1]
        maxfthres[ni] = i
      ths[i-1]=float(i)/255
    #print names[ni],maxf[ni],maxfthres[ni]
    for mi in range(len(methods)):
        if names[ni].split('_')[0]==methods[mi]:
          if names[ni].split('.')[0].split('_')[1] in datasets:
            thresmean[mi]+=maxfthres[ni]/255.0
  thresmean/=len(datasets)
  for ni in range(len(names)):
    for mi in range(len(methods)):
        if names[ni].split('_')[0]==methods[mi]:
          if names[ni].split('.')[0].split('_')[1] in datasets:
            print(names[ni],":",maxfthres[ni],"-",thresmean[mi])
            thresE[mi]+=(maxfthres[ni]/255.0-thresmean[mi])*(maxfthres[ni]/255.0-thresmean[mi])
  thresE = np.sqrt(thresE/len(datasets))
  print(thresmean)
  print(thresE)
  print(methods)
  plotErrorbar(len(methods),thresmean,thresE)

  
Result_Root="thres_variation-data"
names=os.listdir(Result_Root)
subnames=[]
datasets=["ECSSD","DUT-OMRON","HKU-IS","PASCALS"]
#datasets=["SOD"]
methods=["dhs","fdhs","amulet","famulet","dss","floss"]

drawThs(Result_Root,names,datasets,methods)

