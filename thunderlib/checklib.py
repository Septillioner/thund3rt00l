"""
        Author    : Septillioner <egeismailkosedag@gmail.com> or <septillioner@protonmail.com>
        Main      : thund3rt00l
"""

"""docstring for checklib.py"""
import re
class cnsts:
	http_regex = re.compile(r'(https|http)://')

def CheckURL(URL):
	return bool(cnsts.http_regex.match(URL))
