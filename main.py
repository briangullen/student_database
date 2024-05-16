student_name = ["Kevin", "Jessica", "Jordan", "Nelly"]
hometown = ["Detroit", "Cleveland", "Jacksonville", "Austin"]
favorite_food = ["Pizza", "Cheeseburger", "Pasta", "Sushi"]


def provide_names():  # created so the printing of names can be called without code repetition
    print(f'Here are our students:')
    print(*student_name)
    print()


while True:
    while True:  # this loops through ensuring a correct number is provided by user
        prompt_names = input('Would you like to see the list of students? Please enter "y" or "n": ').lower()
        if prompt_names == "y":
            provide_names()
        else:
            print("You have chosen not to print the students names.")
        student_number = int(input("Which student would you like to know about? Enter a number 1-4: "))
        if 0 < student_number <= len(student_name):
            chosen_student = student_name[student_number - 1]
            print(f"Student {student_number} is {chosen_student}.")
            break
        else:
            print(f"Sorry you did not provide a valid response. Please try again.")

    while True:  # loops through ensuring a valid string is provided by user
        category_answer = input('What category would you like to know about? ("hometown" or "favorite food"): ').lower()
        if category_answer == "hometown":
            print(f"{chosen_student}'s hometown is {hometown[student_number - 1]}.")
            break
        if category_answer in "favorite food":
            print(f"{chosen_student}'s favorite food is {favorite_food[student_number - 1]}.")
            break
        else:
            print(f"Sorry you did not provide a valid response. Please try again.")
    keep_going = input("Would you like to learn about another student? Enter 'y' or 'n': ").lower()
    if keep_going == "y":
        continue
    else:
        print(f"Thank you for playing. Goodbye!")
        break


