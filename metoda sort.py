import timeit

test = '''
import random

list = []
for i in range(3000):
    list.append(random.randint(0, 2999))

list.sort()

print(list)
'''

czas = timeit.timeit(test, number = 100)/100
print(czas)