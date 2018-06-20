"To call functions, tools from Library"
# from __future__ import print_function
import datetime
import numpy as np
from matplotlib import cm, pyplot as plt
from hmmlearn.hmm import GaussianHMM, GMMHMM
from hmmlearn.base import _BaseHMM
import os,sys
# from mpl_toolkits.mplot3d import Axes3D
import time
import warnings
warnings.filterwarnings("ignore")
# "To call function of output Data"
# import os,sys
import pandas as pd
import csv


"INPUT"
#number of state
n = 3
#covariance type
covar_type = "full"
#number of iteration
iterr = 23
# figure name
figname1 = "Combined110K300mVCurrent6,7;n23;iter200n%d" % n
 # figname2 = "result__foldernameanalysis1_3d_scatterplot"
figname3 = "CombinedRTA110K300mVCurrent6,7;n23;iter200analysis1_colormapplot_1"
 # figname4 = "result__analysis1_colormapplot_2"
 
script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Test8Combined110K300mVCurrent6,7;n23;iter200/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

"Output Data"
f = open(results_dir + '5Combined110K300mVCurrent6,7;n23;iter200;output.txt','w')
sys.stdout = f

# "Import data from excel file"
# from xlrd import open_workbook
# book = open_workbook('Data_LowTemp_Combined.xlsx')
# sheet = book.sheet_by_index(3)

# "Input"
# #start_time
# start_t = 0
# #end_time
# end_t = 1000
# 
# x = []
# y = []
# 
# 
# for k in range(start_t,end_t):
#     x.append(str(sheet.row_values(k)[0])) #[k] = row, [0] = column ke nol
#     y.append(str(sheet.row_values(k)[1])) #[k] = row, [1] = column ke satu
#  
# x = np.asarray(map(float, x))
# y = np.asarray(map(float, y))

x = []
y = []

with open('RTA100mVCurrent10.csv', 'rb') as f:
    reader = csv.reader(f)
#     for k in range(start_t,end_t):
#         x.append(row(k)[0])) #[k] = row, [0] = column ke nol
#         y.append(row(k)[1])) #[k] = row, [1] = column ke satu

    for row in reader:
        x.append(row[0])
        y.append(row[1])
#         print row
        
        
x = np.asarray(map(float, x))
y = np.asarray(map(float, y))

X = np.reshape(y,(-1,1))
 
"Run Gaussian HMM"
# Make an HMM instance and execute fit
model = GaussianHMM(n_components=n, covariance_type=covar_type, n_iter=iterr, verbose=True).fit(X)
 
# Predict the optimal sequence of internal hidden state
hidden_states = model.predict(X)
print("Number of Rows")
print("--------------")
# print(sheet.nrows)
print(" ")
print("Hidden States")
print("-------------")
print(hidden_states)
 
"Hidden state"
# y_for_axis = hidden_states[:]
# y_for_axis = y_for_axis.tolist()
# new_df = pd.DataFrame(columns=['y_for_axis'], data=y_for_axis)

y_for_axis = []
y_for_axis = [i for i in hidden_states[:]]


print("==============")
for i in range(len(hidden_states)):
    print y_for_axis[i]

# yplot = []
# test = hidden_states[:]
# for i in range(0, len(hidden_states)):
#     yplot.append([hidden_states[i], test])
# # for i in range(len(yplot)):
#     yplot[i][1] = str(model.means_[yplot[i][1]])
# print ("nama",yplot[i][1])

# yplot_for_axis = hidden_states[:]
# yplot_for_axis = yplot_for_axis.tolist()
# new_df = pd.DataFrame(columns=['yplot_for_axis'], data=yplot_for_axis)

# yplot_for_axis = []
# yplot_for_axis = [i for i in yplot[i][1]]
# for i in range(len(yplot)):
#     print yplot_for_axis[i]

print("==============")
# for i in range(len(A)):
# print [yplot_for_axis[i]]
# A = []
# for i in range(0,len(yplot)):
#     A.append(yplot[i][1])
# print("==============")
# for i in range(len(A)):
#     print yplot_for_axis[i]

print("================")
# print yplot   

# y_axis = []

# for i, element in enumerate(hidden_states):
#     y_axis.append(str([hidden_states(i)]))


    
# for i in range(0,len(hidden_states)):
#     y_axis.append(y_for_axis[i])
#     y_axis = model.means_[y_axis[0]]
# print("y_axis")
# print y_axis

print("==============")
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
    
x_y_axis = []
axis = hidden_states[:]
print("===panjang hidden===")
print(len(hidden_states))
for count, elem in enumerate(hidden_states):
    x_y_axis.append([axis,axis])
    axis = i
for i in range(0,len(x_y_axis)):
    x_y_axis[i][0] = x[x_y_axis[i][0]]
    x_y_axis[i][1] = model.means_[x_y_axis[i][1]]
print("===x_axis")
for i in range(0,len(x_y_axis)):
    print x_y_axis[i][0]
print("===y_axis===")
for i in range(0,len(x_y_axis)):
    print x_y_axis[i][1]
#     y_plot.append(i[2])
