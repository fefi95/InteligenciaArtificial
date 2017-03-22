from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Statistics
from pyevolve import DBAdapters
import pyevolve

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
            if i != -1: #is not te generation information
                print line
                # PARSEAR LINEA Y CAMBIAR EL INDIVIDUO
                # pop[i].genomeList = ?
            i += 1
        popFR.close()

    if generation % 20 == 0:
        popF = open("population.txt", 'w')
        print "Current generation: %d" % (generation,)
        popF.write("Generacion: " + str(generation,) + "\n")
        for ind in pop:
            #Save population
            # popF.write(str(ind.getRawScore()) + "\n")
            # popF.write(str(ind.getFitnessScore()) + "\n")
            popF.write(str(ind.genomeList) + "\n")
        popF.close()
    return False

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
   score = 0.0

   # iterate over the chromosome
   # score = len(filter(lambda x: x==0, chromosome.genomeList))
   for value in chromosome:
      if value==0:
         score += 1

   return score

# Enable the pyevolve logging system
pyevolve.logEnable()

# Genome instance, 1D List of 50 elements
genome = G1DList.G1DList(50)

# Sets the range max and min of the 1D List
genome.setParams(rangemin=0, rangemax=10)

# The evaluator function (evaluation function)
genome.evaluator.set(eval_func)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)

# Set the Roulette Wheel selector method, the number of generations and
# the termination criteria
ga.selector.set(Selectors.GRouletteWheel)
ga.setGenerations(500)
ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
ga.setPopulationSize(80)
ga.stepCallback.set(evolve_callback)

# Using CSV Adapter
csvfile_adapter = DBAdapters.DBFileCSV(frequency = 10)
ga.setDBAdapter(csvfile_adapter)

# Do the evolution, with stats dump
# frequency of 20 generations
ga.evolve(freq_stats=20)

# Best individual
print ga.bestIndividual()
