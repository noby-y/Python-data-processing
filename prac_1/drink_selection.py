drinks = {1 : "Cola", 2 : "Fanta", 3 : "Water", }

drink_choice = int(input(f"""Choose your drink:
{drinks.values()}"""))


def assign_to_tank(aquarium_creatures, new_tank_number):
	def apply(x):
		x["tank number"] = new_tank_number
		return x
	return map(apply, aquarium_creatures)

print(f"You chose {drinks[drink_choice]}")

#* Match case test 
# match drink_choice:
#     case 1:
#         print("You chose Cola")
#     case 2:
#         print("You chose Fanta")
#     case 3:
#         print("You chose Water")