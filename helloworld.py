import string
import random
import time

char_set = string.ascii_uppercase + string.ascii_lowercase + ' '

def generate_organism(size):
	organism = []
	for i in range(size):
		organism.append(char_set[random.randint(0, len(char_set) - 1)])

	return organism
	
	
def mutate(organism_in, size):
	organism = organism_in[:]
	number_mutations = int(random.randint(1, size-1))
	
	for i in range(number_mutations):
		organism[random.randint(0, size-1)] = char_set[random.randint(0, len(char_set)-1)]
		
	return organism
	
def fitness(organism, target):
	score = 0
	for i in range(len(target)):
		if organism[i] == target[i]:
			score += 1
		
	return score

if __name__ == '__main__':
	target = list("hello world this is the best thing ever")
	print(target)
	target_len = len(target)
	organisms = [generate_organism(target_len) for i in range(100)]
	
	#print(organisms)
	
	best_fit_score = 0
	best = []
	
	generations = 0
	
	while best != target:
	
		for i in range(len(organisms)):
			if fitness(organisms[i], target) > best_fit_score:
				best_fit_score = fitness(organisms[i], target)
				best = organisms[i]
		
		for i in range(len(organisms)):
			organisms[i] = mutate(best, target_len)		
		
		
		generations += 1
		print(best)
		print(best_fit_score)
		print(generations)
		
		
	print(''.join(best))
		
