# ==============================================
# 📊 Lab 11 – NumPy Arrays & Vector Operations
# ==============================================

import numpy as np

print("=" * 60)
print("LAB 11 – NUMPY ARRAYS & VECTOR OPERATIONS")
print("=" * 60)


# ==============================================
# 1️⃣ Creating NumPy Arrays
# ==============================================

print("\n1️⃣ Creating Arrays\n")

# 1D array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Zeros, Ones, Full
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 3), 7)

print("\nZeros Array:\n", zeros)
print("\nOnes Array:\n", ones)
print("\nFull Array (7s):\n", full)

# Range & Linspace
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

print("\nArange Array:", range_array)
print("Linspace Array:", linspace_array)


# ==============================================
# 2️⃣ Reshaping & Transposing
# ==============================================

print("\n2️⃣ Reshaping & Transposing\n")

arr3 = np.arange(1, 13)
reshaped = arr3.reshape(3, 4)

print("Original:", arr3)
print("\nReshaped (3x4):\n", reshaped)

transposed = reshaped.T
print("\nTransposed:\n", transposed)


# ==============================================
# 3️⃣ Indexing & Slicing
# ==============================================

print("\n3️⃣ Indexing & Slicing\n")

print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice (index 1 to 3):", arr1[1:4])

print("\n2D Array Element [1,2]:", arr2[1, 2])
print("First Row:", arr2[0])
print("Second Column:", arr2[:, 1])


# ==============================================
# 4️⃣ Boolean & Fancy Indexing
# ==============================================

print("\n4️⃣ Boolean & Fancy Indexing\n")

numbers = np.array([5, 10, 15, 20, 25, 30])
filtered = numbers[numbers > 15]

print("Original:", numbers)
print("Numbers > 15:", filtered)

fancy = numbers[[0, 2, 4]]
print("Fancy Indexing [0,2,4]:", fancy)


# ==============================================
# 5️⃣ Broadcasting
# ==============================================

print("\n5️⃣ Broadcasting\n")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

vector = np.array([10, 20, 30])

broadcasted = matrix + vector

print("Matrix:\n", matrix)
print("Vector:", vector)
print("\nMatrix + Vector:\n", broadcasted)


# ==============================================
# 6️⃣ Statistical Functions
# ==============================================

print("\n6️⃣ Statistical Analysis\n")

data = np.array([12, 15, 20, 22, 18, 30, 25])

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Percentile (75%):", np.percentile(data, 75))


# ==============================================
# 7️⃣ Vectorized BMI Calculator
# ==============================================

print("\n7️⃣ Vectorized BMI Calculator\n")

weights = np.array([60, 75, 80, 55])  # in kg
heights = np.array([1.65, 1.8, 1.75, 1.6])  # in meters

bmi = weights / (heights ** 2)

print("Weights:", weights)
print("Heights:", heights)
print("BMI Values:", np.round(bmi, 2))


# ==============================================
# 8️⃣ Sales Data Analysis
# ==============================================

print("\n8️⃣ Sales Data Analysis\n")

# Rows = Months, Columns = Products
sales = np.array([
    [200, 150, 300],
    [220, 180, 310],
    [250, 200, 330],
    [270, 210, 350]
])

print("Sales Data:\n", sales)

# Total sales per month
monthly_sales = np.sum(sales, axis=1)
print("\nTotal Sales per Month:", monthly_sales)

# Total sales per product
product_sales = np.sum(sales, axis=0)
print("Total Sales per Product:", product_sales)

# Best performing product
best_product = np.argmax(product_sales) + 1
print("Best Performing Product: Product", best_product)


print("\n" + "=" * 60)
print("✅ LAB 11 COMPLETED SUCCESSFULLY")
print("=" * 60)
