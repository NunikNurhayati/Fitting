"To call functions, tools from Library"
from __future__ import print_function
import datetime
import numpy as np
from matplotlib import cm, pyplot as plt
from hmmlearn.hmm import GaussianHMM, GMMHMM
from hmmlearn.base import _BaseHMM
from mpl_toolkits.mplot3d import Axes3D
import os


"To call function of output Data"
import os,sys
# import subprocess
# import glob
# from os import path


"INPUT"
#number of state
n = 2
#covariance type
covar_type = "full"
#number of iteration
iterr = 1000
#figure name
figname1 = "130K300mVCurrent3;142-172sn%d" % n
# figname2 = "result__foldernameanalysis1_3d_scatterplot"
figname3 = "130K300mVCurrent3;142-172s;n16analysis1_colormapplot_1"
# figname4 = "result__analysis1_colormapplot_2"

script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'test4/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

"Output Data"
f = open(results_dir + 'RTV300mVCurrent1;300-400s;n16;output.txt','w')
sys.stdout = f

"Import data from excel file"
from xlrd import open_workbook
book = open_workbook('Data2.xlsx')
sheet = book.sheet_by_index(2)

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
 
"Hidden state"
result = []
test = hidden_states[0]
for ind, i in enumerate(hidden_states):
    if n == 1 and ind == 0:
        result.append([0,0,test,test,0])
          
    if i != test:
        if len(result) == 0:
            result.append([0,ind-1,test,test,0])
        else:
            result.append([result[-1][1]+1,ind-1,test, test,0])
        test = i
for i in range(0,len(result)):
    result[i][0] = x[result[i][0]]
    result[i][1] = x[result[i][1]]
    result[i][2] = model.means_[result[i][2]][0]
    result[i][4] = result[i][1] - result[i][0]
  
"Analysis 1: x_i affects x_i+1 for x_i is hidden state in result"
x_i = []
for i in result:
    x_i.append(i[3])
x_i_plus = x_i[:]
  
del x_i[-1] #remove last element 
x_i_plus.pop(0) #remove first element
  
##Create pair of hidden state
# ##1 based on hidden state vestor
# X_i = x_i[:]
# X_i_plus = x_i_plus[:]
# pairr = [[x_i[0],x_i_plus[0]]]
# for j in range(1, len(x_i)):
#     if [x_i[j],x_i_plus[j]] not in pairr:
#         pairr.append([x_i[j],x_i_plus[j]])
          
##2 based on combination of hidden state
X_i = []
xx = []
yy = []
zz = []
XY = []
for i in range(0,n):
    X_i.append(i)
pairr = []
pair_m = []
for i in range(0, n):
    XY.append(str(model.means_[i][0]))
    for j in range(0, n):
        pairr.append([i,j])
        pair_m.append([model.means_[i][0],model.means_[j][0]])
        xx.append(i)
        yy.append(j)
          
density = []
for j in range(0, len(pairr)):
    density.append([pairr[j],0])
    for k in range(0, len(x_i)):
        if pairr[j][0] == x_i[k] and pairr[j][1] == x_i_plus[k]:
            density[-1][-1] += 1
    zz.append(density[-1][-1])
      
"Analysis 3 : x_i affects x_i+1 for x_i is hidden state in hidden_state"
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


print(len(x_i3))