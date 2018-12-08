from TSPClasses import *
from AntColony import *

class ACSolver(object):

    def __init__(self, scenario):
        pass

    def solve(self, scenario, time_allowance = 60):
        cityAmount = len(scenario.getCities())
        cities = scenario.getCities()
        cityMatrix = np.zeros((cityAmount, cityAmount),float, 'C')
        antNum = 10;
        antArray = [];
        bssf = None;
        start_time = time.time()
        currrent_time = time.time()
        while currrent_time - start_time < time_allowance :
            for i in range(antNum):
                antArray.append(Ant(cities,cityMatrix))

            for i in range(antNum):
                antTourMatrixTuple = antArray[i].generate_tour()
                tour = antTourMatrixTuple[0]
                matrix = antTourMatrixTuple[1]
                # Add matrix to each time
                cityMatrix += matrix
                solution = TSPSolution(tour)
                cost = solution.cost
                if bssf == None:
                    bssf = solution
                elif bssf.cost > cost:
                    bssf = solution
            
            currrent_time = time.time()

        return bssf



