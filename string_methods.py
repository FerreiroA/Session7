print(dir("hello"))

print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPOSED TO WORK?".capitalize())
print("Hello".center(50, "x"))
print("gmail.com".find("."))
print("gmail.com".find("John"))
s = "I see a cat who likes to cat while I cat on a cat"
# Find all occurrences
paz = 0
while True:
    paz = s.find("cat", paz)
    if paz == -1:
        break
    print("found cat on position", paz)
    paz += 1

# Join we will come back later

# Lower
s = "I SEE A LOT OF THINGS!"
print(s.lower())

# Replace replaces x with y
s = "I see a cat who likes to eat a rat. What a good cat."
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s = "Hello, kind sir! How are you today?"
print(s.replace(",", "").replace("!", "").replace("?", ""))

# Split
s = "I like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted)

# Title
s = "I like the mountains"
print(s.title())

# Upper
s = "i see a lot of things!"
print(s.upper())