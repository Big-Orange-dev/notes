def spin_wrds(sentence):
	a = sentence.split()
	for i in range(len(a)):
		# print(len(a[i]))
		if len(a[i]) > 5:
			a[i] = list(a[i])
			a[i].reverse()
			a[i] = "".join(a[i])
			# print(a[i])
	a = " ".join(a)
	return a

	
a = 'this is asdfghjkl'
print(spin_wrds(a))
