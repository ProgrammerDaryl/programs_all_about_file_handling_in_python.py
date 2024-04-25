# write multiple lines of text contents into a text file, named "mylife.txt"

#add greetings
import pyfiglet
from colorama import Fore
greetings = pyfiglet.figlet_format("Greetings Milord!", font = "slant" )
print(Fore.CYAN + Fore.LIGHTGREEN_EX + greetings)

# the user will input his/her content

proceed = True
while proceed:
    line = input("Enter your line here: ")
    break_line = line+("\n")
    # txt file to show content of the multiple lines
    with open("mylife.txt", "a") as output_of_my_life_text:
        output_of_my_life_text.write(break_line)
        while proceed:
            #ask the user if he/she still wants to continue the program
            rerun = input("Are there more lines y/n? ")
            if rerun.lower() == "y":
                break
            elif rerun.lower() == "n":
                proceed = False