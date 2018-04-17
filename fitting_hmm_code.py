from __future__ import print_function

import datetime

import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
try:
    from matplotlib.finance import quotes_historical_yahoo_ochl
except ImportError:
    # For Matplotlib prior to 1.5.
    from matplotlib.finance import (
        quotes_historical_yahoo as quotes_historical_yahoo_ochl
    )

from hmmlearn.hmm import GaussianHMM

print(__doc__)

"Import data from excel"
from xlrd import open_workbook
book = open_workbook('data.xlsx')
sheet = book.sheet_by_index(0)

time_x = []
current_y = []

for k in range(1,sheet.nrows):
    time_x.append(str(sheet.row_values(k)[1-1]))
    current_y.append(str(sheet.row_values(k)[2-1]))

time_xx = map(float, time_x)
current_yy = map(float, current_y)

x = np.asarray(time_xx)
y = np.asarray(current_yy)

X = np.reshape(y,(-1,1))


"Run Gaussian HMM"
print("fitting to HMM and decoding ...", end="")

# Make an HMM instance and execute fit
model = GaussianHMM(n_components=30, covariance_type="full", n_iter=1000).fit(X)

# Predict the optimal sequence of internal hidden state
hidden_states = model.predict(X)


print("hidden_states", len(hidden_states), hidden_states)
print("done")


"Print All hidden state parameter"
print("Transition matrix")
print(model.transmat_)
print()

print("Means and vars of each hidden state")
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("var = ", np.diag(model.covars_[i]))
    print()


"Hidden state"
result = []
test = hidden_states[0]
for ind, i in enumerate(hidden_states):
    if i != test:
        if len(result) == 0:
            result.append([test,0,ind-1])
        else:
            start = result[-1][2]+1
            result.append([test,start,ind-1])
        test = i
print(result)

# for i in range(0,len(hidden_states)):
#       print(i, ",", hidden_states[i])

        
"Plot data and result"
x_plot = []
y_plot = []
for i in result:
    x_plot.append(i[1])
    x_plot.append(i[2])
    
    y_plot.append(model.means_[i[0]])
    y_plot.append(model.means_[i[0]])

plt.figure(1)
plt.title("hmm Gaussian method fitting result vs data")
plt.plot(x,y, 'r')#, x,y, 'bo')
plt.plot(x_plot, y_plot, 'k')
plt.savefig("result30")
plt.show()
