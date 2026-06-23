# #### **1. Basic Plotting**
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10. Customize the plot with appropriate labels for the axes and a title.

# ---

# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.

# ---

# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)

#   Customize each plot with titles, axis labels, and different colors.

# ---

# #### **4. Scatter Plot**
# - **Task**: Create a scatter plot of 100 random points in a 2D space. The x and y values should be randomly generated from a uniform distribution between 0 and 10. Use different colors and markers for the points. Add a title, axis labels, and a grid.

# ---

# #### **5. Histogram**
# - **Task**: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1). Plot a histogram of the data with 30 bins. Add a title and axis labels. Adjust the transparency of the bars using the `alpha` parameter.


# ---

# #### **6. 3D Plotting**
# - **Task**: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ over the range of $ x $ and $ y $ values from -5 to 5. Use a suitable colormap and add a colorbar. Set appropriate labels for the axes and title.

# ---

# #### **7. Bar Chart**
# - **Task**: Create a vertical bar chart displaying the sales data for five different products: `['Product A', 'Product B', 'Product C', 'Product D', 'Product E']`. The sales values for each product are `[200, 150, 250, 175, 225]`. Customize the chart with a title, axis labels, and different bar colors.


# ---

# #### **8. Stacked Bar Chart**
# - **Task**: Create a stacked bar chart that shows the contribution of three different categories (`'Category A'`, `'Category B'`, and `'Category C'`) over four time periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period. Customize the chart with a title, axis labels, and a legend.

#task 1


import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x^2 - 4x + 4')
plt.grid(True)
plt.show()

#task 2
x = np.linspace(0, 2 * np.pi, 100)
sin_x = np.sin(x)
cos_x = np.cos(x)
plt.plot(x, sin_x, label='sin(x)', color='blue', linestyle='-', marker='o')
plt.plot(x, cos_x, label='cos(x)', color='orange', linestyle='--', marker='x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()
#task 3
x = np.linspace(-10, 10, 100)
y1 = x**3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(x + 1)
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].plot(x, y1, color='red')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0, 1].plot(x, y2, color='green')
axs[0, 1].set_title('f(x) = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')
axs[1, 0].plot(x, y3, color='blue')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')
axs[1, 1].plot(x, y4, color='purple')
axs[1, 1].set_title('f(x) = log(x + 1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

plt.tight_layout()
plt.show()

#task 4
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.scatter(x, y, color='magenta', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of Random Data')
plt.grid(True)
plt.show()

#task 5
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color='cyan', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normally Distributed Data')
plt.grid(True)
plt.show()
#task 6
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot of f(x, y) = cos(x^2 + y^2)')
plt.show()
#task 7
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.bar(products, sales, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data for Different Products')
plt.grid(axis='y')
plt.show()
#task 8
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.array([[10, 15, 20, 25], [5,  10, 15, 20], [2, 5, 10, 15]])
bar_width = 0.5
plt.bar(time_periods, data[0], color='red', label='Category A', width=bar_width)
plt.bar(time_periods, data[1], color='blue', label='Category B', width=bar_width, bottom=data[0])
plt.bar(time_periods, data[2], color='green', label='Category C', width=bar_width, bottom=data[0] + data[1])
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart of Categories over Time')
plt.legend()
plt.grid(axis='y')
plt.show()


