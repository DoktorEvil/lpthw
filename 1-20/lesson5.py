#More variables and printing
m_name = 'Zed A. Shaw'
m_age = 35 # not a lie
m_height = 74 # inches
m_weight = 180 # lbs
m_eyes = 'Blue'
m_teeth = 'White'
m_hair = 'Brown'

#the {f function updates the format, there are 2 samples below, one w/ and one w/o
#print("Let's talk about {m_name}.")
print("Let's talk about", m_name)
print(f"He's {m_height} inches tall.")
print(f"He's {m_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {m_eyes} eyes and {m_hair} hair.")
print(f"His teeth are usually {m_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = m_age + m_height + m_weight
print(f"If I add {m_age}, {m_height}, and {m_weight} I get {total}.")