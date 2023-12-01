# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:09:00 2023

@author: Jian Zhang
"""

import argparse
import matplotlib.pyplot as plt
import matplotlib
import math
from matplotlib import rcParams

matplotlib.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['figure.dpi'] = 100

config = {
    "mathtext.fontset": 'stix',
    "font.size": 14
    }
rcParams.update(config)

def get_xyz(lines):
    x = []
    y = []
    for line in lines:
        if ("#" in line) or ("@" in line):
            continue
        x.append(eval(line.strip().split()[0]))
        y.append(eval(line.strip().split()[1]))
    return x, y
parser = argparse.ArgumentParser(description="draw RDF and Coordination from xvg file.")
parser.add_argument("-rdf", dest="rdf_file", type=str, help="the path of RDF file")
parser.add_argument("-coor", dest="coor_file", type=str, help="the path of Coordination number file")
# parser.add_argument("-ref", dest="ref", type=str, help="the name of reference atoms")
# parser.add_argument("-sel", dest="sel", type=str, help="the name of selection atoms")
args = parser.parse_args()
f1 = open(args.rdf_file, "r", encoding="utf-8")
lines1 = f1.readlines()
f1.close()
rdf_leg, rdf = get_xyz(lines1)
f2 = open(args.coor_file, "r", encoding="utf-8")
lines2 = f2.readlines()
f2.close()
coor_leg, coor = get_xyz(lines2)
fig, ax = plt.subplots()
ax.plot(rdf_leg, rdf, label="RDF", color="#BEB8DC")
ax.set_xlabel(r'$\mathit{r}$'+"(nm)")
ax.set_ylabel(r'$\mathit{g}$'+'('+r'$\mathit{r}$'+')')
ax.set_xlim(xmin=min(rdf_leg), xmax=max(rdf_leg))
z_ax = ax.twinx()
z_ax.plot(coor_leg, coor, "--", label="Coordination number", color="#FA7F6F")
z_ax.set_ylabel("coordination number")
plt.show(block=True)

    

