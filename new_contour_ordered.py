"To call functions, tools from Library"
from __future__ import print_function
import datetime
import numpy as np
from matplotlib import cm, pyplot as plt
from hmmlearn.hmm import GaussianHMM, GMMHMM
from hmmlearn.base import _BaseHMM
from mpl_toolkits.mplot3d import Axes3D
import os
# from Cython.Includes.libcpp import pair


"To call function of output Data"
import os,sys
# import subprocess
# import glob
# from os import path


"INPUT"
#number of state
n = 16
#covariance type
covar_type = "full"
#number of iteration
iterr = 1000
#figure name
figname1 = "RTV600mVCurrent9n%d" % n
# figname2 = "result__foldernameanalysis1_3d_scatterplot"
figname3 = "colormapplot_1"
# figname4 = "result__analysis1_colormapplot_2"

script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'HH4/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

# "Output Data"
# f = open(results_dir + 'RTV600mVCurrent9;n16;output.txt','w')
# sys.stdout = f

"Import data from excel file"
from xlrd import open_workbook
book = open_workbook('Data2.xlsx')
sheet = book.sheet_by_index(4)

"Input"
#start_time
start_t = 0
#end_time
end_t = sheet.nrows

x = []
y = []


for k in range(start_t,end_t):
    x.append(str(sheet.row_values(k)[0])) #[k] = row, [0] = column ke nol
    y.append(str(sheet.row_values(k)[1])) #[k] = row, [1] = column ke satu
 
x = np.asarray(map(float, x))
y = np.asarray(map(float, y))
 
X = np.reshape(y,(-1,1))
 
"Run Gaussian HMM"
# Make an HMM instance and execute fit
model = GaussianHMM(n_components=n, covariance_type=covar_type, n_iter=iterr).fit(X)
 
# Predict the optimal sequence of internal hidden state
hidden_states = model.predict(X)
print("Number of Rows")
print("--------------")
print(sheet.nrows)
print(" ")
print("Hidden States")
print("-------------")
print(hidden_states)

"ordered hidden states"
#to make list of means of each hidden states
means_state = []
means_state1 = []
for i in range(0,n):
    means_state.append(model.means_[i][0])
    means_state1.append(model.means_[i][0])

#to make the hidden states mean in well ordered
ind_mean_of_hiddenstates = []
for i in range(0,n):
    mm = min(means_state)
    mm_ind = means_state1.index(mm)
    means_state.remove(mm)
    ind_mean_of_hiddenstates.append([mm_ind,model.means_[mm_ind][0]])

"PRINT RESULT"
print("Record data for histogram")
print("**********************************")
print("Hidden state {}th","           ","Mean")
for i in range(0,len(ind_mean_of_hiddenstates)):
    print(ind_mean_of_hiddenstates[i][0], "                        ", ind_mean_of_hiddenstates[i][1])
    
#hidden states in well odered
h_s_o = []
for i in ind_mean_of_hiddenstates:
    h_s_o.append(i[0])
print(h_s_o)

"Analysis 3 : x_i affects x_i+1 for x_i is hidden state in hidden_state"
XY = []
pairr = []
pair_m = []
#         aa = float(format(model.means_[i][0],'.2f'))
#         bb = float(format(model.means_[j][0],'.2f'))
#         pair_d.append([aa,bb])
for i in h_s_o:
    aa = format(model.means_[i][0],'.2f')
    XY.append(aa)
    for j in h_s_o:
        pairr.append([i,j])
        pair_m.append([model.means_[i][0],model.means_[j][0]])

print(pairr)
print(pair_m)
        
x_i3 = hidden_states[:]
x_i3 = x_i3.tolist()
x_i3_plus = hidden_states[:]
x_i3_plus = x_i3_plus.tolist()
zz3 = []
  
print
del x_i3[-1] #remove last element 
x_i3_plus.pop(0) #remove first element
  
density3 = []
for j in range(0, len(pairr)):
    density3.append([pair_m[j],0])
    for k in range(0, len(x_i3)):
        if pairr[j][0] == x_i3[k] and pairr[j][1] == x_i3_plus[k]:
            density3[-1][-1] += 1
    zz3.append(density3[-1][-1])

print(zz3)
print(density3)

print(" ")
print("Record of data hidden state")
print("**********************************")
print("No.","   ","mean of X"," - ","mean of Y","    ","#Number")
for i in range(0,len(density3)):
    print(i, "    ",density3[i][0][0], "    - ", density3[i][0][1], "    ", density3[i][1])

"Plot Analysis 3"
##colormap plot_1
zz3 = np.asarray(zz3)
Z3 = zz3.reshape(n, n)
fig, ax = plt.subplots()
im = ax.imshow(Z3,cmap='nipy_spectral',origin='lower',interpolation='bilinear')
# im = ax.imshow(Z3,cmap='prism',origin='lower',interpolation='bilinear')
# We want to show all ticks...
ax.set_xticks(np.arange(len(XY)))
ax.set_yticks(np.arange(len(XY)))
# ... and label them with the respective list entries
ax.set_xticklabels(XY)
ax.set_yticklabels(XY)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
 
# Loop over data dimensions and create text annotations.
for i in range(len(XY)):
    for j in range(len(XY)):
        if Z3[i, j] != 0:
            text = ax.text(j, i, Z3[i, j],ha="center", va="center", color="w")
plt.savefig(results_dir + "%s.png" % figname3)
plt.show()