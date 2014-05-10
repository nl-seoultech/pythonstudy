from os.path import join
from fio import read

base_path = '/C/dev/NLstudy/pythonstudy/gong/fig/test'

data = 'data.txt'


def test_read():
    """ fio test
    """
    assert 'test_test' == read(data)

def test_join():
	from os.path import join
	front_path = 'c: bc'
	back_path = 'dabc.txt'
	assert 'c: bc\dabc.txt' == join(front_path, back_path)