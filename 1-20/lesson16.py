from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.\n")
print("If you don't want to erase then, hit CTRL_C (^C).\n")
print("If you do want to erase the file, hit ENTER.\n")

input("That's the question?")

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for 3 lines.\n")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"I'm going to write these to the file.\n")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close the file, but wait! Don't you wanna see the guts?\n\n")
target.close()

txt = open(filename)
print(f"Opening your {filename}")
print(txt.read())




