# create txt file for the 20 integers, named integers.txt
# read the content of integers.txt
with open("integers.txt", "r") as integers_file:
    for number in integers_file:
        number = int(number)
        # check if the integers are divisible by 2
        if number % 2 == 0:
            #squared the even numbers
            squared = number **2
