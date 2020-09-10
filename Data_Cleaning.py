# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import pandas as pd

#%%
Data= pd.read_csv('Training data.csv')
Data=Data.drop('Date',1)
Data

# %%
features=["Temp_max","Temp_avg","Temp_min","Dew_max","Dew_avg","Dew_min","Hum_max","Hum_avg","Hum_min","Wind_max","Wind_avg","Wind_min","Pres_max","Pres_avg","Pres_min","Precipitation"]

# %%
def derive_nth_day_feature(df, feature, N):
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N, rows)]
    col_name = f"{feature}_{N}"
    df[col_name] = nth_prior_measurements

# %%
for feature in features:
    if feature != 'date':
        derive_nth_day_feature(Data, feature, 1)

Data =Data.dropna()
Data.to_csv('Final testing data.csv',index=False)
