import numpy
from scipy import stats
import matplotlib.pyplot as plt

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

print("Mean : ", numpy.mean(speed))  # 89.7 (average)
print("Median : ", numpy.median(speed))  # 87.0 Middle value after sorting
print("Mode : ", stats.mode(speed))  # 86 Most occurring value

print("Standard Deviation : ", numpy.std(speed))  # How much spread out the values are
print("Variance : ", numpy.var(speed))  # Square of SD

print("Percentile 75 : ", numpy.percentile(ages, 75))  # 43 The age of 75% of people is 43 or less

print("Ten random floats : ", numpy.random.uniform(0.0, 5.0, 10))  # Generate 10 random floats between 0 and 5

# Data Distribution
plt.hist(numpy.random.uniform(0.0, 5.0, 100000), 5)  # Uniform
plt.show()

plt.hist(numpy.random.normal(5.0, 1.0, 100000), 100)  # Normal (Gaussian) - bell curve
plt.show()

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]  # Scatter plot x-axis
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]  # Scatter plot y-axis

plt.scatter(x, y)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)  # Mean 5, SD 1
y = numpy.random.normal(10.0, 2.0, 1000)  # Mean 10, SD 2

plt.scatter(x, y)
plt.show()
