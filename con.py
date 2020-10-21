n = int(input("Enter a number : "))
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

