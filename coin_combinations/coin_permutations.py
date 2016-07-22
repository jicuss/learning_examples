'''
given an infinite number of quarters, dimes, nickels, and pennies, find the number of possible ways to represent n cents
'''


import unittest
import pdb

def find_fewest_coin_combination(value,starting_array = [0,0,0,0],option_array = [1,1,1,1]):
    ''' the option_array is an array of boolean values. if set to 1, then that coin can be used '''
    quarters = starting_array[0]
    dimes = starting_array[1]
    nickels = starting_array[2]
    pennies = starting_array[3]

    remainder = value
    remainder -= quarters*0.25
    remainder -= dimes*0.10
    remainder -= nickels*0.05
    remainder -= pennies*0.01

    while True:
        if remainder > 0.25 and option_array[0] == 1:
            quarters += int(remainder/0.25)
            remainder -= quarters*0.25
        elif remainder > 0.10 and option_array[1] == 1:
            dimes += int(remainder/0.10)
            remainder -= dimes*0.10
        elif remainder > 0.05 and option_array[2] == 1:
            nickels += int(remainder/0.05)
            remainder -= nickels*0.05
        elif remainder > 0.01 and option_array[3] == 1:
            pennies += int(round(remainder/0.01))
            remainder -= pennies*0.01
        else:
            break

    return [quarters,dimes,nickels,pennies]


class Queue():
    def __init__(self,value):
        self.value = value
        self.queue = []
        self.possible_solutions = []
        self.first_element()
        self.queue_loop()

    def first_element(self):
        self.append_to_queue(find_fewest_coin_combination(self.value))

    def append_to_queue(self,array):
        self.queue.insert(0,array)

    def queue_loop(self):
        while len(self.queue) > 0:
            self.next_iteration()

    def next_iteration(self):
        current_combination = self.queue.pop()
        self.possible_solutions.append(current_combination)

        new_combination = list(current_combination)
        if new_combination[0] > 0:
            new_combination[0] -= 1
            self.append_to_queue(find_fewest_coin_combination(self.value,new_combination,[0,1,1,1]))
        elif new_combination[1] > 0:
            new_combination[1] -= 1
            self.append_to_queue(find_fewest_coin_combination(self.value,new_combination,[0,0,1,1]))
        elif new_combination[2] > 0:
            new_combination[2] -= 1
            self.append_to_queue(find_fewest_coin_combination(self.value,new_combination,[0,0,0,1]))
        else:
            print 'DONE!'

class CoinPermutationTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_fewest_coin_combination(self):
        self.assertEquals(find_fewest_coin_combination(2.05,[0,0,0,0],[1,1,1,1]),[8, 0, 0, 5])

    def test_find_all_combinations(self):
        q = Queue(0.10)
        self.assertEquals(q.possible_solutions,[[0, 0, 2, 0], [0, 0, 1, 5], [0, 0, 0, 10]])
        q = Queue(2.05)
        self.assertEquals(q.possible_solutions,[[8, 0, 0, 5], [7, 2, 0, 10], [6, 4, 0, 10], [5, 6, 0, 10], [4, 9, 0, 10], [3, 11, 0, 10], [2, 14, 0, 10], [1, 16, 0, 10], [0, 19, 0, 10], [0, 18, 2, 15], [0, 17, 3, 15], [0, 16, 5, 15], [0, 15, 7, 15], [0, 14, 9, 15], [0, 13, 11, 15], [0, 12, 13, 15], [0, 11, 15, 15], [0, 10, 17, 15], [0, 9, 19, 15], [0, 8, 21, 15], [0, 7, 23, 15], [0, 6, 25, 15], [0, 5, 27, 15], [0, 4, 29, 15], [0, 3, 31, 15], [0, 2, 33, 15], [0, 1, 35, 15], [0, 0, 37, 15], [0, 0, 36, 25], [0, 0, 35, 30], [0, 0, 34, 35], [0, 0, 33, 40], [0, 0, 32, 45], [0, 0, 31, 50], [0, 0, 30, 55], [0, 0, 29, 60], [0, 0, 28, 65], [0, 0, 27, 70], [0, 0, 26, 75], [0, 0, 25, 80], [0, 0, 24, 85], [0, 0, 23, 90], [0, 0, 22, 95], [0, 0, 21, 100], [0, 0, 20, 105], [0, 0, 19, 110], [0, 0, 18, 115], [0, 0, 17, 120], [0, 0, 16, 125], [0, 0, 15, 130], [0, 0, 14, 135], [0, 0, 13, 140], [0, 0, 12, 145], [0, 0, 11, 150], [0, 0, 10, 155], [0, 0, 9, 160], [0, 0, 8, 165], [0, 0, 7, 170], [0, 0, 6, 175], [0, 0, 5, 180], [0, 0, 4, 185], [0, 0, 3, 190], [0, 0, 2, 195], [0, 0, 1, 200], [0, 0, 0, 205]])

if __name__ == '__main__':
    unittest.main()