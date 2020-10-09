LONGEST_KEY = 1

dict = {
	"SC": ("casa", "ca"),
	"N": ("nana", "n")
}

lastValue = ""

def lookup(key):
	global lastValue
	value = ""
	if dict.get(key[0]) is not None:
		value = dict.get(key[0])[0] 
		if value == "":
			value = dict.get(key[0])[1]
	if value == "":
		searchKey = key[0][:]
		searchKeyValue = ""
		while len(searchKey) > 0:
			if dict.get(searchKey) is not None:
				searchKeyValue = dict.get(searchKey)[1]
			if searchKeyValue == "":
				searchKey = searchKey[:len(searchKey)-1]
			else:
				value += searchKeyValue
				searchKeyValue = ""
				searchKey = key[0][len(searchKey):]
	lastValue = value
	return value