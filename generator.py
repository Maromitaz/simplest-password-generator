import random
list_base = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?', '`', '~']
def generate_no_repeat(lenght: int):
    return_pass = str()
    for _ in range(lenght):
        lett = random.choice(list_base)
        list_base.pop(list_base.index(lett))
        return_pass = f"{return_pass}{lett}"
    return return_pass

def generate_normal_random(lenght: int):
    return_pass = str()
    for _ in range(lenght):
        return_pass = f"{return_pass}{random.choice(list_base)}"
    return return_pass