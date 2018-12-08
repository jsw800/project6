import numpy as np
import copy
import random
from TSPClasses import *


def choose_index(probs):
    total_prob = sum(probs)
    choice = random.uniform(0.0, total_prob)
    vals = [sum(probs[:i]) for i in range(1, len(probs) + 1)]
    for i in range(len(vals)):
        if choice < vals[i]:
            return i


class Ant(object):

    def __init__(self, cities, master_pheromone_matrix):
        self.cities = copy.deepcopy(cities)
        self.master_pheromones = master_pheromone_matrix
        self.tour = [self.cities.pop(random.randint(0, len(self.cities) - 1))]
        self.pherms_to_add = np.zeros(master_pheromone_matrix.shape, dtype=float)
        self.num_pheromones = 50.0

    def generate_tour(self):
        while len(self.cities) > 0:
            probs = [self.master_pheromones[self.tour[-1]._index, city._index] for city in self.cities]
            idx_to_add = choose_index(probs)
            self.tour.append(self.cities.pop(idx_to_add))
        total_cost = TSPSolution(self.tour).cost
        for i in range(len(self.tour) - 1):
            this_one = self.tour[i]
            next_one = self.tour[i + 1]
            cost = this_one.costTo(next_one)
            ratio = cost / total_cost
            pheromones_to_alloc = self.num_pheromones * ratio
            self.num_pheromones -= pheromones_to_alloc
            self.pherms_to_add[this_one._index, next_one._index] = pheromones_to_alloc
        return self.tour, self.pherms_to_add
