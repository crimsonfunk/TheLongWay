import time # used for realtime waiting periods
import sys # used for letter-by-letter typeouts

def spinningIcon(): # "loading up" symbol
	print('')
	for x in range(12):
		print('/', end = '\r')
		time.sleep(.1)
		print('-', end = '\r')
		time.sleep(.1)
		print('\\', end = '\r')
		time.sleep(.1)
	for x in '/-\\':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(.5)
	time.sleep(1)
	print('')

def waitingDots(): # Use for sleep/day cycle?
	for s in range(3):
		print('.' + ('.' * s))
		time.sleep(1)
	time.sleep(1)

def typeOut(phrase, s): # s is the number of seconds waited per character
	for char in phrase:	
		sys.stdout.write(char)
		if char == '.' or char =='?':
			time.sleep(1)
		sys.stdout.flush()
		time.sleep(s)
	time.sleep(1.5)
	print('')

scene1 = '''You are surrounded by steel walls, a dreary grey, in a dimly-lit room. You can make out metal panels of different shapes and sizes, bolted securely, covering every face of the room. There is a single light source above you in the center of the room.

(1) Search the room?
(2) Yell for help?
(3) Sit and wait?'''
scene2 = '''You awaken again, now to a well-lit room. You can now see an open vent - high on one of the walls. A new source of light peeks past one of the panels on the wall. And the floor grate has been left wide open..

You find a worn note on the floor. It reads, “Every man for themselves.” Someone’s been here..

(1) Go through the grate opening?
(2) Pry the panel open?
(3) Climb into the vent?
'''
scene3a = '''The further you go, the clearer you can hear voices above you. You stop in a passage under floor grates; above appears to be a command room. 
				
				(1) Move on and search for an exit?
				(2) Stay and listen to the conversation?'''
scene3b = '''The further you go, the clearer you can hear voices ahead of you. You stand out into a large room. Before you stands a command room.
				
				(1) Move on and search for an exit?
				(2) Stay and listen to the conversation?'''
scene3c = '''The further you go, the clearer you can hear voices below you. You stop in a duct. Peering down, below you appears to be a command room.
				
				(1) Stay and listen to the conversation?
				(2) Move on and search for an exit?'''
scenes3 = ''
sceneList = scene1, scene2, scenes3

def titleCard():
	title = '''THE
    LONG
         WAY'''
	typeOut(title, 0.15)
	time.sleep(1.5)
	print('')
	print('Press Enter to Start.', end ='')
	input()

def displayIntro(): # returns player name
	time.sleep(3)
	print('\nWhat is your name?')
	playerName = input()
	waitingDots()

	time.sleep(2)
	intro = '''You awaken from a deep sleep. A burst of warm air blows through you.  Your head and left hand lay atop a metal grate, emanating warmth. You feel cold metal against your right side, and slowly sit up to find your bearings...'''
	typeOut((playerName + ','), 0.8)
	typeOut(('\n' + intro), 0.08)

	return playerName

def setScene(scene):
	spinningIcon()
	typeOut((scene), 0.1)

def pickOption(): # returns choice
	choice = ''
	print()
	print('\n' + 'Enter your choice.')
	choice = input()
	while choice != '1' and choice != '2' and choice != '3':
		print('That is not a valid option. Try a number.')
		choice = input()

	return choice

def checkOption(chosenOption):
	passCount = '0'
	waitingDots()
	if chosenOption == '1': # good
		passCount = 1
	if chosenOption == '2': # bad
		passCount = 2
	if chosenOption == '3': # neutral
		passCount = 3
	time.sleep(2)
	print()
	return passCount

def endGame(playerName, rightOrWrong):
	waitingDots()
	typeOut('Before you know it, your captors are made of your presence. You take off immediately, into a long, long tunnel, and--', 0.1)
	spinningIcon()

	if rightOrWrong.count('O') > 1:
		typeOut(('You escape! Congratulations!'), 0.1)
	if rightOrWrong.count('X') > 1:
		typeOut('You are swiftly caught.. and promptly returned to the room.', 0.1)
	else:
		typeOut('You run and run, unknowningly deeper into the facilities. There is no way out.', 0.1)
		time.sleep(1)
		typeOut('Anymore.', 0.1)

	print("It is the end of your journey, " + playerName + '.')
	time.sleep(2)
	print('Let\'s see how you did...')
	time.sleep(3)
	print()
	typeOut((rightOrWrong + '\n'), 1)
	print('(O\'s are good choices, X\'s are bad, -\'s are neutral)') 


restart = 'yes'
while restart == 'yes' or restart == 'y':
	choices = ''
	titleCard()
	playerName = displayIntro()
	passCount = ''

	for scene in sceneList:

		if scene == scenes3:
			if passCount == 1:
				scene = scene3a
			if passCount == 2:
				scene = scene3b
			if passCount == 3:
				scene = scene3c

		setScene(scene) # produce scene description
		optionNumber = pickOption() # request choice input
		passCount = checkOption(optionNumber) # equate choice to path
		if scene == scene1:
			passCount = 0
			typeOut('Your actions change nothing. The room is devoid of any loose objects or potential tools. There are no other sounds but your own. Time goes by. There’s nothing left to do... but sleep...', 0.1)
			waitingDots()

		if scene == scene3a:
			if passCount == 2:
				passCount = 3
		if scene == scene3c:
			if passCount == 1:
				passCount = 3

		if passCount == 1:
			choices += 'O '
		if passCount == 2:
			choices += 'X '
		if passCount == 3:
			choices += '- '

	endGame(playerName, choices)
	
	print ('''\nDo you want to play again?''')
	restart = input()
	if restart != 'yes' and restart != 'y':
		typeOut('Thanks for playing!', 0.1)
