charge = 35.00
numChars = int(input("How many characters are on the sign?: "))
woodType = str(input("Is the sign made of pine or oak?: "))
color = str(input("Is the text black or gold?: "))

if numChars > 5: 
    charge = charge + 4 * (numChars - 5)
   
if woodType == "pine":
    charge = charge
if woodType == "oak":
    charge = charge + 20.00

if color == "black":
    charge = charge
if color == "gold":
    charge = charge + 15.00

print(f"The charge for this sign is ${charge:.2f}")

#I initialized charge at 35.00 instead of 0.00 because of the set minimum.
#I edited the print statement to force a two decimal place output from a float instead of using a string.
