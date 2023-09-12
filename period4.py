restaurants = ["Raising Canes", "Chick Fil A", "Taco Bell", "McDonalds", "Burger King"]

print("Welsome to your resturant ranker! Your current ranking is ", restaurants,"! You can add and rank a new resturant")
new_restaurant = input("what restaurant would you like to add?")

def rank_restaurant(new_restaurant,restaurants):

    for i in range(len(restaurants)):
        str = "Do you you like A) ", new_restaurant, "or B) ", restaurants[i], "more? A/B "
        ranking = input(str)
        if ranking == "A":
            restaurants.insert(i,new_restaurant)
            break
        elif ranking == "B":
            continue

    return restaurants
print("you new ranking is", rank_restaurant(new_restaurant, restaurants))

