#coding:utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import linecache, os
from os.path import join, splitext, split, isfile, abspath
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
specified = True
if specified:
  txts = ['amulet_ECSSD', 'amulet_floss', 'dhs_ECSSD.txt', 'fdhs_ECSSD.txt', 'dss_ECSSD.txt', 'DSS_floss_ECSSD.txt']#, "rfcn_ECSSD.txt", "dcl_ECSSD.txt"]
  legends = ["Amulet", "Amulet+FLoss", "DHS","DHS+FLoss", "DSS" ,"DSS+FLoss"]#, "RFCN", "DCL"]
  colors = ["g--",'g-', 'b--', 'b-', 'r--', 'r', 'm--', 'y--']
  txts = [join(THIS_DIR, 'f-thres-data', i) for i in txts]
else:
  txts = [splitext(i)[0] for i in os.listdir(join(THIS_DIR, 'f-thres-data'))]
  legends = txts
assert len(txts) == len(legends)
# append '.txt' to txt filenames (if not containing)
for i in range(len(txts)):
  t = txts[i]
  if '.txt' not in t:
    txts[i] = txts[i] + ".txt"

def read_data(txt_filename):
  assert isfile(txt_filename), "%s doesn't exist!" % txt_filename
  data = np.zeros((255, 3), dtype=np.float32)
  with open(txt_filename, 'r') as txt:
    lines = txt.readlines()
    for i in range(1, 256):
      l = lines[i].split()
      data[i-1, 0] = float(l[5])
      data[i-1, 1] = float(l[7])
      data[i-1, 2] = float(l[9])
  return data

def draw_method(data, color, fig):
  assert data.ndim == 2
  assert data.shape[0] == 255 and data.shape[1] == 3
  plt.plot(np.linspace(0, 1, 255), data[:, 2], color, linewidth=4)

fig = plt.figure(figsize=(10, 8))
maxF = float(-1)
for idx, txt in enumerate(txts):
  data = read_data(txt)
  if data[:, 2].max() >= maxF:
    maxF = data[:, 2].max()
  draw_method(data, colors[idx], fig)
# adjust figure style
ax = plt.gca()
ymin = 0.80
ymax = maxF+0.001
ax.set_ylim([ymin, ymax])
ax.set_xlim([0, 1])
# sticks font size
ax.tick_params(axis='x', labelsize=26)
ax.tick_params(axis='y', labelsize=26)
# box border width
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
# legends
#plt.legend(legends, fontsize=22, loc="lower center")
plt.legend(legends, fontsize=22, loc="lower center")

# grid
xmajor_ticks = np.arange(0, 1.01, 0.2)
xminor_ticks = np.arange(0, 1.01, 0.1)
ymajor_ticks = np.arange(ymin, ymax, 0.02)
yminor_ticks = np.arange(ymin, ymax, 0.01)
ax.set_xticks(xmajor_ticks)
ax.set_xticks(xminor_ticks, minor=True)
ax.set_yticks(ymajor_ticks)
ax.set_yticks(yminor_ticks, minor=True)
ax.grid(which='minor', alpha=1, linestyle='dotted', linewidth=2, color='black')
ax.grid(which='major', alpha=1, linestyle='dotted', linewidth=2, color='black')
#plt.grid(alpha=1, linestyle='dotted', linewidth=2, color='black')  
# xlabel and ylabel
ax.set_xlabel("Threshold", fontsize=26)
ax.set_ylabel("F-measure", fontsize=26)
plt.tight_layout()
# plt.tight_layout(pad=0.4, w_pad=16, h_pad=3.0)
# save figure into pdf format
plt.savefig(join(THIS_DIR, 'f-thres.svg'))
