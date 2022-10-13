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
	
	
	for n in range(5,30):
		start = pc()
		fib_py(n)
		py_times.append(pc()-start)
  
		start = pc()
		fib_numba(n)
		numba_times.append(pc()-start)
  
	plt.plot(range(5,30), py_times)
	plt.plot(range(5,30), numba_times)
	
	plt.xlabel("Fib(n)")
	plt.ylabel("Time")
 
	plt.legend(["Python", "Numba"])
 
	plt.savefig("plot.png")

if __name__ == '__main__':
	main()
