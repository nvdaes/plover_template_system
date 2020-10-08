LONGEST_KEY = 1

DICT = {
    "CA": ("casa", "ca")
}

value = None

def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    global value
    searchKey = key[0]
    try:
        value = dict[searchKey][0]
        return value
    except:
        value = None
    n = 0
    while n < len(key)[0]
        searchKey = key[0][:-n]
        try:
            value = dict[searchKey][1]
            searchKey = key(:n)
        except KeyError:
            continue
    return value