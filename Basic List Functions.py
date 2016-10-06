car = []
new_car = ""

print("please enter a car brand, when finished enter done")
while new_car != "done":
    new_car = raw_input("please enter a car brand: ")
    if new_car != "done":
        car.append(new_car)
for truck in car:
    print truck
print ("\n")


