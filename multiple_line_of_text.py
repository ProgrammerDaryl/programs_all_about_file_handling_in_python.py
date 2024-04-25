# write multiple lines of text contents into a text file, named "mylife.txt"
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
            