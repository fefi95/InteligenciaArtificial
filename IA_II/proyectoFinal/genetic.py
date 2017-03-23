"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:

"""

from tetris import TetrisApp
from ai import AI
from random import randint as rand_randint
from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Statistics
from pyevolve import DBAdapters
import pyevolve

# Global variables/Settings
NUM_HEURISTIC = 4
GENERATIONS = 500
POPULATION = 500
SURVIVORS = 50 #10%
MUTATION_RATE = 0.05 #5%
FREQ_STATS = 5
GAMES_PER_INDIVIDUAL = 50
genomeInit = [] # Genomes stores in population file
n_ind = 0 # Number of the individual to be initialize

"""
    Description:
        Initialize every genome of the population using the
        genomeInit wich contains the genome of the individuals
        of previous executions
    Params:
        @param genome : the genome of an individual
        @param **args : aditional args
"""
def G1DListTetrisInitializator(genome, **args):
    genome.clearList()
    global n_ind
    genome.genomeList = genomeInit[n_ind]
    n_ind += 1

"""
    Description:
        Stores population information to a file so it can be used
        in another execution. This function is called every step
        (generation) of the GA evolution
    Params:
        @param ga_engine : the GA engine used for evolution
"""
def evolve_callback(ga_engine):
    generation = ga_engine.getCurrentGeneration()
    pop = ga.getPopulation()
    if generation % FREQ_STATS == 0:
        popF = open("population.txt", 'w')
        print "Current generation: %d" % (generation,)
        popF.write("Generacion: " + str(generation,) + "\n")
        for ind in pop:
            # Save population
            # popF.write(str(ind.getRawScore()) + "\n")
            # popF.write(str(ind.getFitnessScore()) + "\n")
            popF.write(str(ind.genomeList) + "\n")
        popF.write("Best:" + str(pop.bestFitness().genomeList) + "\n")
        popF.close()
    return False

"""
    Description:
        Calculates the fitness function by playing
        GAMES_PER_INDIVIDUAL games and gets the sum of the
        scores afeter finishing
    Params:
        @param chromosome : the individual of the population
"""
def fitness(chromosome):
    print "Genome: " + str(chromosome.genomeList)
    fitness = 0
    app = TetrisApp()
    app.genetic_toggle(GAMES_PER_INDIVIDUAL)
    app.ai = AI(app, chromosome[0], chromosome[1], chromosome[2], chromosome[3])
    # app.ai = AI(app, -496, 897, -109, -910)
    app.ai.instant_play = True
    try:
        app.run()
    except Exception as e:
        print "fitness:" + str(e)
        fitness = e.args[0]
        return fitness

"""
    The genetic algorithm
"""
# Enable the pyevolve logging system
pyevolve.logEnable()

# Genome instance, 1D List of number of heuristic
genome = G1DList.G1DList(NUM_HEURISTIC)

# Sets the range max and min of the 1D List
genome.setParams(rangemin=-100, rangemax=100)

# Try to read store data on population file
try:
    popFR = open("population.txt", 'r')
    i = -1 # number of the individual
    for line in popFR:
        if i != -1 and i != POPULATION: #is not te generation information
            # print "line" + line
            ind = line[1:-2].split(',')
            # print ind
            genomeInit.append([])
            for j in range(NUM_HEURISTIC):
                genomeInit[i].append(int(ind[j]))
        i += 1
    #Changing the default initializator
    genome.initializator.set(G1DListTetrisInitializator)

except Exception as e:
    print "Population file not found, using default initializator"

# The evaluator function (evaluation function)
genome.evaluator.set(fitness)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)

# Set the Roulette Wheel selector method
ga.selector.set(Selectors.GRouletteWheel)
# Set the population size and how many individuals survive
# for the next generation
ga.setPopulationSize(POPULATION)
ga.setElitism(True)
ga.setElitismReplacement(SURVIVORS)
ga.setGenerations(GENERATIONS)
# Set generation criteria
ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
# Set probability of mutation of an individual
ga.setMutationRate(MUTATION_RATE)
# Set function to be called after a generation
ga.stepCallback.set(evolve_callback)

# Using CSV Adapter
csvfile_adapter = DBAdapters.DBFileCSV(frequency = FREQ_STATS, reset = False)
ga.setDBAdapter(csvfile_adapter)

# Do the evolution, with stats dump
# frequency of 20 generations
ga.evolve(freq_stats = FREQ_STATS)

# Best individual
print ga.bestIndividual()
