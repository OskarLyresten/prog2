#!/usr/bin/env python3

from person import Person
from numba import njit

def main():
	f = Person(5)
	print(f.fib())

if __name__ == '__main__':
	main()
