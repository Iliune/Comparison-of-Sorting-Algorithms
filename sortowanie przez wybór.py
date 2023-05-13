import timeit

test = '''
import random

def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


list = []
for i in range(3000):
    list.append(random.randint(0, 2999))

selection_sort(list)
print(list)
'''

czas = timeit.timeit(test, number = 100)/100
print(czas)