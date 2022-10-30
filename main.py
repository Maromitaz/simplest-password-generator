import random, os, subprocess
# The generator
list_base = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?', '`', '~']
def generate_no_repeat():
    lett = random.choice(list_base)
    if (lett in list_base):
        list_base.pop(list_base.index(lett))
    return lett

def generate_normal_random():
    return random.choice(list_base)

# Console thingy
def main(error_status):
    try:
        subprocess.run(["cls"], check=True, shell=True)
        print("Windows batch 🤮")
    except subprocess.CalledProcessError:
        subprocess.run(["clear"], shell=True)
        print("Not Windows 👍")
    if error_status == 0:
        pass
    if error_status == 1: 
        print("Please input a number.\n")
    if error_status == 2:
        print("Unkown generating type, use only 1 or 2 for selection.\n")
    if error_status == 3:
        print(f"You must insert a number smaller than {len(list_base)}\n")
    password = ""
    print("What kind of a password does your heart desire?\n1) Simple random;\n2) Simple random but with no repeating characters.\n")
    try:
        password_type = int(input("Input 1 or 2: "))
    except ValueError:
        main(2)
    if not (password_type == 1 or password_type == 2):
        main(1)
    if password_type == 1:
        try:
            lenght_password = int(input("Password lenght: "))
        except ValueError:
            main(1)
        for _ in range(lenght_password):
            lett = generate_normal_random()
            password = f"{password}{lett}"
    if password_type == 2:
        try:
            lenght_password = int(input(f"Password lenght (can only be maximum of {len(list_base)} characters): "))
            if lenght_password > len(list_base):
                main(3)
        except ValueError:
            main(1)
    for _ in range(lenght_password):
        lett = generate_no_repeat()
        password = f"{password}{lett}"
    if os.path.exists("password.txt"):
        os.remove("password.txt")
    f = open("password.txt" , "a")
    f.write(password)
    f.close()
    quit()
if __name__ == '__main__':
    main(0)