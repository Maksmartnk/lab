words = "напишіть число1-дію-число2 (з пробілами між символами):"
while True:
    
	a, b, c = input(words).split()
	a, c = float(a), float(c)
	if c == 0:
		print("ділення на 0 неможливе!")
		continue

	if b == "+": print(f"{a+c}")
	
	elif b == "-": print(f"{a-c}")
	
	elif b == "*": print(f"{a*c}")
	
	elif b == "/": print(f"{a/c}")

	else: print("Не відома операція!")
