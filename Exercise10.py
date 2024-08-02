word = input("Enter a string word: ")
number = int(input("Enter a number: "))
if word == "good" and 7 <= number <= 15:
    print("It's good")
elif word == "bad" and (number < 7 or number > 15):
    print("It's bad")