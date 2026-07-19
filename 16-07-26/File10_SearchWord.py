file = open("sample.txt", "r")
data = file.read()
word = input("Enter the word to search: ")
if word in data:
    print("Word found.")
else:
    print("Word not found.")
file.close()