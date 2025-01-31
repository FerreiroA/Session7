s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(s1, "hello")
print(3*s2)
# print(s1*s2)
print((10//2)*s1)
# len function gives you the size of the string
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(c*4, end="")

new_string = ""
for c in s2:
    new_string += c*4
print(new_string)

h = "h"
e = "e"
l = "l"
o = "o"
print(h*4+e*4+l*8+o*4)

print("h" is s1)
print("hello world" in s2)
print("wor" in s2)
