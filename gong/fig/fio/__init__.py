from os.path import join

base_path = 'C:\\dev\\NLstudy\\pythonstudy\\gong\\fig\\assets'

def read(data):
    path = join(base_path, data)

    with open(path, 'r') as test_file:
    	return test_file.readline().strip()
