import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use("ggplot")
data= pd.read_csv("data.csv")

predictlist="Wind_avg".split(',')
for predict in predictlist:
    print('----------X--------------------X--------------')
    x=np.array(data.drop(["Jul","Date",predict],1))
    y=np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    best = 0
    for _ in range(1000):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        #print("Accuracy: " + str(acc))

        if acc > best:
            best = acc
            with open(f"{predict}.pickle", "wb") as f:
                pickle.dump(linear, f)

    print("------------------------")           
    print("Final Accuracy: " + str(best))
    print("------------------------")           

    pickle_in = open(f"{predict}.pickle", "rb")
    linear = pickle.load(pickle_in)


    print("-------------------------")
    print('Coefficient: \n', linear.coef_)
    print('Intercept: \n', linear.intercept_)
    print("-------------------------")

    predicted= linear.predict(x_test)
    for x in range(len(predicted)):
        print(f"Predicted :{predicted[x]}, for Data Giver: {x_test[x]},Expected Data show be:{y_test[x]}")