#！usr/bin/env python

import sys
import re

str_input = input('please input a word:\n')
str_input
p1 = re.compile(r'[a-zA-Z]', re.I)				# only match word
p2 = re.compile(r'[^aeiouAEIOU]', re.I)			# only match consonant
match1 = p1.match(str_input)
if match1:
	match2 = p2.search(str_input)
	if match2:
		print(match2)
		id_tuple = match2.span()
		id_match = id_tuple[0]
		if id_match == 0:
			print('new string:', str_input[1:] + '-' + str_input[0] + 'ay')
		else:
			print('new string:', str_input[:id_match] + str_input[(id_match+1):] + '-' + str_input[id_match] + 'ay')
	else:
		print('no vowel character')
else:
	print('This is not a valid word')
		

