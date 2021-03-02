import re

phoneNumString = "Call me at 415-555-1111 today or 415-555-2222 tomorrow."
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(phoneNumString)
print(mo)
