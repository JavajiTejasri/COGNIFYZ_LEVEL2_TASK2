import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Count online delivery availability
delivery_counts = df['Has Online delivery'].value_counts()

print("Online Delivery Availability:")
print(delivery_counts)

# Calculate percentage
percentage = (delivery_counts / delivery_counts.sum()) * 100

print("\nPercentage Distribution:")
print(percentage)

# Plot graph
delivery_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title("Online Delivery Availability")

plt.ylabel("")

# Save graph
plt.savefig("online_delivery_distribution.png")

plt.show()