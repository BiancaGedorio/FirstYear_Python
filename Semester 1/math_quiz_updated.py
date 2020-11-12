# Author: Bianca Gedorio

import random
output_file_questions = open("math_quiz_questions.txt", 'w')
output_file_questions_and_answer = open("math_quiz_questions_and_answer.txt", 'w')

try:
    print("Welcome to your Math Quiz!")
    class_name = str(input("What is your class' name? "))
    teacher_name = str(input("What is your name? "))
    questions_num = int(input("Number of question? "))
    choice = int(input("1. Specific \n2. Random \nChoose one: "))
    score = 0
    if choice == 1:
        math_operator = str(input("+,-,*,/" + "\nChoose one: "))
        output_file_questions.write("Class: " + class_name + '\n' +
                                    "Teacher: " + teacher_name + '\n')
        output_file_questions.write("_______________________________" + '\n')
        output_file_questions_and_answer.write("Class: " + class_name + '\n' +
                                               "Teacher: " + teacher_name + '\n')
        output_file_questions_and_answer.write("_______________________________" + '\n')

        if math_operator == "+":
            for questions_num in range(1, questions_num):
                ops_1 = '+'
                rand = random.randint(1, 12)
                rand2 = random.randint(1, 12)
                maths = eval(str(rand) + str(ops_1) + str(rand2))
                specific_questions = ('{} : '.format(questions_num) +
                                      "{:.0f} {} {:.0f} = ___".format(rand, ops_1, rand2))
                specific_answer = ('{} : '.format(questions_num) +
                                   "{:.0f} {} {:.0f} = ".format(rand, ops_1, rand2) + str(maths))
                output_file_questions.write(str('\n' + specific_questions))
                output_file_questions_and_answer.write('\n' + specific_answer)

        if math_operator == "-":
            for questions_num in range(1, questions_num):
                ops_2 = '-'
                rand = random.randint(1, 12)
                rand2 = random.randint(1, 12)
                if rand > rand2:
                        maths = int(rand - rand2)
                        output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                        "{:.0f} {} {:.0f} = ____".format(rand, ops_2, rand2)))
                        output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                                   "{:.0f} {} {:.0f} = ".format(rand, ops_2, rand2)
                                                                   + str(maths)))
                elif rand2 > rand:
                        maths = int(rand2 - rand)
                        output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                        "{:.0f} {} {:.0f} = ____".format(rand2, ops_2, rand)))
                        output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                                   "{:.0f} {} {:.0f} = ".format(rand2, ops_2, rand)
                                                                   + str(maths)))
        if math_operator == "*":
            for questions_num in range(1, questions_num):
                ops_3 = '*'
                rand = random.randint(1, 12)
                rand2 = random.randint(1, 12)
                maths = eval(str(rand) + str(ops_3) + str(rand2))
                specific_questions = ('{} : '.format(questions_num) +
                                      "{:.0f} {} {:.0f} = ___".format(rand, ops_3, rand2))
                specific_answer = ('{} : '.format(questions_num) +
                                   "{:.0f} {} {:.0f} = ".format(rand, ops_3, rand2) + str(maths))
                output_file_questions.write(str('\n' + specific_questions))
                output_file_questions_and_answer.write('\n' + specific_answer)

        if math_operator == "/":
            for questions_num in range(1, questions_num):
                ops_4 = '/'
                rand = random.randint(1, 12)
                rand2 = random.randint(1, 12)

                if rand > rand2:
                    maths = int(rand / rand2)
                    output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                    "{:0.0f} {} {:0.0f} = ____".format(rand, ops_4, rand2)))
                    output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                               "{:0.0f} {} {:0.0f} = ".format(rand, ops_4, rand2)
                                                               + str(maths)))
                elif rand2 > rand:
                    maths = int(rand2 / rand)
                    output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                    "{:0.0f} {} {:0.0f} = ____".format(rand2, ops_4, rand)))
                    output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                               "{:0.0f} {} {:0.0f} = ".format(rand2, ops_4, rand)
                                                               + str(maths)))

    if choice == 2:
        output_file_questions.write("Class: " + class_name + '\n' +
                                    "Teacher: " + teacher_name + '\n')
        output_file_questions.write("_______________________________" + '\n')
        output_file_questions_and_answer.write("Class: " + class_name + '\n' +
                                               "Teacher: " + teacher_name + '\n')
        output_file_questions_and_answer.write("_______________________________" + '\n')

        for questions_num in range(1, questions_num):
            ops = ['+', '-', '*', '/']
            operation = random.choice(ops)
            if operation == "+":
                    rand = random.randint(1, 12)
                    rand2 = random.randint(1, 12)
                    maths = eval(str(rand) + str(operation) + str(rand2))
                    specific_questions = ('{} : '.format(questions_num) +
                                          "{:.0f} {} {:.0f} = ___".format(rand, operation, rand2))
                    specific_answer = ('{} : '.format(questions_num) +
                                       "{:.0f} {} {:.0f} = ".format(rand, operation, rand2) + str(maths))
                    output_file_questions.write(str('\n' + specific_questions))
                    output_file_questions_and_answer.write('\n' + specific_answer)

            if operation == "-":
                    rand = random.randint(1, 12)
                    rand2 = random.randint(1, 12)
                    if rand > rand2:
                        maths = int(rand - rand2)
                        output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                        "{:.0f} {} {:.0f} = ____".format(rand, operation, rand2)))
                        output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                                   "{:.0f} {} {:.0f} = ".format(rand, operation, rand2)
                                                                   + str(maths)))
                    elif rand2 > rand:
                        maths = int(rand2 - rand)
                        output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                        "{:.0f} {} {:.0f} = ____".format(rand2, operation, rand)))
                        output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                                   "{:.0f} {} {:.0f} = ".format(rand2, operation, rand)
                                                                   + str(maths)))
            if operation == "*":
                    rand = random.randint(1, 12)
                    rand2 = random.randint(1, 12)
                    maths = eval(str(rand) + str(operation) + str(rand2))
                    specific_questions = ('{} : '.format(questions_num) +
                                          "{:.0f} {} {:.0f} = ___".format(rand, operation, rand2))
                    specific_answer = ('{} : '.format(questions_num) +
                                       "{:.0f} {} {:.0f} = ".format(rand, operation, rand2) + str(maths))
                    output_file_questions.write(str('\n' + specific_questions))
                    output_file_questions_and_answer.write('\n' + specific_answer)

            if operation == "/":
                    rand = random.randint(1, 12)
                    rand2 = random.randint(1, 12)

                    if rand > rand2:
                        maths = int(rand / rand2)
                        output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                        "{:0.0f} {} {:0.0f} = ____".format(rand, operation, rand2)))
                        output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                                   "{:0.0f} {} {:0.0f} = ".format(rand, operation, rand2)
                                                                   + str(maths)))
                    elif rand2 > rand:
                        maths = int(rand2 / rand)
                        output_file_questions.write(str('\n' + '{} : '.format(questions_num) +
                                                        "{:0.0f} {} {:0.0f} = ____".format(rand2, operation, rand)))
                        output_file_questions_and_answer.write(str('\n' + '{} : '.format(questions_num) +
                                                                   "{:0.0f} {} {:0.0f} = ".format(rand2, operation, rand)
                                                                   + str(maths)))
    output_file_questions.close()
    output_file_questions_and_answer.close()
except ValueError:
    print("Error")
