# create txt file for the 20 integers, named integers.txt
# read the content of integers.txt
with open("integers.txt", "r") as integers_file:
    for number in integers_file:
        number = int(number)
# check if the integers are divisible by 2
        if number % 2 == 0:
# squared the even numbers
            squared = number **2
            with open("double.txt", "a") as output_of_squared_even_numbers:
                output_of_squared_even_numbers.write(str(squared) + "\n")
                # not divisible by 2, will be odd numbers
        else:
#cubed the odd numbers
            cubed = number **3
            with open("triple.txt", "a") as output_of_cubed_odd_numbers:
                output_of_cubed_odd_numbers.write(str(cubed) + "\n")
