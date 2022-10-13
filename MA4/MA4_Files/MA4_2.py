#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
from matplotlib import pyplot as plt


def fib_py(n):
    if n <= 0:
        return 1
    else:
        return fib_py(n-1) + fib_py(n-2)
    
@njit
def fib_numba(n):
    if n <= 0:
        return 1
    else:
        return fib_numba(n-1) + fib_numba(n-2)


def main():
	
	py_times = []
	numba_times = []
	
	N = [5, 10, 15, 20, 25, 30]
	for n in N:
		start = pc()
		fib_py(n)
		py_times.append(pc()-start)
  
		start = pc()
		fib_numba(n)
		numba_times.append(pc()-start)
  
	plt.plot(N, py_times)
	plt.plot(N, numba_times)
 
	plt.legend(["Python", "Numba"])
 
	plt.savefig("plot.png")

if __name__ == '__main__':
	main()
