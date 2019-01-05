#csvをparseして2次元arrayで返します
def parse_csv(csv_path):
	rv = []
	with open( csv_path ) as f:
		csv_data = f.read()
	
	lines = csv_data.splitlines()
	
	for line in lines:
		dict_data = line.split(',')
		rv.append(dict_data)

	return rv

#txtをparseしてarrayで返します
def parse_txt(txt_path):
	rv = []
	with open( txt_path ) as f:
		txt_data = f.read()
	
	rv = txt_data.splitlines()
	
	return rv
