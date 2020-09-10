#%%
import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
import pickle

#%%
data= pd.read_csv('Final testing data.csv')

# print(data.info())
#%%
Modelnames={'Temp_avg':['Temp_max_1','Temp_avg_1','Temp_min_1'],
'Hum_avg':['Dew_max_1','Dew_avg_1','Dew_min_1','Hum_max_1','Hum_avg_1','Hum_min_1'],
'Precipitation':['Precipitation_1']}


def Checktraining():
    Choice =input("Are we Training?(y/n)\n")
    return Choice.lower()=='y'

def datasplit(x,y):
    return sklearn.model_selection.train_test_split(x, y, test_size=0.01)
    
def Train(x,y):
    best = 0
    for _ in range(100000):
        x_train, x_test, y_train, y_test =datasplit(x,y)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        #print("Accuracy: " + str(acc))
    

        if acc > best:
            best = acc

            with open(f"Models/{Modelname}.pickle", "wb") as f:
                pickle.dump(linear, f)

    print("------------------------")        
    print("Final Accuracy: " + str(best))
    print("------------------------")           

    

def  Test(X,Y,training,linear=None ):
    if training:
        _, X, __, Y =datasplit(X,Y)

    if linear==None:
        try:
            filename=f"Models/{Modelname}.pickle"
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

    predicted= linear.predict(X)
    for x in range(len(predicted)):
        print(f"Predicted :{predicted[x]}, for Data Giver: {X[x]},Expected Data show be:{Y[x]}")

    

# print("""
 
# """)
# 
if __name__ == "__main__":
    
    for Modelname in Modelnames:
        x=np.array(data[Modelnames[Modelname]])
        y=np.array(data[Modelname])
        training = Checktraining()
        if training:
            print(f"Starting to train data for {Modelname}")
            Train(x,y)
            print(f"Done training data for {Modelname}")
        print(f"Starting Testing data for {Modelname}")
        Test(x,y,training=False)
        print(f"Done testing data for {Modelname}")
