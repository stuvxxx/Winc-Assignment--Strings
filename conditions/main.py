# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


from ast import IsNot


def farm_action(weather, day_night, cow_need_milking, cow_loc, season, tank_full, grass_long):
    if cow_loc == "pasture" and day_night == "night" or weather == "rain": 
        print("take cows to cowshed")
        return str("take cows to cowshed")
    elif cow_need_milking: 
        if cow_loc == "cowshed":
            print("milk cows")
            return("milk cows")
        else: print("take cows to cowshed\nmilk cows\ntake cows back to pasture")
        return str("take cows to cowshed\nmilk cows\ntake cows back to pasture")
    elif tank_full and (weather == "rainy" or "neutral"):
        if cow_loc == "cowshed": 
            print("fertilize pasture")
            return("fertilize pasture")
        else: print("take cows to cowshed\nfertilize pasture\ntake cows back to pasture")
        return("take cows to cowshed\nfertilize pasture\ntake cows back to pasture")
    elif grass_long and season == "spring" and weather == "sunny": 
        if cow_loc == "cowshed": 
            return("mow grass")
        else: ("take cows to cowshed\nmow grass\ntake cows back to pasture")
    print("wait")
    return ("wait")
    



farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)