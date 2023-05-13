import timeit

test = '''
import random

def bubblesort(list):

    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = []
for i in range(3000):
    list.append(random.randint(0, 2999))

bubblesort(list)
print(list)

'''

czas = timeit.timeit(test, number = 100)/100
print(czas)