answer1 = "Yes"
answer2 = "yes"
answer3 = "No"
answer4 = "no"
answer5 = "Maybe"
answer6 = "maybe"
print("I need help. I forgot to do my english homework."" I had to write a paragraph about a food.")
print("Will you help me?")
answer = input("Yes or No?: ")
if answer == answer1:# and answer2:
	print("Thank you!")
elif answer == answer2:
	print("Thank You")
elif answer == answer3:# and answer4:
	print("Too bad you're helping me anyway.")
elif answer == answer4:
	print("Too bad you're helping me anyway.")
elif answer == answer5:# and answer6:
	print("Make a decision")
	print("I'll decide for you, you'll help me.")
elif answer == answer6:
	print("Make a decision")
	print("I'll decide for you, you'll help me.")
else:
	print("That's not an option, but eh you can help")
print("I'm gonna ask you a few questions to help me put it together.")
print("Remember to use correct capitalization.")
food = input("Pick a food to write about: ")
adj = input("Pick an adjective to describe that food: ")
wkday = input("Pick a day of the week: ")
ing = input("What is your favorite ingredient in " + food + "?: ")
print("Here's the final draft of the paragraph")
print("The food I chose to write about is " + food + ".")
print(food + " is " + adj + ". I like to eat it every " + wkday + "!")
print("My favorite ingredient is " + ing + ".")
print("That's why " + food + " is my favorite food!")