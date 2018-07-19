"To call functions, tools from Library"
# from __future__ import print_function
import datetime
import numpy as np
from matplotlib import cm, pyplot as plt
from hmmlearn.hmm import GaussianHMM, GMMHMM
from hmmlearn.base import _BaseHMM
import os,sys
# import panda as pd
# from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings("ignore")
# "To call function of output Data"
# import os,sys



"INPUT"
#number of state
n = 23
#covariance type
covar_type = "full"
#number of iteration
iterr = 250
#figure name
figname1 = "RTV50mVCurrent24;n23;iter250;n%d" % n
# figname2 = "result__foldernameanalysis1_3d_scatterplot"
figname3 = "RTV50mVCurrent24;n23;iter250analysis1_colormapplot_1"
# figname4 = "result__analysis1_colormapplot_2"

script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'FittingperpointRTV50mVCurrent24;n23;iter250/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

"Output Data"
f = open(results_dir + 'RTV50mVCurrent24;n23;iter250;output.txt','w')
sys.stdout = f

"Import data from excel file"
from xlrd import open_workbook
book = open_workbook('Data_RTV50mV.xlsx')
sheet = book.sheet_by_index(8)
  
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
# "import data from csv"
# import csv
# x = []
# y = []
# with open('RTA300mVCurrent4.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         x.append(row[0])
#         y.append(row[1])
# x = np.asarray(map(float, x))
# y = np.asarray(map(float, y))
# X = np.reshape(y,(-1,1))
 
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
    

"Analysis for ordered hidden states"
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
print(" ")
print("Record data for histogram")
print("**********************************")
print("Hidden state {}th","           ","Mean")
for i in range(0,len(ind_mean_of_hiddenstates)):
    print(ind_mean_of_hiddenstates[i][0], "                        ", ind_mean_of_hiddenstates[i][1])
    
#hidden states in well odered
h_s_o = []
for i in ind_mean_of_hiddenstates:
    h_s_o.append(i[0])
print("hidden state ordered", h_s_o)

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

# print(pairr)
# print(pair_m)
        
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

# print(zz3)
# print(density3)
    
print(" ")
print("Record of data hidden state")
print("**********************************")
print("No.","   ","mean of X"," - ","mean of Y","    ","#Number")
# for i in range(0,len(density3)):
#     print(i, "    ",density3[i][0][0], "    - ", density3[i][0][1], "    ", density3[i][1])
 
print("-----------------------------------")
print("mean of X")
print("-----------------------------------")    
for i in range(0,len(density3)):
    print(density3[i][0][0])
 
print("-----------------------------------")
print("mean of Y")
for i in range(0,len(density3)):
    print(density3[i][0][1])
 
print("-----------------------------------")
print("Number")
for i in range(0,len(density3)):
    print(density3[i][1])

  
"Analysis 2 : Total time domain"
analysis_2 = []
for i in range(0,n):
    analysis_2.append([i,0,0])
    for j in result:
        if j[3] == i:
            analysis_2[-1][1] += 1
            analysis_2[-1][2] += j[4]
  
# "Print All hidden state parameter"
# print("Transition matrix")
# print(model.transmat_)
# print()
# 
# print("Means and Variance of each hidden state")
# 
# for i in range(model.n_components):
#     print("{0}th hidden state".format(i))
#     print("mean = ", model.means_[i])
#     print("variance = ", np.diag(model.covars_[i]))
#     print()


# "Print RESULT"
# print(" ")
# print("Record of all hidden state")
# print("**********************************")
# print("No.","   ","TIME Start"," - ","TIME End","    ","VALUE","         ","Hidden State {}th","     ","Time domain")
# for i in range(0,len(result)):
#     print(i, "    ",result[i][0], "    - ", result[i][1], "    ", result[i][2], "      ", result[i][3], "             ", result[i][4])
# 
# 
# "Print list pair of x_i,x_i+1"
# print("record of list pair of x_i,x_i+1")
# print("hidden_states original", hidden_states)
# print('x_i     ', x_i3)
# print('x_i_plus', x_i3_plus)            
# print('list of [x_i,x_i_plus]', pairr)
# print('List of [[x_i,x_i_plus], number of repetition]', density3)

print(" ")
print("Means and total domain of each hidden state")
print("---------------------------------------")
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("total number with this hidden state = ", analysis_2[i][1])
    print("mean = ", model.means_[i])
    print("total time_domain = ", analysis_2[i][2])
#     print("variance = ", np.diag(model.covars_[i]))
 
"Plot data and result"
x_plot = []
y_plot = []
for i in result:
    x_plot.append(i[0])
    x_plot.append(i[1])
       
    y_plot.append(i[2])
    y_plot.append(i[2])
    
# "To change list to row"
# x_for_axis = []
# x_for_axis = [i for i in x_plot[:]]
# print("=======x_for_axis=======")
# for i in range(len(x_plot)):
#     print x_for_axis[i]
# 
# y_for_axis = []
# y_for_axis = [i for i in y_plot[:]]
# print("=======y_for_axis=======")
# for i in range(len(y_plot)):
#     print y_for_axis[i]
    

"To print all means states per point"
y_hs = hidden_states[:]
y_hs = y_hs.tolist()
A = []
B = []
for i in range(len(hidden_states)):
    A.append(y_hs[i])
for i in range(len(A)):
    B.append(model.means_[A][i][0])
y_axis = []
y_axis = [i for i in B[:]]
print("===============================================================y_axis==================================================================")
for i in range(len(B)):
    print y_axis[i]
print("===finished===")

plt.figure(1)
plt.title("hmm Gaussian method fitting result vs data")
plt.plot(x,y, 'r')#, x,y, 'bo')
plt.plot(x_plot, y_plot, 'k')
# plt.savefig("diag101000") 
plt.savefig(results_dir + "%s.png" % figname1)
plt.show()
  
"Plot Analysis 3"
##3D scatter plot
# plt.figure(2)
# plt.title("Hidden state mapping")
# fig = plt.figure(2)
# ax = fig.gca(projection='3d')
# for i in range(0,len(density)):
#     if density[i][1] != 0:
#         ax.scatter(density[i][0][0],density[i][0][1],density[i][1],color='b') 
#         ax.text(density[i][0][0],density[i][0][1],density[i][1],  '(%s,%s)%s' % (str(density[i][0][0]),str(density[i][0][1]),str(density[i][1])), size=7, zorder=1,  
#  color='k') 
# # for i,j,k in zip(xx,yy,zz):
# #     ax.annotate(str(zz),xyz=(i,j,k))
# ax.set_xlabel('Hidden State')
# ax.set_ylabel('Hidden State')
# ax.set_zlabel('Number')
# plt.savefig(results_dir + "%s.png" % figname2)
# plt.close()
 
##colormap plot_1
zz3 = np.asarray(zz3)
Z3 = zz3.reshape(n, n)
fig, ax = plt.subplots()
im = ax.imshow(Z3,cmap='nipy_spectral_r',origin='lower',interpolation='bilinear')
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
            text = ax.text(j, i, Z3[i, j],ha="center", va="center", color="black", fontsize=7)
plt.savefig(results_dir + "%s.png" % figname3)
plt.show()
