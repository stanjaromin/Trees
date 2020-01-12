
#przykład 1
for i in range(0, 100, 5): # range(start, stop (-1), krok)
    print ("i is {} ". format(i))

#przykład 2
for state in["not pinin", "no more", "a stiff", "bereth of life"]:
    print("This parrot is "+ state)
    #print("This parrot is {}".format(state))

#przykład 3
number = "9,22,334,567,45,654,654,6456,456"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))
# Nie można użyć takiej komendy: print("The number is "+ newNumber)
# ponieważ konkatenacja działą tylko dla stringów