import sys
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr 
rfile = open(sys.argv[1],"r")
rfile1 = open(sys.argv[2],"r")
data = []
actual = []
predicted = []
coef = []
M=0
MAPE=0
for line in rfile:
    line = line.strip().rstrip(',')
    data.append(line.split(','))
    #file_name.append(sample)
print(data)

for line in rfile1:
	line = line.strip().rstrip(',')
	coef.append(line.split(','))
#print(coef[3][0])
for i in range(1,len(data)):
	actual.append(float(data[i][0]))
	a= float(data[i][0])
	x=0
	for j in range(1,len(data[i])):
		y=str(coef[j-1][0])
		#print(y)
		x+=float(data[i][j])*float(y)
	#print("ss",coef[-1][0])
	x*=3
	x+=float(coef[-1][0])
	M+= abs((a-x)/a)
	predicted.append(x)
MAPE = (M/len(data))*100
print(pearsonr(actual,predicted))
'''print("--------Actual---------")
for i in range(0,44):
	print(actual[i])

print("---------Predicted--------")
for i in range(0,44):
	print(predicted[i])'''

plt.plot(actual,'r',predicted,'b')
plt.show()
#plt.plot(predicted)
#plt.show()
print("MAPE= ",MAPE)		


