# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)
report = scorer_1 + " scored in the " + str(goal_0) + "nd minute\n" + scorer_2 + " scored in the " + str(goal_1) + "th minute"
player = "Oleksij Mychajlytsjenko"
first_name = player[:player.find(" ")]
last_name = player[player.index(first_name) + 1 + len(first_name):]
last_name_len = len(last_name)
name_short = player[0] + ". " + last_name
print(name_short)
chant_fail = len(first_name) * (first_name + "! ")
chant = chant_fail.rstrip()
good_chant = chant[-1] != " "