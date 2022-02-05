#From a dict,how can we print the key whose value has max frequency
from collections import Counter
s = 'welcome'
d = dict(Counter(s))
print(d)

print(max(d, key = d.get))
val = d.values()
print(max(val))
