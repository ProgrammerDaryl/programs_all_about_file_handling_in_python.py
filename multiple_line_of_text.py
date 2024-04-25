# write multiple lines of text contents into a text file, named "mylife.txt"

#add greetings
import pyfiglet
from colorama import Fore, Back, Style
greetings = pyfiglet.figlet_format("Greetings, Milord!", font = "slant" )
print(Fore.CYAN + greetings)

# the user will input his/her content

proceed = True
while proceed:
    line = input(Fore.YELLOW + "Please enter your line here, Milord: " )
    break_line = line+("\n")
    # txt file to show content of the multiple lines
    with open("mylife.txt", "a") as output_of_my_life_text:
        output_of_my_life_text.write(break_line)
        while proceed:
            #ask the user if he/she still wants to continue the program
            rerun = input(Fore.LIGHTGREEN_EX + "Are there any more lines you want to share, Milord y/n? ")
            if rerun.lower() == "y":
                break
            elif rerun.lower() == "n":
                proceed = False
            else:
                print(Fore.LIGHTRED_EX + "Those words are INVALID, please type y or n only, Milord.")
                continue