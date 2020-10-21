while True:
	i = input("Enter a number ('e' to exit) : ")
	if i == "e":
	break
	n = int(i)
	while True:
		if n % 2 == 0 and n != 1:
			n = n/2
			print(int(n),"- ",end="")
		elif n % 2 != 0 and n != 1:
			n = (3*n) + 1
			print(int(n),"- ",end ="")
		elif n == 1:
			print()
			break
