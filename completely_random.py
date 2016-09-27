import string
import random
import time

char_set = string.ascii_uppercase + string.ascii_lowercase + ' '


target = list('hello')

def make_random_word(size):
	word = [char_set[random.randint(0, len(char_set) - 1)] for i in range(size)]
	return word
	

random_word = make_random_word(len(target))

attempts = 0
while random_word != target:
	attempts += 1
	random_word = make_random_word(len(target))
	print(random_word)
	print(attempts)
	
print("done it took {} attempts to guess {}".format(attempts, target))
	

	
