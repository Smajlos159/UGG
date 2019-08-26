import random, os, datetime, time, ctypes
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

ctypes.windll.kernel32.SetConsoleTitleW("Ultimate Giftcard/pattern Generator") # Console Title

def randomchar(replacer):
        global output
        character = random.choice(replacer)
        output += character  


print("""ULTIMATE GIFTCARD/CODE PATTERN GENERATOR


? = Random letter or number
! = Random letter
) = Random uppercase letter
( = Random lowercase letter
] = Random uppercase letter or number
[ = Random lowercase latter or number
* = Random number

""")
output_list = [] # Used for the non-duplicates mode
progress = 0 # Used for progress % in the  console title
date = str(datetime.datetime.now()).replace(":","-")
if not os.path.isdir("Results"):
        os.mkdir("Results")
input_pattern = list(input("> Pattern?\n> "))
output_f = open(f"Results\\{date[:19]}.txt", "w")
while True:
        try:
                number_codes = int(input("> How many codes do you want to generate?\n> "))
                break
        except ValueError:
                print("> Only numbers!")
while True:  
        duplicates_answer = input("> Do you want to filter out duplicates (Yes/No)? [SLOW]\n> ")
        if duplicates_answer == "Yes" or duplicates_answer == "yes":
                duplicates = True
                break
        elif duplicates_answer == "No" or duplicates_answer == "no":
                duplicates = False
                break
        else:
                print("> Only Yes/No!")
print("> Generating codes...")


start_time = time.time() # Starting point for timer
for output in range(number_codes):
        output = ""
        for character in input_pattern:
                if  character == "?":
                        randomchar(ascii_letters + digits)
                elif  character == "!":
                        randomchar(ascii_letters)
                elif  character == "(":
                        randomchar(ascii_lowercase)
                elif  character == ")":
                        randomchar(ascii_uppercase)
                elif  character == "[":
                        randomchar(ascii_lowercase + digits)
                elif  character == "]":
                        randomchar(ascii_uppercase + digits)
                elif  character == "*":
                        randomchar(digits)
                else:
                        output += character
        if duplicates:
                output_list.append(output) 
                progress += 1 
                ctypes.windll.kernel32.SetConsoleTitleW(f"Ultimate Giftcard/pattern Generator [{int(progress / number_codes * 100)}%]") # Updates console title
        else:
                output_f.write(f"{output}\n")
                progress += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Ultimate Giftcard/pattern Generator [{int(progress / number_codes * 100)}%]") # Updates console title 
if duplicates:
        output_list = list(dict.fromkeys(output_list))
        for filtered_output in output_list:
                output_f.write(f"{filtered_output}\n")



finish_time = time.time() # Stopping point for timer
print(f"> Done in {round(finish_time - start_time, 2)} seconds! Output has been saved in the results directory.")
time.sleep(7.5)
exit
