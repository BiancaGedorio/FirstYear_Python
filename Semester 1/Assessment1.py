# Author: Bianca Gedorio
# Giving feedbacks to a student based results from a recent English and Maths exams
# First Year Assessment


# try and except statement
try:
    first_name = input("Please enter your name: ")
    english_results = int(input("What are your results for English: "))
    maths_results = int(input("What are your results in Maths: "))
    overall = 200
    percentage = 100

    # calculating the average results
    total = english_results + maths_results
    average = total / overall
    final_result = average * percentage

    # calculating the increase mark
    mark = 0.1 * 100
    multiply_mark = final_result * mark
    increase_mark = multiply_mark + final_result
    total = increase_mark / mark
    print(first_name, "your average mark is ", format(final_result, ".5f"))

    # if else statements
    if final_result > 90:
        print("Well done. Enjoy your weekend off!")
    elif english_results < 40 and maths_results < 40:
        print("Please discuss your English result with your English teacher.")
        print("Please discuss your Maths result with your Maths teacher.")
    else:
        print("Good work. Your target mark for the next exam is now ", format(total, ".5f"))
except ValueError:
    print("Error")
