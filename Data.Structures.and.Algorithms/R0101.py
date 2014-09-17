"""
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""


def is_multiple(n: int, m: int) -> bool:
	return 0 != m and n % m == 0


# Tests
for i in range(-10, 10):
	for j in range(-10, 10):
		print("is_multiple(%i, %i): %s" % (i, j, is_multiple(i, j)))