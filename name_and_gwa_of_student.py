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
        for name, grade in txt_data.items():
            decimal_number = float(grade)
            if highest_gwa is None or decimal_number > float(highest_gwa):
                student_name_highest_gwa = name
                highest_gwa = grade
        return student_name_highest_gwa, highest_gwa
name, grade = find_highest_gwa(txt_file)
# add designs to your output from pyfiglet, colorama, and Fore
import pyfiglet
result = pyfiglet.figlet_format(f"{name} got the highest GWA, with a GWA of {grade}" + "!", font = "bulbhead")
print(result)