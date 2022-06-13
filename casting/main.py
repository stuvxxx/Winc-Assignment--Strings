# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

from pickletools import int4
from tokenize import Number


leek_price = 2 

casting_string = "Leek is " + str(leek_price) + " euro per kilo."
print(casting_string)
order = "leek 4"
find_amount = order.find("4")
filter_number = slice(5,6) 
order_amount = order[filter_number]
sum_total = int(leek_price) * int(order_amount)
print(sum_total)

broccoli = 2.34
order = "broccoli 1.6"

