st = input('Enter a string: ')
sound = "aAeEiloOuU"
k=0
for char in st:
     if char in sound:
         k = k+1
print(f"there is/are {k} sound letters in '{st}'.\n ")
