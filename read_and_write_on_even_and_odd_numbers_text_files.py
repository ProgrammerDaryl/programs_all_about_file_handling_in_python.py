# create a numbers.txt file
# read from the numbers.txt file
with open("numbers.txt", "r") as integers_file:
    # add a for loop
    for number in integers_file:
        # separation of even from odd numbers
        if int(number) % 2 == 0:
            # write even numbers in even.txt file
            with open("even.txt", "a") as output_of_even_numbers:
                output_of_even_numbers.write(number)
        else:
            # write odd numbers in odd.txt file
            with open("odd.txt", "a") as output_of_odd_numbers:
                output_of_odd_numbers.write(number)