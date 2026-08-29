#Simple Linear Regression
import pandas as pd
import statsmodels.api as sm
data=pd.DataFrame({"Experience":[1,2,3,4,5],"Salary":[30000,35000,40000,45000,50000]})
print(data)
x=data["Experience"]
y=data["Salary"]
x=sm.add_constant(x)   #Add a constant term to the predictor
model=sm.OLS(y,x).fit()  #Fit the model 
result=model.summary()  #Get the summary of the model
print(result)