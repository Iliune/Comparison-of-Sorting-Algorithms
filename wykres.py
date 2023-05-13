import matplotlib.pyplot as plt

times = [0.01869509800337255, 0.03322266300208867, 0.5722191789979115, 0.028588143000379204, 0.261198846003972, 0.27606634600088]

labels = ['metoda sort()', 'Merge Sort', 'sortowanie bąbelkowe', 'sortowanie powłowki', 'sortowanie przez wstawianie', 'sortowanie przez wybór']

plt.bar(labels, times)

plt.title('Execution Times')

plt.ylabel('Time (seconds)')

plt.show()
