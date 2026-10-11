#identify whether the number is zero, positive or negative
num = int(input("Enter number: "))
if num==0:
    print("zero")
elif num > 0:
    print("positive")
else:
    print("negative")

# print("zero" if num==0 else "positive" if num>0 else "negative") can also be used 