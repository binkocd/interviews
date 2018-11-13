message = "This is a test. This meassage is only a test. No missles are actually heading toward you at this time. Carry on, my wayward son."

count = {}
count_uppers = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

for character in message.upper():
    count_uppers.setdefault(character, 0)
    count_uppers[character] = count_uppers[character] + 1

print("This is the count as is: ")
print(count)
print("This is with everything converted to upper case: ")
print(count_uppers)
