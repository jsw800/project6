from TSPClasses import *
from AntColony import *

EVAP_RATE = .1
NUM_PER_GENERATION = 40
GENERATION_BOUND = 80


def evaporate(phMatrix):
    phMatrix *= EVAP_RATE
    return phMatrix


class ACSolver(object):

    def __init__(self, scenario, time_allowance = 60):
        self.scenario = scenario
        self.time = time_allowance

    def solve(self):
        cityAmount = len(self.scenario.getCities())
        cities = self.scenario.getCities()
        # master pherm matrix
        pheromone_matrix = np.ones((cityAmount, cityAmount), dtype=float)
        dist_matrix = np.zeros([cityAmount, cityAmount], dtype=float)
        for i, city in enumerate(cities):
            for j, city2 in enumerate(cities):
                dist_matrix[i, j] = city.costTo(city2)
                if dist_matrix[i, j] == 0.0:
                    dist_matrix[i, j] = 0.1

        for i in range(len(cities)):
            pheromone_matrix[i, i] = 0
        ants = []
        bssf = None
        start_time = time.time()
        current_time = time.time()
        lastEdited = 0
        currentGeneration = 0

        while current_time - start_time < self.time and currentGeneration < lastEdited + GENERATION_BOUND:
            ants = [Ant(cities, pheromone_matrix, dist_matrix) for _ in range(NUM_PER_GENERATION)]
            pheromones_to_register = []
            for i in range(len(ants)):
                tour, matrix = ants[i].generate_tour()
                # Add matrix to each time
                pheromones_to_register.append(matrix)
                solution = TSPSolution(tour)
                cost = solution.cost
                if bssf is None or bssf.cost > cost:
                    bssf = solution
                    lastEdited = currentGeneration
                    print('updated bssf')

            for phMatrix in pheromones_to_register:
                pheromone_matrix += phMatrix
            
            currentGeneration += 1
            pheromone_matrix = evaporate(pheromone_matrix)
            current_time = time.time()
        print(currentGeneration)
        return bssf



