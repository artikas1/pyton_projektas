import matplotlib.pyplot as plt

# Read data from the text file
file_path = 'sorted_dataset.txt'  
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse the data
data = [line.strip().split(',') for line in lines]

# Extract the first and second columns for the bar chart
x_values = [row[0] for row in data]
y_values = [row[1] for row in data]

# Create the bar chart
plt.bar(range(len(x_values)), y_values, tick_label=x_values)
plt.xlabel('X-Axis Label')  # Add a label for the x-axis
plt.ylabel('Y-Axis Label')  # Add a label for the y-axis
plt.title('Bar Chart of Data Set')  # Add a title for the chart

# Display the chart
plt.show()
