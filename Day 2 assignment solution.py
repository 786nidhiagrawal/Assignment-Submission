#Lottery Project
s = input('Enter the lottery word: ')

freq = [0] * 26

#lowercase alphabets - ASCII CODE:97 TO 122
for i in s:
     freq[ord(i) - 97] += 1

print(freq) 
x = freq.index(max(freq))
print(x)
print(chr(97+x))




