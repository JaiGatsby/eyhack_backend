
# coding: utf-8

# In[71]:

import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR


# In[5]:

df = pd.read_csv("Data/lol.csv")


# In[6]:

df.head(5)


# In[46]:

X = np.array(df[["REST_ID","TABLE SIZE", "TIME (SEC)", "MONTH", "DAY"]])
Y = np.array(df["WAIT TIME"])


# In[69]:

train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.25)


# In[72]:

# regr = RandomForestRegressor(n_estimators = 50)
regr = SVR()


# In[73]:

regr.fit(train_x, train_y)


# In[ ]:

MSE = lambda pred: np.mean((pred - test_y) ** 2)
MAE = lambda pred: np.mean(np.absolute(pred-test_y))
p = regr.predict(test_x)
print(MSE(p))
print(MAE(p))


# In[67]:

regr.predict([[113442,5,4015,1,5]])


# In[ ]:



