#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
from matplotlib import pyplot as plt


def fib_py(n):
    if n <= 1:
        return 1
    else:
        return fib_py(n-1) + fib_py(n-2)
    
@njit
def fib_numba(n):
    if n <= 1:
        return 1
    else:
        return fib_numba(n-1) + fib_numba(n-2)


def main():
	
	# Calcualte fib(47) with Numba and C++
	numba47 = fib_numba(47)
 
	f = Person(47)
	cpp47 = f.fib()
	
	print(f"fib(47) with Numba = {numba47:,}")
	print(f"fib(47) with C++ = {cpp47:,}\n")
	
 
	fig, ax = plt.subplots(1,2)		# Initiate plot
	
	
	# Compare regular Python, Python with Numba and C++
	py_times = []		# Times it takes Python to calculate fib(n)
	numba_times = []	# Times it takes Numba to calculate fib(n)
	cpp_times = []		# Times it takes C++ to calculate fib(n)
	steps = range(30,46)
	
	for n in steps:
		print(f"Step: {n}: ", end ="")
		step_timer = pc()
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

		print(f"{pc()-step_timer:.8} seconds")
	
	# First subplot
	ax[0].plot(steps, py_times)
	ax[0].plot(steps, numba_times)
	ax[0].plot(steps, cpp_times)
	
	ax[0].set_xlabel("n")
	ax[0].set_ylabel("Time for fib(n)")
 
	ax[0].legend(["Python", "Numba", "C++"])
  
	
	# Comparing regular Python with Python + Numba
	py_times = []		# Times it takes Python to calculate fib(n)
	numba_times = []	# Times it takes Numba to calculate fib(n)
	cpp_times = []		# Times it takes C++ to calculate fib(n)
	steps = range(20,31)
	
	for n in steps:
		print(f"Step: {n}: ", end ="")
		step_timer = pc()
		start = pc()		# Regular Python 
		fib_py(n)
		py_times.append(pc()-start)
	
		start = pc()		# Python with Numba
		fib_numba(n)
		numba_times.append(pc()-start)

		print(f"{pc()-step_timer:.8} seconds")
  
	
	# Second subplot
	ax[1].plot(steps, py_times)
	ax[1].plot(steps, numba_times)
	
	ax[1].set_xlabel("n")
 
	ax[1].legend(["Python", "Numba"])
	
 
	fig.suptitle(f"Numba: fib(47) = {numba47:.}    C++: fib(47) = {cpp47:.}")
 
	fig.savefig("plot.png")
 


if __name__ == '__main__':
	main()
