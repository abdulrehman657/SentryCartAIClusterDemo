import pandas as pd 
import numpy as np 

np.random.seed(42)

num_normal = 950

normal_clicks = np.random.uniform(10,35,num_normal)
normal_checkout = np.random.uniform(120,600,num_normal)
normal_spend = np.random.normal(75,25,num_normal)
normal_failed = np.random.choice([0,1], size=num_normal, p=[0.9,0.1])
normal_distance = np.zeros(num_normal)

df_normal = pd.DataFrame({
    'clicks_per_min': normal_clicks,
    'checkout_speed_sec' : normal_checkout,
    'total_spend' : np.clip(normal_spend,10,200),
    'failed_login' : normal_failed,
    'distance_km' : normal_distance
})

num_bots = 25

bot_clicks = np.random.uniform(300,500,num_bots)
bot_checkout = np.random.uniform(0.5,3.0,num_bots)
bot_spend = np.random.uniform(1500,4000,num_bots)
bot_failed = np.zeros(num_bots)
bot_distance = np.zeros(num_bots)

df_bots = pd.DataFrame({
    'clicks_per_min' : bot_clicks,
    'checkout_speed_sec' : bot_checkout,
    'total_spend' : bot_spend,
    'failed_login' : bot_failed,
    "distance_km" : bot_distance
})

num_fraud = 25

fraud_clicks = np.random.uniform(15, 50, num_fraud)
fraud_checkout = np.random.uniform(60, 300, num_fraud)
fraud_spend = np.random.uniform(500, 1500, num_fraud)
fraud_failed = np.random.randint(5, 20, num_fraud)
fraud_distance = np.random.uniform(4000, 12000, num_fraud)

df_fraud = pd.DataFrame({
    'clicks_per_min': fraud_clicks,
    'checkout_speed_sec': fraud_checkout,
    'total_spend': fraud_spend,
    'failed_login': fraud_failed,
    'distance_km': fraud_distance
})

df_final = pd.concat([df_normal, df_bots, df_fraud], ignore_index=True)

df_final = df_final.sample(frac=1).reset_index(drop=True)

df_final.to_csv('security_logs.csv', index=False)


print("✅ Data Factory Successful! Generated 1,000 mixed user logs inside 'security_logs.csv'")
print(f"-> Total Dataset Shape: {df_final.shape}")