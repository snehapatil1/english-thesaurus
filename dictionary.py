import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_meaning(word):
	if word in data:
		return data[word]
	elif word.capitalize() in data:
		return data[word.capitalize()]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		possible_words = get_close_matches(word, data.keys())
		yn = (input(f"Did you mean {possible_words[0]} ? If Yes the type Y else type N.  ")).lower()
		if yn == 'y':
			return data[possible_words[0]]
		elif yn == 'n':
			return f"Word {word} does not exist in the dictionary, please recheck the word and enter again."
		else:
			return f'Input {yn} is incorrect, kindly retry.'
	else:
		print(f"Word {word} does not exist in the dictionary, please recheck the word and enter again.")
		main()

def main():
	word = (input('Enter word:  ')).lower()
	meaning = get_meaning(word)
	if isinstance(meaning, str):
		print(meaning)
	if isinstance(meaning, list):
		print(f"Meaning: {meaning[0]}")

main()