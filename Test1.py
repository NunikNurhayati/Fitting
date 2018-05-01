"To call functions, tools from Library"
from __future__ import print_function
import datetime
import numpy as np
from matplotlib import cm, pyplot as plt
from hmmlearn.hmm import GaussianHMM, GMMHMM
from hmmlearn.base import _BaseHMM
from matplotlib._image import GAUSSIAN
# from matplotlib.mlab import bivariate_normal
# from mpl_toolkits.mplot3d import Axes3D
# from Cython.Includes.libcpp import pair

"INPUT"
#number of state
n = 5
#covariance type
covar_type = "full"
#number of iteration
iterr = 1000
#figure name
figname1 = "resultData2n5T=110KCurren6until210%d" % n

# figname2 = "3DresultData2n2T=90KCurrent10until27"

"Import data from excel file"
from xlrd import open_workbook
book = open_workbook('Data2.xlsx')
sheet = book.sheet_by_index(7)

print(sheet.nrows)

x = []
y = []

for k in range(1,sheet.nrows):
    x.append(str(sheet.row_values(k)[1-1]))
    y.append(str(sheet.row_values(k)[2-1]))

x = np.asarray(map(float, x))
y = np.asarray(map(float, y))

X = np.reshape(y,(-1,1))

"Run Gaussian HMM"
# Make an HMM instance and execute fit
model = GaussianHMM(n_components=n, covariance_type=covar_type, n_iter=iterr).fit(X)
# model = GMMHMM(n_components=n_comp, n_iter=1000).fit(X)

# Predict the optimal sequence of internal hidden state
hidden_states = model.predict(X)
print("done fitting to HMM")

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
    

"Print All hidden state parameter"
print("Transition matrix")
print(model.transmat_)
print()

print("Means and Variance of each hidden state")

for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("variance = ", np.diag(model.covars_[i]))
    print()


"Analysis 2 : Total time domain"
analysis_2 = []
for i in range(0,n):
    analysis_2.append([i,0,0])
    for j in result:
        if j[3] == i:
            analysis_2[-1][1] += 1
            analysis_2[-1][2] += j[4]

"Print RESULT"
print("Record of all hidden state")
print("**********************************")
print("No.","   ","TIME Start"," - ","TIME End","    ","VALUE","         ","Hidden State {}th","     ","Time domain")
for i in range(0,len(result)):
    print(i, "    ",result[i][0], "    - ", result[i][1], "    ", result[i][2], "      ", result[i][3], "             ", result[i][4])

print(" ")
print("Means and total domain of each hidden state")
print("---------------------------------------")
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("total number with this hidden state = ", analysis_2[i][1])
    print("mean = ", model.means_[i])
    print("total time_domain = ", analysis_2[i][2])
#     print("variance = ", np.diag(model.covars_[i]))
    print()

"Plot data and result"
x_plot = []
y_plot = []
for i in result:
    x_plot.append(i[0])
    x_plot.append(i[1])
     
    y_plot.append(i[2])
    y_plot.append(i[2])
 
plt.figure(1)
plt.title("hmm Gaussian method fitting result vs data")
plt.plot(x,y, 'r')#, x,y, 'bo')
plt.plot(x_plot, y_plot, 'k')
# plt.savefig("diag101000") 
plt.savefig("%s.png" % figname1)
# plt.close()
plt.show()