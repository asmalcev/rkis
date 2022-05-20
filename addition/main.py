import math
import random

def int_to_bin(num, length = None):
	bin_num = bin(num).replace('0b', '')
	if length is not None:
		bin_num = '0' * (length - len(bin_num)) + bin_num
	return bin_num

def bin_to_int(num):
	return int(num, 2)


#
# INPUT DATA
#
def f(x):
	return -math.sin(0.9 * x - 1) - math.sin(1.8 * x - 1) * math.cos(7.8 * x)

population_size = 50
chromosome_length = 20
start_population_size = bin_to_int('1' * chromosome_length)

lower_border = -5
upper_border = 5

Pc = 0.8
Pm = 0.15

#
# GENERATE POPULATION
#
points_step = (upper_border - lower_border) / start_population_size
start_population = list(map(
	lambda x: int_to_bin(x, chromosome_length),
	range(0, start_population_size)
))

population = set()
while len(population) < population_size:
	population.add( start_population[random.randint(0, start_population_size - 1)] )

population = list(population)


#
# EVOLUTION PROCESS
#
def cross(a, b):
	divider = random.randint(1, len(a) - 2)
	return a[:divider] + b [divider:]


def mutate(a):
	locus = random.randint(0, len(a) - 1)
	a = a[:locus] + ('0' if a[locus] == '1' else '1') + a[locus + 1:]
	return a

def get_population_values(population):
	return list(map(
		lambda x: lower_border + points_step * bin_to_int(x),
		population
	))

def get_population_weights_from_population(population):
	return list(map(
		lambda x: f(lower_border + points_step * bin_to_int(x)),
		population
	))

def get_population_weights_from_values(population):
	return list(map(
		lambda x: f(x),
		population
	))

def roulette(weights, weights_sum):
	percentages = list(map(
		lambda x: x / weights_sum,
		weights
	))

	pick = random.random()

	percentages_sum = 0
	index = 0

	try:
		while percentages_sum < pick or index + 1 == len(percentages):
			percentages_sum += percentages[index]
			index += 1
	except:
		pass

	return index - 1


def run_evolution(population):
	#
	# CROSSING
	#
	population_indexes = list(
		range(0, len(population))
	)
	random.shuffle(population_indexes)

	next_generation = filter(lambda x: x, [
		(
			cross(
				population[population_indexes[i]],
				population[population_indexes[i + 1]],
			) if random.random() < Pc else None
		) for i in range(0, len(population), 2)
	])

	#
	# MUTATION
	#
	next_generation = list(map(
		lambda x: mutate(x) if random.random() < Pm else x,
		next_generation
	))

	#
	# REDUCTION
	#
	population += next_generation
	population_weights = get_population_weights_from_population(population)

	# improve values
	min_weight = min(population_weights)
	if min_weight < 0:
		min_weight = -min_weight

		population_weights = list(map(
			lambda x: x + min_weight,
			population_weights
		))

	weights_sum = sum(population_weights)

	next_population = []

	while len(next_population) < population_size:
		index = roulette(population_weights, weights_sum)

		next_population.append( population[index] )
		weights_sum -= population_weights[index]
		del population_weights[index]

	return next_population


def print_population_data(population, title=None):
	population_values = get_population_values(population)
	population_weights = get_population_weights_from_values(population_values)

	if title is not None:
		print(title)

	for i in range(len(population)):
		print('%2d %+f %s %+f %+f' % (
			i + 1,
			population_values[i],
			population[i],
			population_weights[i],
			population_weights[i]
		))

print_population_data(population, 'First')

should_print = True
for i in range(1000):
	population = run_evolution(population)

	if should_print:
		should_print = False
		print_population_data(population, 'Second')

print_population_data(population, 'Last')


population_values = get_population_values(population)
population_weights = get_population_weights_from_values(population_values)

max_weight = max(population_weights)
max_value = population_values[population_weights.index(max_weight)]

print('x =', max_value, 'y =', max_weight)