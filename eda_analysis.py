import pandas as pd

# Load the dataset
df = pd.read_csv("books_dataset.csv")

print("===== DATASET OVERVIEW =====")

# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset shape
print("\nNumber of rows and columns:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())


print("\n===== PRICE ANALYSIS =====")

# Remove currency symbol and convert price to numeric
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

print("\nPrice statistics:")
print(df["Price"].describe())

print("\nAverage price:")
print(df["Price"].mean())

print("\nMinimum price:")
print(df["Price"].min())

print("\nMaximum price:")
print(df["Price"].max())


print("\n===== AVAILABILITY ANALYSIS =====")

print("\nAvailability counts:")
print(df["Availability"].value_counts())


print("\n===== RATING ANALYSIS =====")

print("\nRating counts:")
print(df["Rating"].value_counts())


print("\n===== TOP 5 MOST EXPENSIVE BOOKS =====")

print(
    df.sort_values("Price", ascending=False)[
        ["Title", "Price", "Rating"]
    ].head(5)
)


print("\n===== TOP 5 CHEAPEST BOOKS =====")

print(
    df.sort_values("Price")[
        ["Title", "Price", "Rating"]
    ].head(5)
)


print("\n===== EDA SUMMARY =====")

print("Total books:", len(df))
print("Average price: £", round(df["Price"].mean(), 2))
print("Most expensive book price: £", round(df["Price"].max(), 2))
print("Cheapest book price: £", round(df["Price"].min(), 2))
print("Most common rating:", df["Rating"].mode()[0])
print("Most common availability:", df["Availability"].mode()[0])
import matplotlib.pyplot as plt

# Rating Distribution
plt.figure(figsize=(8, 5))
df["Rating"].value_counts().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()


# Price Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=5)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()