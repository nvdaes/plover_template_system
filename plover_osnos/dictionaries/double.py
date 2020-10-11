import os
import sys

sys.path.append(os.path.dirname(__file__))
import common
import semplice
del sys.path[-1]

LONGEST_KEY = 2

wordsWithDoubleStroke = {
	"Ccn": "camina"
	}


def lookup(key):
	value = wordsWithDoubleStroke.get(key[0])
	if value is None:
		raise KeyError
	common.lastValue = value
	if len(key) == 1:
		return " "
	value = common.reverseSearch(semplice.dict , key[1])
	if value[0] in ("a", "á", "e", "é", "i", "o", "ó"):
		value = common.lastValue[:-1] + value
	else:
		value = common.lastValue + value
	common.lastValue = value
	if value.endswith(" "):
		return value
	else:
		return value + "{^}"
