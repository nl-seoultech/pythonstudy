from deco.func import my_sum,my_cal


def test_my_sum():
	assert 55 == my_sum(1,2,3,4,5,6,7,8,9,10)
	assert 45 == my_sum(1,2,3,4,5,6,7,8,9)


def test_my_cal():
	assert 55 == my_cal(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, cal='+')