#Multiple Linear Regression
import pandas as pd
import statsmodels.formula.api as smf
data=pd.DataFrame({"Experience":[1,3,5,7,10],"Education":[12,16,16,18,18],"Age":[25,28,32,25,40],"Salary":[30000,35000,40000,45000,50000]})
print(data)
model=smf.ols("Salary ~ Experience + Education + Age",data=data)
result=model.fit()
print(result)