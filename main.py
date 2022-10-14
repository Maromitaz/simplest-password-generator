import random, os
list_base = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?', '`', '~']
lenght_password = 75
password = random.choice(list_base)
def generate():
    lett = random.choice(list_base)
    if (lett in list_base):
        list_base.pop(list_base.index(lett))
    return lett
if __name__ == '__main__':
    for i in range(lenght_password):
        lett = generate()
        password = f"{password}{lett}"
    if os.path.exists("password.txt"):
        os.remove("password.txt")
    f = open("password.txt" , "a")
    f.write(password)
    f.close()
