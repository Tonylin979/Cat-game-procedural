cat_attributes = {
    "intelligence": 5,
    "energy": 10,
    "weight": 5,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("choose a colour for your cat: ")

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed your cat 4. Put it to sleep 5. Show stats: ")

    if option == '1':
        cat_attributes["energy"] -= 3
        cat_attributes["weight"] -= 2
        cat_attributes["intelligence"] += 1
        pass
    elif option == '2':
        cat_attributes["weight"] -= 1
        cat_attributes["intelligence"] += 3
        cat_attributes["energy"] -= 2
        pass
    elif option == "3":
        cat_attributes["weight"] += 3
        cat_attributes["energy"] -= 2
        cat_attributes["intelligence"] -= 1

        pass
    elif option == "4":
        cat_attributes["energy"] += 3
        cat_attributes["intelligence"] -= 1
        cat_attributes["weight"] -=2
        pass
    else:
        for keys,values in cat_attributes.items():
            print(keys)
            print(values)



    # finish off the if statements below
    if cat_attributes['energy'] < 5:
        if cat_attributes["intelligence"] <= 0 or cat_attributes["energy"] <=0 or cat_attributes["weight"] <= 0:
            print("Your cat has died")
            break
        elif cat_attributes["energy"] < 5:
            print("Cats energy is less than 5, too tired")
            pass
        elif cat_attributes["weight"] < 3:
            print("your cat is hungry, Feed your cat")
        pass


    # elif ...
    