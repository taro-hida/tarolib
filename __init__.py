def parse_csv(csv_path):
	rv = []
	with open( csv_path ) as f:
		csv_data = f.read()
	
	lines = csv_data.splitlines()
	
	for line in lines:
		dict_data = line.split(',')
		rv.append(dict_data)

	return rv
