#2nd model for Simple Linear Regression
import pandas as pd
import statsmodels.formula.api as smf
data=pd.DataFrame({"experience":[1,2,3,4,5],"salary":[30000,35000,40000,45000,50000]})
model=smf.ols("salary ~ experience",data=data)
result=model.fit()