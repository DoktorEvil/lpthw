def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enuff for a party!")
    print("Get a blanket! \n")


print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do the math inside too:")
cheese_and_crackers(10 + 20 - 13, 5 + 6 - 4)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("And with math we found out some was eaten")
cheese_and_crackers(amount_of_cheese + 100 - 25, amount_of_crackers + 1000 - 800)

prompt = '> '

print("How many pieces of cheese do you want?\n")
cheese_chunks = input(prompt)
print("How many crackers do you want?\n")
crackers = input(prompt)

print("\n")

print(f"Alright, you want {cheese_chunks} pieces of cheese and {crackers} crackers.\n")
