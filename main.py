import os, subprocess
# The generator
from generator import generate_no_repeat, generate_normal_random, list_base

# Console thingy
error_list = [
    "Please input a number.\n",
    "Unkown generating type, use only 1 or 2 for selection.\n",
    f"You must insert a number smaller than {len(list_base)}\n",
]
def main(error_status):
    try:
        subprocess.run(["cls"], check=True, shell=True)
    except subprocess.CalledProcessError:
        subprocess.run(["clear"], shell=True)

    if error_status > 0 & error_status < 4:
        print(error_list[error_status])
    
    password = ""
    print("What kind of a password would you like?\n1) Simple random;\n2) Simple random but with no repeating characters.\n")
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
        password = generate_normal_random(lenght_password)
    if password_type == 2:
        try:
            lenght_password = int(input(f"Password\'s lenght (can only be maximum of {len(list_base)} characters): "))
            if lenght_password > len(list_base):
                main(3)
            password = generate_no_repeat(lenght_password)
        except ValueError:
            main(1)
    if os.path.exists("password.txt"):
        os.remove("password.txt")
    f = open("password.txt" , "a")
    f.write(password)
    f.close()
    quit()
if __name__ == '__main__':
    main(0)