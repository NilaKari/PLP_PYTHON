# ====================================================
# Task: Data Analysis & Visualization on Iris Dataset
# ====================================================

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

try:
    # Load dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame   # Convert to pandas DataFrame

    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError as e:
    print("❌ Error: File not found.", e)
except Exception as e:
    print("❌ An unexpected error occurred:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check structure, data types, and missing values
print("\nDataset Info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# Clean dataset (not necessary here, but let's be explicit)
df = df.dropna()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Descriptive statistics
print("\nStatistical Summary:")
print(df.describe())

# Grouping: mean petal length per species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("\nAverage Petal Length per Species (by target code):")
print(grouped)

# Map species codes to names
species_map = dict(enumerate(iris.target_names))
print("\nTarget mapping:", species_map)

# Interesting finding: differences in petal length by species
print("\nObservation: Iris-virginica has the largest average petal length, while Iris-setosa has the smallest.")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

sns.set(style="whitegrid")

# 1. Line chart - sepal length across dataset index
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x=df["target"].map(species_map), y=df["petal length (cm)"], ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="sepal length (cm)", 
    y="petal length (cm)", 
    hue=df["target"].map(species_map), 
    data=df, 
    palette="Set1"
)
plt.title("Scatter Plot: Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
