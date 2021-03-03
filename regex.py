#! python3

import re, pyperclip

# program that scrapes emails and phone numbers from documents

# Create regex for phone numbers

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Regex for email

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+    # name
@    # @
[a-zA-Z0-9_.+]+     # domain

''', re.VERBOSE)

# get text from pyperclip clipboard

text = pyperclip.paste()

# extract email and phone from text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

