import itertools
import numpy as np
from .search_alg import Search
import time

ITERATION = 50

class BanditSearch(Search):
    ''' Bandit search algorithm
    
    :attribute _file_name: The name of the targeted file
    :attribute _need_compile: Whether the file need to be compiled
    :attribute _params: All possible parameters
    :attribute _best_params: The parameters performing the best
    :attribute _best_result: The best performance
    :attribute _combinations: The parameters combinations
    :attribute _counts: Sampled times of each configuration
    :attribute _values: The result of each configuration
    '''
    
    def __init__(self, file_name: str, need_compile: bool, params: dict) -> None:
        ''' Initialize the Grid Search
        
        :param file_name: The name of the targeted file
        :param need_compile: Whether the file need to be compiled
        :param params: All possible parameters (eg: {block_size: (2, 4, 8), gcc_flag: (O1, O2, O3)})
        :param best_params: The parameters performing the best
        :param best_result: The best performance
        '''
        super().__init__(file_name, need_compile, params)
        
        self._option_cnt = 0
        self._combinations = []
        for combination in itertools.product(self._params['o'], self._params['s']):
            current_params = {'o': combination[0], 's': combination[1]}
            self._combinations.append(current_params)
            self._option_cnt += 1
            
        self._counts = np.zeros(self._option_cnt)
        self._values = np.zeros(self._option_cnt)
        
        self._epsilon = 0.1
            
    def run(self):
        '''
        Execute the bandit search algorithm to get the best parameter configuration
        '''
        for _ in range(ITERATION):
            rand = np.random.rand(0, 1)
            if rand < self._epsilon:
                idx = np.random.randint(0, self._option_cnt)
            else:
                idx = np.argmax(self._values)
                
            current_params = self._combinations[idx]
            start_time = time.time()
            self._single_execution(current_params)
            end_time = time.time()
            duration = end_time - start_time
            
            self._counts[idx] += 1
            n = self._counts[idx]
            value = self._values[idx]
            self._values[idx] = value + (- duration - value) / n
        
        self._best_params = self._combinations[np.argmax(self._values)]
    
    def _single_execution(self, current_params: dict):
        '''
        Execute the program with one specific parameter configuration
        '''
        target_file_name = self._file_name
        super().get_and_execute_command(target_file_name, current_params)