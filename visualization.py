import matplotlib.pyplot as plt

# Function to read the dataset from a text file
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to visualize the sorted data
def visualize_sorted_data(sorted_dataset, selected_field_index, selected_field_name):
    # Extract data for visualization
    labels = [row.split(',')[0] for row in sorted_dataset]
    values = [float(row.split(',')[selected_field_index]) for row in sorted_dataset]  # Assuming you want to visualize the second column

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='blue')
    plt.xlabel('ID')
    plt.ylabel(selected_field_name)
    plt.title('Sorted Data Visualization')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Show the bar chart
    plt.show()

# Array of field names
field_names = [
    "Response Time",
    "Availability",
    "Throughput",
    "Successability",
    "Reliability",
    "Compliance",
    "Best Practices",
    "Latency",
    "Documentation",
    "WsRF",
    "Service Classification"
]

# Prompt user to choose a field for sorting
print("Choose a field for sorting:")
for i, field in enumerate(field_names, 1):
    print(f"{i}. {field}")

selected_field_index = int(input("Enter the index of the field you used for sorting: ")) - 1
selected_field_name = field_names[selected_field_index]

# Get user input for the file path of the sorted dataset
file_path = "sorted.txt"

# Read the sorted dataset from the text file
sorted_dataset = read_dataset(file_path)

# Visualize the sorted data
visualize_sorted_data(sorted_dataset, selected_field_index, selected_field_name)
