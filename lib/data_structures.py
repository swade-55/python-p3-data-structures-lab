spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = []
    for food in spicy_foods:
        new_list.append(food['name'])
    return new_list

def get_spiciest_foods(spicy_foods):
    new_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            new_list.append(food)
            break
    return new_list

def print_spicy_foods(spicy_foods):
    resultant_string = "🌶"
    for food in spicy_foods:
        print(food["name"] + " (" + food["cuisine"] + ") " + "| "+"Heat Level: "+(resultant_string*food['heat_level']))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    resultant_string = "🌶"
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(food["name"] + " (" + food["cuisine"] + ") " + "| "+"Heat Level: "+(resultant_string*food['heat_level']))
            

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food['heat_level']
    average_heat = int(total_heat/len(spicy_foods))
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
#need help with create_spicy_food method