import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# we check if the dimensions are right and if 
	# there's actually a row component in a
	a = np.array(a)
	b = np.array(b)

	if a.size == 0 or a.shape[0] != b.size:
		return -1

	return list(a @ b)
	
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	return [sum(x * y for x,y in zip(row, b)) for row in a]