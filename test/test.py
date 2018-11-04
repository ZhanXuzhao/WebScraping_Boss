import re

if re.search("h.*5", "html5 开发", re.IGNORECASE):
    value = True
else:
    value = False

print(value)
