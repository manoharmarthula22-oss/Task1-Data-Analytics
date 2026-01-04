import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

print(df.head())
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())
print("\nCity wise customer count:")
print(df['city'].value_counts())

df['city'].value_counts().plot(kind='bar')
plt.title("Number of Customers by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.savefig("city_wise_customers.png")   
plt.show()

df['amount'].plot(kind='hist', bins=5)
plt.title("Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.savefig("amount_distribution.png")   
plt.show()

print("\nAverage amount by city:")
print(df.groupby('city')['amount'].mean())

print("\nMaximum amount by city:")
print(df.groupby('city')['amount'].max())
