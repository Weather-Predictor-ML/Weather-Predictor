import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
import pickle

data= pd.read_csv('Test_data.csv')
Modelname='Temp_avg'
test=np.array(data[['Temp_max','Temp_avg','Temp_min']])
print(test)
try:
    filename=f"{Modelname}.pickle"
    print(filename)
    pickle_in = open(filename, "rb")
    linear = pickle.load(pickle_in)
except :
    print("No Model Found")
    quit()

print("-------------------------")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("-------------------------")

predicted= linear.predict(test)
for x in range(len(predicted)):
    print(f"Predicted :{predicted[x]}, for Data Giver: {data['Temp_avg'][x]}")

# print("""