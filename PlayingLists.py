even = [2, 4, 5, 6, 7, 9]

another_even = list(even)  #użycie '==' nie działa
another_even.sort(reverse=True)

print("Even jest rowne", even)
print("another_even jest rowne", another_even)