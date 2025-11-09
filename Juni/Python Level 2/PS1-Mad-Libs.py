"""
Create your own mad lib by asking the user for any number of nouns, adjectives, verbs, or other types of words. Ask for at least five words. Then, print the mad lib with these words filled in!
"""

adjective = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
verb2 = input("Enter another verb, in past tense: ")

print(
	'The cafeteria at our school is very ' + adjective + '. For example, they serve ' + adjective2 + ' pizza. They also serve ' + noun + '. One time, I saw somebody ' + verb + ' across the cafeteria. Everybody ' + verb2 + '!')
