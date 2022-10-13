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
	cpp_times = []
	steps = range(45)
	
	for n in steps:
		start = pc()		# Regular python 
		fib_py(n)
		py_times.append(pc()-start)
  
		start = pc()		# Python with numba
		fib_numba(n)
		numba_times.append(pc()-start)

		f = Person(n)		# C++
		start = pc()
		f.fib(n)
		cpp_times.append(pc()-start)
	
 
	plt.plot(steps, py_times)
	plt.plot(steps, numba_times)
	plt.plot(steps, cpp_times)
	
	plt.xlabel("n")
	plt.ylabel("Time for fib(n)")
 
	plt.legend(["Python", "Numba", "C++"])
 
	plt.savefig("plot.png")
 
	print("Saved plot as plot.png")

if __name__ == '__main__':
	main()
