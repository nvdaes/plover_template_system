LONGEST_KEY = 1

dict = {
	"SC": ("casa", "ca")
}

lastValue = None

def lookup(key):
	assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
	global lastValue
	value = ""
	try:
		value = (dict[key])[0]
		lastValue = value
		return value
	except KeyError:
		pass
	n = len(key)
	searchKey = key[:]
	for n in range(n):
		lenSearchKey = len(searchKey)
		try:
			value += (dict[searchKey])[1]
			searchKey = key[lenSearchKey:]
		except KeyError:
			searchKey.pop()
	lastValue = value
	return value