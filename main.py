import random as rand
num_of_Elite_chromose=1
POPULATION_SIZE=10
TournmentSize=4
Mutation_rate=0.25
TARGET_CHROMOSOME=[1,1,0,1,0,0,1,1,1,0]
class Chromose:
    def __init__(self):
        self.genes=[]
        self.fitness=0
        i=0
        while i<TARGET_CHROMOSOME.__len__():
            if rand.random()>=0.5:
                self.genes.append(1)
            else:
                self.genes.append(0)
            i+=1
    def get_genes(self):
        return self.genes
    def get_fitness(self):
        self.fitness=0
        for i in range(self.genes.__len__()):
            if self.genes[i]==TARGET_CHROMOSOME[i]:
                self.fitness+=1
        return self.fitness
    def __str__(self):
        return self.genes.__str__()
class Population:
    def __init__(self,size):
        self._chromosomes=[]
        i=0
        while i<size:
            self._chromosomes.append(Chromose())
            i+=1
    def getChromose(self):
        return self._chromosomes
class Genetic:
    @staticmethod
    def evolve(pop):
        return Genetic.mutate(Genetic.crossover(pop))
    @staticmethod
    def crossover(pop):
        crossover_pop=Population(0)
        for i in range(num_of_Elite_chromose):
            crossover_pop.getChromose().append(pop.getChromose()[i])
        i=num_of_Elite_chromose
        while i<POPULATION_SIZE:
            ch1=Genetic.select_tournment(pop).getChromose()[0]
            ch2=Genetic.select_tournment(pop).getChromose()[0]
            crossover_pop.getChromose().append(Genetic.crossover_chromosome(ch1,ch2))
            i+=1
        return crossover_pop
    @staticmethod
    def mutate(pop):
        for i in range(num_of_Elite_chromose,POPULATION_SIZE):
            Genetic.mutate_chromosome(pop.getChromose()[i])
        return pop
    @staticmethod
    def crossover_chromosome(ch1,ch2):
        ch=Chromose()
        for i in range(TARGET_CHROMOSOME.__len__()):
            if rand.random()>=Mutation_rate:
                if rand.random()<0.5:
                    ch.get_genes()[i]=ch1.get_genes()[i]
                else:
                    ch.get_genes()[i]=ch2.get_genes()[i]
       
        return ch
    @staticmethod
    def mutate_chromosome(chromosome):
        for i in range(TARGET_CHROMOSOME.__len__()):
            if rand.random()<Mutation_rate:
                chromosome.get_genes()[i]=1
            else:
                chromosome.get_genes()[i]=0
        return chromosome
    @staticmethod
    def select_tournment(pop):
        tourpop=Population(0)
        i=0
        while i<TournmentSize:
            tourpop.getChromose().append(pop.getChromose()[rand.randrange(0,POPULATION_SIZE)])
            tourpop.getChromose().sort(key=lambda x: x.get_fitness(),reverse=True)
            i+=1
        return tourpop  
def _print_population(pop,gen_number):
        print("\n------------------------------------------------")
        print("Generation #",gen_number,"| Fittest Chromosome fitness",pop.getChromose()[0].get_fitness())
        print("Target Chromosome",TARGET_CHROMOSOME)
        print("===================================================")
        i=0
        for x in pop.getChromose():
            print("Chromosome #",i,"  :",x,"|Fittness",x.get_fitness())
            i+=1
population=Population(POPULATION_SIZE)
population.getChromose().sort(key=lambda x: x.get_fitness(),reverse=True)
_print_population(population,0)
generation_number=1
while population.getChromose()[0].get_fitness()<TARGET_CHROMOSOME.__len__():
    population=Genetic.evolve(population)
    population.getChromose().sort(key=lambda x: x.get_fitness(),reverse=True)
    _print_population(population,generation_number)
    