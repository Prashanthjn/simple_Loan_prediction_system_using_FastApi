import pandas as pd 
from sklearn.ensemble import RandomForestClassifier  
import joblib 
from sklearn.model_selection import train_test_split

df=pd.read_csv("data.csv")
X=df[["Age","Salary"]]

y=df["Approved"]

model=RandomForestClassifier()
model.fit(X,y)

joblib.dump(model, "loan_model.joblib")

print("model saved successfully!")
