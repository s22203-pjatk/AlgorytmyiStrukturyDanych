import copy
import time
import sys
import random

sys.setrecursionlimit(10**6)

###############################################################
random_tab = []

for x in range(0, 500000):
    random_tab.append(random.randint(0, 1000))
n = open('random_tab.txt', 'w')
n.write('{}'.format(random_tab))
n.close()

random_tab_copy = copy.copy(random_tab)
random_tab_copy_2 = copy.copy(random_tab)
random_tab_copy_3 = copy.copy(random_tab)

sort_tab = sorted(random_tab)
n = open('sort_tab.txt', 'w')
n.write('{}'.format(sort_tab))
n.close()

resort_tab = sort_tab[::-1]
n = open('resort_tab.txt', 'w')
n.write('{}'.format(resort_tab))
n.close()

resort_tab_copy = copy.copy(resort_tab)
resort_tab_copy_2 = copy.copy(resort_tab)
resort_tab_copy_3 = copy.copy(resort_tab)


###############################################################
def heapify(tab, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and tab[i] < tab[l]:
        largest = l
    if r < n and tab[largest] < tab[r]:
        largest = r
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, n, largest)


def heapsort(tab):
    n = len(tab)
    for i in range(n // 2, -1, -1):
        heapify(tab, n, i)
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, i, 0)


###############################################################
def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r, 1):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)


###############################################################
def mergesort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        left = tab[:mid]
        right = tab[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            tab[k] = right[j]
            j += 1
            k += 1


###############################################################
def bubblesort(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                temp = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1] = temp


###############################################################
###############################################################
###############################################################
###############################################################111

start_time = time.time()
heapsort(random_tab)
print("heapsort random %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
print("\n")
###############################################################

start_time = time.time()
heapsort(sort_tab)
print("heapsort sort %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
print("\n")
###############################################################

start_time = time.time()
heapsort(resort_tab)
print("heapsort resort %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
###############################################################
print("\n\n\n")
###############################################################
###############################################################222

start_time = time.time()
mergesort(random_tab_copy)
print("mergesort random %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
print("\n")
###############################################################

start_time = time.time()
mergesort(sort_tab)
print("mergesort sort %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
print("\n")
###############################################################

start_time = time.time()
mergesort(resort_tab_copy)
print("mergesort resort %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
###############################################################
print("\n\n\n")
###############################################################
###############################################################333

start_time = time.time()
quicksort(random_tab_copy_2, 0, len(random_tab) - 1)
print("quicksort random %s sec" % (time.time() - start_time))
start_time = 0

###############################################################
print("\n")
###############################################################
print("quicksort sort --exit code -1073741571 (0xC00000FD)--")
print("quicksort resort --exit code -1073741571 (0xC00000FD)--")
###############################################################
###############################################################
print("\n\n")
###############################################################
###############################################################444


start_time = time.time()
bubblesort(random_tab_copy_3)
print("bubblesort random %s sec" % (time.time() - start_time))
start_time = 0


###############################################################
print("\n")
###############################################################


start_time = time.time()
bubblesort(sort_tab)
print("bubblesort sort %s sec" % (time.time() - start_time))
start_time = 0


###############################################################
print("\n")
###############################################################


start_time = time.time()
bubblesort(resort_tab_copy_3)
print("bubblesort resort %s sec" % (time.time() - start_time))
start_time = 0


