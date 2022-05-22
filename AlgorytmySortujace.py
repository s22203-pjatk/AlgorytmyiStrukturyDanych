import numpy
import time
import sys

sys.setrecursionlimit(10000)


###############################################################
def open_tab_random():
    random_tab = numpy.random.randint(1, high=500, size=500000)
    n = open('random_tab.txt', 'w')
    n.write('{}'.format(random_tab))
    n.close()
    return random_tab


def read_tab_random():
    costam = open("random_tab.txt", "r")
    print("Nowa tablica --> ", open_tab_random())
    costam.close()
    return open_tab_random()


###############################################################
def open_tab_sort():
    sort_tab = list(range(1, 500000))
    n = open('sort_tab.txt', 'w')
    n.write('{}'.format(sort_tab))
    n.close()
    return sort_tab


def read_tab_sort():
    costam = open("sort_tab.txt", "r")
    costam.close()
    return open_tab_sort()


###############################################################
def open_tab_resort():
    resort_tab = []
    for i in range(500000, 0, -1):
        resort_tab.append(i)
    n = open('resort_tab.txt', 'w')
    n.write('{}'.format(resort_tab))
    n.close()
    return resort_tab


def read_tab_resort():
    costam = open("resort_tab.txt", "r")
    costam.close()
    return open_tab_resort()


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
###############################################################
start_time = time.time()
heapsort(read_tab_random())
print("heapsort random %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
heapsort(read_tab_sort())
print("heapsort sort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
heapsort(read_tab_resort())
print("heapsort resort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
###############################################################
###############################################################
###############################################################
start_time = time.time()
mergesort(read_tab_random())
print("mergesort random %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
mergesort(read_tab_sort())
print("mergesort sort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
mergesort(read_tab_resort())
print("mergesort resort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
###############################################################
###############################################################
###############################################################
start_time = time.time()
bubblesort(read_tab_random())
print("bubblesort random %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
bubblesort(read_tab_sort())
print("bubblesort sort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
bubblesort(read_tab_resort())
print("bubblesort resort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
###############################################################
###############################################################
###############################################################
start_time = time.time()
quicksort(read_tab_random(), 0, 499999)
print("quicksort random %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
quicksort(read_tab_sort(), 0, 499999)
print("quicksort sort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
start_time = time.time()
quicksort(read_tab_resort(), 0, 499999)
print("quicksort resort %s sec" % (time.time() - start_time))
start_time = 0
###############################################################
