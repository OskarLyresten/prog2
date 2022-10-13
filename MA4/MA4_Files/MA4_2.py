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
	steps = range(40)
	
	for n in steps:
		print(f"Step: {n}")
		start = pc()		# Regular Python 
		fib_py(n)
		py_times.append(pc()-start)
  
		start = pc()		# Python with Numba
		fib_numba(n)
		numba_times.append(pc()-start)

		f = Person(n)		# C++
		start = pc()
		f.fib()
		cpp_times.append(pc()-start)
	
	start = pc()
	fib_numba(47)
	numba47 = pc()-start	# Time for fib(47) with Numba
 
	f = Person(47)
	start = pc()
	f.fib()
	cpp47 = pc()-start	# Time for fib(47) with Numba
 
 
	plt.plot(steps, py_times)
	plt.plot(steps, numba_times)
	plt.plot(steps, cpp_times)
	
	plt.xlabel("n")
	plt.ylabel("Time for fib(n)")
 
	plt.legend(["Python", "Numba", "C++"])
 
	plt.savefig("plot.png")
 
	print(f"fib(47) with Numba took {numba47} seconds")
	print(f"fib(47) with C++ took {cpp47} seconds")

if __name__ == '__main__':
	main()
