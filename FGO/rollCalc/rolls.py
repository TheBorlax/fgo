'''
Created on Jun 7, 2018

@author: TheBorlax
'''
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class Core:
    def __init__(self):
        return 0
    
    def minChance(self, rolls, probability = 0.007):
        return (1 - pow((1 - probability), rolls))
    
    def distribute(self, rolls, probability = 0.007):
        distribution = {}
        for index in range(rolls + 1):
            coeff = math.factorial(rolls) / (math.factorial(index) * math.factorial(rolls - index))
            distribution[index] = coeff * pow(probability, index) * pow(1 - probability, rolls - index)
        return distribution
    
    def distributeBuiltIn(self, rolls, probability = 0.007, minCount = 1, showGraph = True):
        distribution = {}
        range = np.arange(0, 101)
        binomial = stats.binom.pmf(range, rolls, probability)
        sumArray = binomial[minCount:len(binomial)]
        print(np.sum(sumArray))
        if (showGraph):
            plt.plot(range, binomial, 'o-')
            plt.title('Binomial: rolls: %i, probability: %.3f' % (rolls, probability), fontsize = 15)
            plt.xlabel('Number of Successes')
            plt.ylabel('Probability of Successes')
            plt.show()
     
def main():
    core = Core
    core.distributeBuiltIn(core, 128, 0.015, 5, False)
    
if __name__ == "__main__":
    main()