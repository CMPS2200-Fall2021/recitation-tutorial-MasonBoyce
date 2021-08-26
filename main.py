def sum_of_squares(a):
	total = 0
	for i in a:
		square = i ** 2
		total += square
	return total

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([5,6,7]) == 110
