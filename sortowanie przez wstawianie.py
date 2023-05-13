import timeit

test = '''
import random

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

list = []
for i in range(3000):
    list.append(random.randint(0, 2999))

insertion_sort(list)
print(list)
'''

czas = timeit.timeit(test, number = 100)/100
print(czas)