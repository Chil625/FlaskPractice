# should_continue = True
# if should_continue == True:
#     print("Hello")
#
# people_we_know = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in people_we_know:
#     print("You  know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))


def who_do_you_know():
    people_str = input("Let me know names you know, separated by a comma: ")
    people_you_know = people_str.split(",")
    # people_you_know_without_space = []
    # for person in people_you_know:
    #     people_you_know_without_space.append(person.strip())
    people_you_know_without_space = [person.strip() for person in people_you_know]
    return people_you_know_without_space


def ask_user(known_people):
    person = input("Enter the person you know: ")
    if person in known_people:
        print("You know {}!".format(person))
    else:
        print("You don't know {}...".format(person))


# print(who_do_you_know())
known_people = who_do_you_know()
print(known_people)
ask_user(known_people)
