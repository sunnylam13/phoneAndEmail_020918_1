# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# phoneAndEmail_020918_1.py - Finds phone numbers and email addresses on the clipboard...
# can use testData_020918_1.md

import pyperclip, re

#####################################
# PHONE REGEX
#####################################

phoneRegex = re.compile(r'''
		((\d{3}|\(\d{3}\))? # area code aka group 1
		(\s|-|\.)? # separator aka group 2
		(\d{3}) # first 3 digits aka group 3
		(\s|-|\.) # separator aka group 4
		(\d{4}) # last 4 digits aka group 5
		(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension aka group 6-8
		)
	''', re.VERBOSE)

#####################################
# END PHONE REGEX
#####################################

#####################################
# EMAIL REGEX
#####################################

# create email regex

emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+ # username
		@ # @ symbol
		[a-zA-Z0-9.-]+ # domain name
		(\.[a-zA-Z]{2,4}) # dot-something
		)
	''', re.VERBOSE)

#####################################
# END EMAIL REGEX
#####################################

#####################################
# FIND MATCHES IN CLIPPED TEXT
#####################################

# Find matches in clipboard text

text = str(pyperclip.paste()) # get a string value of the text on the clipboard

matches = []

for groups in phoneRegex.findall(text):
	print(phoneRegex.findall(text))
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])

	if (groups[8] != ''):
		phoneNum += ' x' + groups[8]

	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

#####################################
# END FIND MATCHES IN CLIPPED TEXT
#####################################

#####################################
# COPY RESULTS TO CLIPBOARD
#####################################

# copy results to the clipboard

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard: ')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')

#####################################
# END COPY RESULTS TO CLIPBOARD
#####################################

