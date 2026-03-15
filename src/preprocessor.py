def preprocess(raw):
	return '\n'.join([
		tmp 
		for line in raw.splitlines()
		if (tmp := line.strip()) and tmp[0] != '-'
	])