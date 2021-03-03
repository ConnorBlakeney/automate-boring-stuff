#! python3

import re, pyperclip

# Create regex for phone numbers
re.compile(r'''

# 555-555-5555, 555-5555, (555) 555-5555, 555-5555 ext 12345, ext. 12345, x12345 

((\d\d\d) | (\(\d\d\d)))? # area code (optional)

(\s|-) # first separator

/d/d/d# first three digits

- # separator

/d/d/d/d # last 4 digits

((ext(\.)?\s |x) # extension word part (optional)

(\d{2,5}))? # extension number part (optional)

''', re.VERBOSE)

# Regex for email

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+    # name
@    # @
[a-zA-Z0-9_.+]+     # domain

''', re.VERBOSE)

# get text from pyperclip clipboard

text = pyperclip.paste()