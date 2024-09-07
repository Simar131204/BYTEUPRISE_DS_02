import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:/Users/harse/Downloads/tested.csv'  # Update this path to your dataset location
data = pd.read_csv(file_path)

# Set the style for seaborn
sns.set(style="whitegrid")

# Plot distribution of 'Age' and its relationship with 'Survived'
plt.figure(figsize=(12, 6))

# Age distribution
plt.subplot(1, 2, 1)
sns.histplot(data['Age'], kde=True, color='skyblue')
plt.title('Age Distribution')

# Age vs. Survived
plt.subplot(1, 2, 2)
sns.boxplot(x='Survived', y='Age', data=data, palette='Set2')
plt.title('Age vs. Survival')

plt.tight_layout()
plt.show()

# Plot distribution of 'Fare' and its relationship with 'Survived'
plt.figure(figsize=(12, 6))

# Fare distribution
plt.subplot(1, 2, 1)
sns.histplot(data['Fare'], kde=True, color='lightgreen')
plt.title('Fare Distribution')

# Fare vs. Survived
plt.subplot(1, 2, 2)
sns.boxplot(x='Survived', y='Fare', data=data, palette='Set3')
plt.title('Fare vs. Survival')

plt.tight_layout()
plt.show()
