import matplotlib.pyplot as plt

# Execution times of the two programs
times = [0.01869509800337255, 0.03322266300208867, 0.5722191789979115, 0.028588143000379204, 0.261198846003972, 0.27606634600088]

# Labels for the x-axis
labels = ['metoda sort()', 'Merge Sort', 'sortowanie bąbelkowe', 'sortowanie powłowki', 'sortowanie przez wstawianie', 'sortowanie przez wybór']

# Create a bar graph
plt.bar(labels, times)

# Set the title of the graph
plt.title('Execution Times of Two Programs')

# Set the label for the y-axis
plt.ylabel('Time (seconds)')

# Display the graph
plt.show()
