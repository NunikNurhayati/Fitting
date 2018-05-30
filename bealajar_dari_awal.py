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

"INPUT"
#number of state
n = 5
#covariance type
covar_type = "full"
#number of iteration
iterr = 1000
#figure name
figname1 = "result__histogram%d" % n
# figname2 = "result__histogramanalysis1_3d_scatterplot"
figname3 = "result__histogramanalysis1_colormapplot_1"
# figname4 = "result__analysis1_colormapplot_2"

script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'belajar dari awal/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

# "Output Data"
# f = open(results_dir + 'histogram.txt','w')
# sys.stdout = f

"Import data from excel file"
from xlrd import open_workbook
book = open_workbook('Data2.xlsx')
sheet = book.sheet_by_index(5)

"Input"
#start_time
start_t = 0
#end_time
end_t = 200

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

print("-------------")
X = []
# time_end = 
for count, elem in enumerate(hidden_states):
    
    X.append([elem, 0, 1000])
#     print (count, elem)
print (X)