from TSPClasses import *
from AntColony import *


class ACSolver(object):

    def __init__(self, scenario, time_allowance = 60):
        self.scenario = scenario
        self.time = time_allowance

    def solve(self):
        cityAmount = len(self.scenario.getCities())
        cities = self.scenario.getCities()
        # master pherm matrix
        cityMatrix = np.ones((cityAmount, cityAmount), float, 'C')
        for i in range(len(cities)):
            cityMatrix[i, i] = 0
        antNum = 10
        antArray = []
        bssf = None
        start_time = time.time()
        currrent_time = time.time()
        generationBound = 10
        currentGeneration = 0

        while currrent_time - start_time < self.time:
            antArray = []
            for i in range(antNum):
                antArray.append(Ant(cities, cityMatrix))

            pheromones_to_register = []
            for i in range(antNum):
                tour, matrix = antArray[i].generate_tour()
                # Add matrix to each time
                pheromones_to_register.append(matrix)
                solution = TSPSolution(tour)
                cost = solution.cost
                if bssf == None:
                    bssf = solution
                elif bssf.cost > cost:
                    bssf = solution

            for phMatrix in pheromones_to_register:
                cityMatrix += phMatrix
            
            currentGeneration += 1
            currrent_time = time.time()
        print(currentGeneration)
        return bssf



