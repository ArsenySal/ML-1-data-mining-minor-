s = 'sdfdsfds'
for i in range(len(s)):
	if s[i].isalpha():
		s = s[:i] + chr(ord(s[i]) + 1) + s[i+1:]
print(s)