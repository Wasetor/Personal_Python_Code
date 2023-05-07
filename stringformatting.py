name1= "Solomon Tor Igbawase"
fname = input("Insert Firstname: ")
sname = input("Insert Surname: ")
age = int(input("Insert age: "))

# using the old style formatting
print("Your name is %s %s and you are %d years old" %(fname, sname, age))
print('have an amazing day %s' % (name1))

# using the new style formatting (str.formart())
print("Your name is {} {} and you are {} years old" .format(fname, sname, age))
print(" have an amazing day {}".format(name1))
# print strings without implicit conversion
print()
print("Your name is {:s} {:s} and you are {:d} years old" .format(fname, sname, age))
print(" have an amazing day {}" .format(name1))
# print strings using the index in the format list
print()
print("Your name is {1} {0} and you are {2} years old" .format(fname, sname, age))
print(" have an amazing day {}" .format(name1))
# f-string formatting style
print()
print(f"Your name is {fname} {sname} and you are {age} years old")
print(f"have an amazing day{name1}")

a = f"{2 + 6}"
type(a)
