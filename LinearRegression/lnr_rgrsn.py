import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('Salary_dataset.csv')

# plt.scatter(data.YearsExperience, data.Salary)
# plt.show()

def lossFunction(m, b, points):

    for i in range (len(points)):
        totalError = 0
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary

        totalError += (y - (m*x + b))**2
    totalError / float(len(points))        
        
   