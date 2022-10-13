# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

def alphabetical_order(list): 
    return sorted(list)

def won_golden_globe(film):
    win_list = ["Jaws", "Star Wars: Episode IV", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]
    a = (map(lambda x: x.lower(), win_list))
    win_list_lower = list(a)
    print(film.lower())
    print(win_list_lower)
    if film.lower() in win_list_lower:
     return True
    else: 
     return False

def remove_toto_albums(list):
    if "Fahrenheit" in list: list.remove("Fahrenheit")
    if "The Seventh One" in list: list.remove("The Seventh One")
    if "Toto XX" in list: list.remove("Toto XX")
    if "Falling in Between" in list: list.remove("Falling in Between")
    if "Toto XIV" in list: list.remove("Toto XIV")
    if "Old Is New" in list: list.remove("Old Is New")
    return list


