from sys import argv
#read the WYSS section for how to run this
script, first, second, third , fourth = argv

print("The script is called:" , script)
print("Your first variable is:" , first)
print("Your second variable is:" , second)
print("Your third variable is:" , third)
print("Your fourth variable is:" , fourth)

#combining the inputs style from Lesson 12
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print(f"So, you're {age} years old, {height} tall, and weigh {weight}.")