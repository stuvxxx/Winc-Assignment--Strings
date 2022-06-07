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
player = "Oleksiy Mykhaylychenko"
first_name_first_letter = player.find("O")
first_name_last_letter = player.find("y")
first_name = player[:first_name_last_letter + 1]
last_name_first_letter = player.find("M")
last_name_len = len(player[last_name_first_letter:])
name_short = player[first_name_first_letter] + ". " + player[last_name_first_letter:]
chant_fail = len(first_name) * (first_name + "! ")
chant = chant_fail.rstrip()
good_chant = chant[-1] != " "