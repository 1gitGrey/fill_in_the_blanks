#encoding=utf-8
# Grey Grissom
# Create Your Own Quiz -- Stage 2 -- NDP

# Global Scope Variables for Quiz:


spaces = ['____1____','____2____','____3____','____4____','____5____']
#----------------------------
easy_quiz = '''
On November 8, 2016, Donald ____1____ stunned millions of people both
worldwide and abroad as he won this year's consequential Presidential election.
His opponent ____2____ Clinton, in disbelief and presumably deep grief, refused
to deliver a same-day concession speech as was suspected of the losing side.
The ____3____ Party, devastated and in shambless, found itself exactly where
they saw the Republicans to be-- futureless, leaderless, visionless. As tears
flowed down countless supporters, HRC did indeed ____4____ to Donald J. Trump
on the following day. As days passed, her supporters hold onto the fact
that she may have lost the electoral vote, but she won the ____5____ vote by
more than 2 million votes!
'''
moderate_quiz = '''
____1____ loops are ideal for repeating a procedure until
some expression proves untrue.
____2____ is the result of not finding a particular substring from a string.
       (Using the Find method we learned in this stage)
____3____ Flow is term used to describe the set of rules and guidelines
a programmer may utilize to build robust applications.
If, ____4____, and else work hand-in-hand to control flow in some circumstances.
____5____ loops are great to iterate over a body of items.
'''
hard_quiz = '''
____1____ lie between a function's parenthesis in a function declaration.
When functions are actually invoked, the parameters are called ____2____.
Always remember that lines of code following a function's ____3_____ statement
are ignored and will not be processsed. Often times, it is helpful
to use multiple ____4____ statements throughout functions
when debugging -- they output relevant code when needed.
All ____5____ definitions begin with the keyword def.
'''
#----------------------------

easy_answers = ['trump', 'hillary', 'democratic', 'concede', 'popular']
moderate_answers = ['while', '-1', 'control', 'elif', 'for']
hard_answers = ['parameters', 'arguments', 'return', 'print', 'function']

# ---------------------------
valid_difficulty_options = ['easy', 'moderate', 'hard', 'help']








def getDifficulty():
	"""
	Prompts user with three quiz difficulty options
	The program will repeat prompting for a valid
	Non-null response
	"""
	print "Choose quiz difficulty >>> easy | moderate | hard \n"
	difficulty_input = raw_input(">>>\t").lower()
	while difficulty_input not in valid_difficulty_options:
		difficulty_input = raw_input(">>>\t").lower()
	return difficulty_input

def validation_helper_data(difficulty_input):
	"""
	simple helper function that takes the user's difficulty selection
	and pushes the matching quiz_data into the
	validate_responses function
	"""
	quiz_data = ''
	if difficulty_input == "easy":
		quiz_data = easy_quiz
	elif difficulty_input == "moderate":
		quiz_data = moderate_quiz
	elif difficulty_input == "hard":
		quiz_data = hard_quiz
	return quiz_data

def validation_helper_answers(validation_helper_data):
	"""
	simple helper function input: difficulty_input
	output: quiz_answers sent to validate_responses function
	"""
	quiz_answers = []
	if quiz_data == easy_quiz:
		quiz_answers = easy_answers
	elif quiz_data == moderate_quiz:
		quiz_answers = moderate_answers
	elif quiz_data == hard_quiz:
		quiz_answers = hard_answers
	return quiz_answers

def validate_responses(validation_helper_answers):
	'''
	'''
	index = 0
	print nonlocal quiz_data + ("\n" * 3)
	current_answer = raw_input("____1____ = ? >>>\t").lower()
	while index < 5:
		while current_answer != quiz_answers[index]:
			print "\n" + nonlocal quiz_data + "\n"
			current_answer = raw_input(">>>").lower()
		if current_answer == quiz_answers[index]:
			print nonlocal quiz_data.replace(spaces[index], quiz_answers[index])
			index += 1



	'''for item in quiz_answers:
		if current_answer.lower() == item:
			print quiz_data.replace(spaces[index], item)
			index += 1
		while current_answer.lower() != item:
			print quiz_data
			current_answer = raw_input("Try Again :) >>>\t")
'''
	print "Congrats! You Made it!  Game End!"

validate_responses(validation_helper_answers(validation_helper_data(getDifficulty())))