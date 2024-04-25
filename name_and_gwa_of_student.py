# create a students_data.txt file
# simplify your txt file for easy reading
txt_file = (r"students_data.txt")
def find_highest_gwa(txt_file):
    # read the content of the students_data.txt file
    with open(txt_file, "r") as students_grades:
        data = students_grades.read()
        txt_data = eval(data)
        highest_gwa = None
        student_name_highest_gwa = None
# adding a for loop
# add designs to your output from pyfiglet, colorama, and Fore