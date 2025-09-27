# adjective1 = input('write your adjective 1:')
# adjective2 = input('write your adjective 2:')
# adjective3 = input('write your adjective 3:')
# noun1 = input('write your noun1:')
# noun2 = input('write your noun2:')
# noun3 = input('write your noun3:')
# verb = input('write your verb:')
# if adjective1 == adjective2 or adjective1 == adjective3 or adjective2 == adjective3:
#     print("Adjectives must be different")
# elif adjective1 == "" and adjective2 == "" and adjective3 == "":
#     print("Adjectives must be filled")

# else:
#     print("The " + noun1 + " " + adjective1 +
#           " likes to " + verb + " " + adjective2 + ".")

#     print("The " + noun2 + " is very " + adjective3 + ".")


# import random
# secret_number = random.randint(1, 10)
# play_again = "yes"
# guess = int(input("guess a number between 1 and 10: "))
# count_gesses = 1
# while play_again.lower() == "yes":
#     match guess:
#         case _ if guess == secret_number:
#             print("Congratulations, you guessed it!")
#             play_again = input("Do you want to play again? (yes/no): ")
#             if play_again.lower() == "yes":
#                 secret_number = random.randint(1, 10)
#                 guess = int(input("guess a number between 1 and 10: "))
#             else:
#                 print("Thank you for playing! Goodbye!")
#                 break
#         case _ if guess > secret_number:
#             print("Oops, your guess is a bit high. Try again!")
#             guess = int(input("guess a number between 1 and 10: "))
#         case _ if guess < secret_number:
#             print("Nope, your guess is a bit low. Give it another shot!")
#             guess = int(input("guess a number between 1 and 10: "))
#             count_gesses += 1
# print(f"You made {count_gesses} guesses.")

# Exercice 2 For loop
# numbers = [1, 5, 3, 9]
# total = 0
# for number in numbers:
#     total += number
# print(f"the total is {total}")

# # While loops exercice
# # i = 1
# # while i <= 5:
# #     print("Telusko", end=" ")
# #     j = 1
# #     while j <= 4:
# #         print("rocks", end=" ")
# #         j = j + 1

# #     i = i + 1
# #     print()

# Exercice 3 while loop

shoping_list = ["apple", "banana", "orange", "grape"]
item_found = False

while not item_found:
    item = input("Search for an item in your list (or 'q' to quit): ")
    if item.lower() == "q":
        break  # Exit the loop if user enters 'q'

    if item_found in shoping_list:
        item_found = True
        print(f"{item} is in your shopping list!")
    else:
        print(f"{item} is not in your shopping list.")
