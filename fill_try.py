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
flowed down countless supporters' faces, HRC did indeed ____4____ to Donald Trump
on the following day. As days passed, her supporters held onto the fact
that she may have lost the electoral vote, but she won the ____5____ vote by
more than 2 million votes.
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
easy_tuple = ( easy_quiz, easy_answers )
moderate_tuple = ( moderate_quiz, moderate_answers )
hard_tuple = ( hard_quiz, hard_answers )
# ----------------------------

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
	print difficulty_input
	difficulty_input = validation_helper(difficulty_input)
	return difficulty_input

def validation_helper(difficulty_input):
	"""
	simple helper function that takes the user's difficulty selection
	and pushes the matching quiz into the
	validate_responses function
	"""
	quiz_tuple = ()
	if difficulty_input == "easy":
		quiz_tuple = easy_tuple
	elif difficulty_input == "moderate":
		quiz_tuple = moderate_tuple
	elif difficulty_input == "hard":
		quiz_tuple = hard_tuple
	quiz_tuple = validate_responses(quiz_tuple)
	return quiz_tuple

def validate_responses(quiz_tuple):
	'''
	index = 0
	print quiz_tuple[0] + "\n"
	current_answer = raw_input(">>>  ").lower()
	while index < 5:
		while current_answer not in quiz_tuple[1]:
			print "try again\n"
			print quiz_tuple[0]
			current_answer = raw_input(">>>")
		if current_answer == quiz_tuple[1][index]:

			print "Correct!"
			print quiz_tuple[0].replace(spaces[index], quiz_tuple[1][index])
			quiz_tuple[0] = quiz_tuple[0].split(". ")
			for line in quiz_tuple[0]:
				print line
			#index += 1

			index += 1
			current_answer = raw_input(">>>  ").lower()

	'''

	spaces = [ '____1____', '____2____', '____3____', '____4____', '____5____']
	for item in spaces:
		current_answer = ''
		print quiz_tuple[0], "\n"
		current_answer = raw_input(">>> ")
		while current_answer.lower() != quiz_tuple[1][index]:
			try:
				current_answer = raw_input(">>> ")
				if current_answer.lower() != quiz_tuple[1][index]:
					print "WRONG! TRY AGAIN!", "\n"
					#print quiz_tuple[0], "\n"
					print quiz_tuple[0] + "\n"
			except IndexError:
				pass
		print ":) Correct!" + "\n"
		print quiz_tuple[0].replace(spaces[index], current_answer), "\n"
		index += 1


	print "Congrats! You Made it!  Game End!"

#validation
validate_responses(validation_helper(getDifficulty()))

