from os.path import exists
from sys import argv

script, from_file, to_file = argv

print(f"Copying from {from_file}) to {to_file}")

# we could do the following on one row, get this to work 1st and then ..
in_file = open(from_file) ; indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print (f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRC_C to abort.")
input()

out_file = open(to_file, 'a')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()