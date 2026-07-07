import pandas as pd
import numpy as np 
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv('security_logs.csv')

model = IsolationForest(contamination = 0.05, random_state = 42)

model.fit(df)

predictions = model.predict(df)

df['ai_decision'] = predictions

print(df['ai_decision'].value_counts())

joblib.dump(model,'security_model.pkl')
print('AI model saved ')