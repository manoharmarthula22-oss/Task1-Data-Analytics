import pandas as pd

df = pd.read_csv("cleaned_data.csv")

# KPIs
total_customers = df.shape[0]
avg_amount = df['amount'].mean()
max_amount = df['amount'].max()
customers_by_city = df['city'].value_counts()

print("Total Customers:", total_customers)
print("Average Amount:", avg_amount)
print("Maximum Amount:", max_amount)
print("\nCustomers by City:")
print(customers_by_city)

print("\nAverage Amount by City:")
print(df.groupby('city')['amount'].mean())
