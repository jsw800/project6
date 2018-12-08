import numpy as np
import copy
import random


class Ant(object):

    def __init__(self, cities, master_pheromone_matrix):
        self.cities = copy.deepcopy(cities)
        self.master_pheromones = master_pheromone_matrix
        self.tour = [self.cities.pop(random.randint(0, len(self.cities) - 1))]
        self.pherms_to_add = np.zeros(master_pheromone_matrix.shape, dtype=float)
        self.num_pheromones = 50.0

    def generate_tour(self):
        while len(self.cities) > 0:
            


