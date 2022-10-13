from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.



def unique_koala_facts(int): 
    fact_list = []
    i = int
    while i > 0:
        fact_list.append(str(random_koala_fact()))
        i -= 1
    return fact_list

if __name__ == "__main__":
    print(unique_koala_facts(4))    