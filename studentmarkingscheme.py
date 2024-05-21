from graphics import *

# Max amount to be entered
PASS_TOTAL = 120  
DEFER_TOTAL = 120 
FAIL_TOTAL = 120 

def histogram(students_data, win):
    scale = 2  # To scale the bars appropriately
    # Histogram bar and label modification
    # Calculate the data for all students
    pass_total_agg = sum(data[0] for data in students_data)
    defer_total_agg = sum(data[1] for data in students_data)
    fail_total_agg = sum(data[2] for data in students_data)

    progress_bar = Rectangle(Point(50, 250), Point(150, 250 - pass_total_agg * scale))
    progress_bar.setFill('green')
    progress_bar.draw(win)
    progress_label = Text(Point(100, 270), "Progress")
    progress_label.draw(win)

    trailer_bar = Rectangle(Point(200, 250), Point(300, 250 - defer_total_agg * scale))
    trailer_bar.setFill('yellow')
    trailer_bar.draw(win)
    trailer_label = Text(Point(250, 270), 'Trailer')
    trailer_label.draw(win)

    retriever_bar = Rectangle(Point(350, 250), Point(450, 250 - fail_total_agg * scale))
    retriever_bar.setFill('red')
    retriever_bar.draw(win)
    moduler_label = Text(Point(400, 270), "Retriever")
    moduler_label.draw(win)

    exclude_bar = Rectangle(Point(500, 250), Point(600, 250 - (pass_total_agg + defer_total_agg + fail_total_agg) * scale))
    exclude_bar.setFill('blue')
    exclude_bar.draw(win)
    exclude_label = Text(Point(550, 270), "Exclude")
    exclude_label.draw(win)

    total_students = len(students_data)  # Calculate total number of students entered
    total_label = Text(Point(300, 300), f"{total_students} outcomes in total")
    total_label.setSize(14)
    total_label.draw(win)

    win.getMouse()  # Wait for mouse to close the window
    win.close()

def main(): 
    students_data = []

    while True:  # Keep looping until the input values are correct
        # Prompt user for input variables
        pass_input = input("Please enter your credits at pass: ")  # Enter pass credit
        while True:  # Loop to check if an integer is required for input
            try:
                pass_input = int(pass_input)
                if pass_input not in [0, 20, 40, 60, 80, 100, 120]:  # Checking that it's not out of range
                    print('Out of range!')
                    pass_input = input("Please enter your credits at pass: ")
                    continue
                break
            except ValueError:
                print("Integer Required")
                pass_input = input("Please enter your credits at pass: ")  # Input an int() again if str() entered

        defer_input = input('Please enter your credits at defer: ')  # Enter defer credit
        while True:  # Loop to check if an integer is required for input
            try:
                defer_input = int(defer_input)
                if defer_input not in [0, 20, 40, 60, 80, 100, 120]:  # Checking that it's not out of range
                    print('Out of range!')
                    defer_input = input("Please enter your credits at defer: ")
                    continue
                break
            except ValueError:
                print("Integer Required")
                defer_input = input("Please enter your credits at defer: ")  # Input an int() again if str() entered

        fail_input = input('Please enter your credits at fail: ')  # Enter fail credit
        while True:  # Loop to check if an integer is required for input
            try:
                fail_input = int(fail_input)
                if fail_input not in [0, 20, 40, 60, 80, 100, 120]:  # Checking that it's not out of range
                    print('Out of range!')
                    fail_input = input("Please enter your credits at fail: ")
                    continue
                break
            except ValueError:
                print("Integer Required")
                fail_input = input("Please enter your credits at fail: ")  # Input an int() again if str() entered

        if pass_input < 0 or defer_input < 0 or fail_input < 0:
            print('Out of range!')  # Checking if the entered values are till the 120 range
        else:
            total = pass_input + defer_input + fail_input
            if total != 120:
                print('Total Incorrect!')
                continue
            elif pass_input == 120:
                print('Progress')
            elif pass_input == 100:
                print('Progress (module trailer)')
            elif pass_input <= 40 and fail_input >= 80:
                print('Exclude')
            else:
                print('Do not Progress - module retriever')

            students_data.append((pass_input, defer_input, fail_input))  # Stores the input data into the students_data list as tuples

        add_more = input("Do you want to add another set of data? 'y' for yes and 'q' for quit and display: ")
        if add_more == 'q':
            print('Launching histogram')
            win = GraphWin("Histogram", 1000, 800)
            win.setBackground('white')
            my_heading = Text(Point(140, 30), 'Histogram results')  # Define text
            my_heading.setTextColor("grey")
            my_heading.setSize(20)
            my_heading.setStyle("bold")
            my_heading.setFace("helvetica")
            my_heading.draw(win)
            histogram(students_data, win)
            display_results(students_data)
            break
        elif add_more == 'y':
            continue
        else:
            print('Invalid input, try again')

def display_results(students_data):
    # Calculating counts for each progression outcome
    pass_count = sum(1 for data in students_data if data[0] == 120 and data[1] == 0 and data[2] == 0)
    trailer_count = sum(1 for data in students_data if data[0] == 100 and data[1] in [20, 0] and data[2] in [0, 20])
    retriever_count = sum(1 for data in students_data if (data[0] in [80, 60, 40, 20] or data[0] == 0) and data[2] < 80)
    exclude_count = sum(1 for data in students_data if data[2] >= 80)

    # Print Results
    print("---Progression Outcome---\n")
    print(f"Progress: {pass_count}")
    print(f"Progress (Module Trailer): {trailer_count}")
    print(f"Do not progress (Module Retriever): {retriever_count}")
    print(f"Exclude: {exclude_count}")

    # Storing and saving the input data
    with open('progression_outcomes.txt', 'w') as file:
        file.write('---Progression Outcome---\n')
        file.write(f'Progress: {pass_count}\n')
        file.write(f"Progress (Module Trailer): {trailer_count}\n")
        file.write(f"Do not progress (Module Retriever): {retriever_count}\n")
        file.write(f'Exclude: {exclude_count}\n')
                
main()
