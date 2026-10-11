# reverse the given number

#soln 1:
r = int(input("Enter a number to reverse: "))
rev = 0
while r > 0:
    digit = r % 10
    rev = rev * 10 + digit
    r = r // 10

print(rev)

#soln 2:
r1 = input("Enter a number to reverse: ")
print(r1[::-1])