# for i in range(0, 100, 5): # range(start, stop (-1), krok)
#     print ("i is {} ". format(i))

for n in range(0, 4):
    print("n is ", n)
    for m in range(0, 4):
        print("m is ", m, end=" ")
    print("\n")

# Wynik:
# n is  0
# m is  0 m is  1 m is  2 m is  3
#
# n is  1
# m is  0 m is  1 m is  2 m is  3
#
# n is  2
# m is  0 m is  1 m is  2 m is  3
#
# n is  3
# m is  0 m is  1 m is  2 m is  3