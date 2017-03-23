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
POPULATION = 10 #1000
SURVIVORS = 1 #100 #10%
MUTATION_RATE = 0.05 #5%
FREQ_STATS = 10
GAMES = 1#100

# The step callback function, this function
# will be called every step (generation) of the GA evolution
def evolve_callback(ga_engine):
    generation = ga_engine.getCurrentGeneration()
    pop = ga.getPopulation()
    if generation == 0:
        popFR = open("population.txt", 'r')
        i = -1 # number of the individual
        #Initilize population
        for line in popFR:
            if i != -1 and i != POPULATION: #is not te generation information
                print "line" + line
                ind = line[1:-2].split(',')
                print ind
                for j in range(NUM_HEURISTIC):
                    pop[i].genomeList[j] = int(ind[j])
            i += 1
        popFR.close()
        ga.internalPop = pop

    if generation % 20 == 0:
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

# This function is the evaluation function
# (fitness function)
def fitness(chromosome):
    print "Genome: " + str(chromosome.genomeList)
    fitness = 0
    app = TetrisApp()
    app.genetic_toggle(GAMES)
    app.ai = AI(app, chromosome[0], chromosome[1], chromosome[2], chromosome[3])
    # app.ai = AI(app, -496, 897, -109, -910)
    app.ai.instant_play = True
    try:
        app.run()
    except Exception as e:
        print "fitness:" + str(e)
        fitness = e.args[0]
        return fitness

# Enable the pyevolve logging system
pyevolve.logEnable()

# Genome instance, 1D List of number of heuristic
genome = G1DList.G1DList(NUM_HEURISTIC)

# Sets the range max and min of the 1D List
genome.setParams(rangemin=-100, rangemax=100)

# The evaluator function (evaluation function)
genome.evaluator.set(fitness)
# genome.crossover.set(weightedCrossover)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)

# Set the Roulette Wheel selector method, the number of generations and
# the termination criteria
ga.selector.set(Selectors.GRouletteWheel)
ga.setElitism(True)
ga.setElitismReplacement(SURVIVORS)
ga.setGenerations(GENERATIONS)
ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
ga.setPopulationSize(POPULATION)
ga.setMutationRate(MUTATION_RATE)
ga.stepCallback.set(evolve_callback)

# Using CSV Adapter
csvfile_adapter = DBAdapters.DBFileCSV(frequency = FREQ_STATS)
ga.setDBAdapter(csvfile_adapter)

# Do the evolution, with stats dump
# frequency of 20 generations
ga.evolve(freq_stats = FREQ_STATS)

# Best individual
print ga.bestIndividual()
