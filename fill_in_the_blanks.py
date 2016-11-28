#encoding=utf-8
#
#
# 	Grey Grissom
# 	November 25, 2016
# 	Create Your Own Quiz
# 	Stage 2 - ND Program

def getDifficulty():
	# Prompts user / reviewer to choose difficulty level , returns their choice
	print "Choose your difficulty:\nEASY\t|\tMODERATE\t|\tHARD\t"
	difficulty = raw_input().lower()
	return difficulty

def easySpaces():
	# Quiz for easy spaces
	question = "On November 8, 2016, Donald ____1____ stunned millions of people worldwide when he won the Presidential election. His opponent ____2____ Clinton could not deliver her concession speech as intended due to the shock of the outcome. The ____3____ Party, devastated and in shambles, found itself without a future, leader, purpose. Despite protests, Clinton did ____4____ to him the following day. Despite losing the electoral college vote, she did win the ____5____ vote."

	user_responses = ["", "", "", "", ""]
	correct_responses = ["trump", "hillary", "democratic", "concede", "popular"]
	confirm_responses(question, user_responses, correct_responses)

def moderateSpaces():
	# Quiz with slightly more difficult answers
	question = "____1____ loops are ideal for repeating a procedure until some expression proves untrue. ____2____ is the result of not finding a particular substring from a string. With the expression (True or False) ____3____ = 1 if True, 0 if False. If, ____4____, and else work hand-in-hand to control flow in some circumstances. ____5____ loops are great to iterate over a body of items."
	user_responses = ["", "", "", "", ""]
	correct_responses = ["while", "-1", "1", "elif", "for"]
	confirm_responses(question, user_responses, correct_responses)

def hardSpaces():
	# Most challenging quiz yet
	question = "____1____ lie between a function's parenthesis in a function declaration. When actually invoked, the parameters become ____2____. Always remember that lines of code following a function's ____3_____ statement are ignored and will not be processsed. Often times, it is helpful to use multiple ____4____ statements throughout functions when debugging -- they output relevant code when needed. All ____5____ definitions begin with the keyword def "
	user_responses = ["", "", "", "", ""]
	correct_responses = ["parameters", "arguments", "return", "print", "function"]
	confirm_responses(question, user_responses, correct_responses)

def confirm_responses(question, user_responses, correct_responses):
	# Prints one q at a time. Prompt user fill in blank
	spaces = ['____1____','____2____','____3____','____4____','____5____']
	index = 0
	print question, "\n"
	question = question.split(". ")
	for line in question:
		print line
		while user_responses[index].lower() != correct_responses[index]:
			user_responses[index] = raw_input("Fill in blanks:")
			if user_responses[index].lower() != correct_responses[index]:
				print ":( Wrong! Try again!"
				print line + "\n"
		print ":) Correcto!"
		print line.replace(spaces[index], correct_responses[index]), "\n"
		index += 1

	print "Game End!"

def fillSpaces(difficulty):
	if difficulty == "easy":
		easySpaces()
	elif difficulty == "moderate":
		moderateSpaces()
	elif difficulty == "hard":
		hardSpaces()

#initializes game
fillSpaces(getDifficulty())