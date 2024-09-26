import itertools
import os
from .search_alg import Search
import time

class GridSearch(Search):
    ''' Grid search algorithm
    
    @attribute _file_name: The name of the targeted file
    @attribute _need_compile: Whether the file need to be compiled
    @attribute _params: All possible parameters
    @attribute _best_params: The parameters performing the best
    @attribute _best_result: The best performance
    '''
    
    def __init__(self, file_name: str, need_compile: bool, params: dict) -> None:
        ''' Initialize the Grid Search
        
        @param file_name: The name of the targeted file
        @param need_compile: Whether the file need to be compiled
        @param params: All possible parameters (eg: {block_size: (2, 4, 8), gcc_flag: (O1, O2, O3)})
        @param best_params: The parameters performing the best
        @param best_result: The best performance
        '''
        super().__init__(file_name, need_compile, params)
        
    def run(self):
        for combination in itertools.product(self._params['o'], self._params['s']):
            current_params = {'o': combination[0], 's': combination[1]}
            start_time = time.time()
            self._single_execution(current_params)
            end_time = time.time()
            duration = end_time - start_time
            if duration < self._best_result:
                self._best_params = current_params
                self._best_result = duration
    
    def _single_execution(self, current_params: dict):
        target_file_name = self._file_name
        if self._need_compile:
            gcc_cmd = 'gcc -'
            gcc_cmd += current_params['o']
            gcc_cmd += ' '
            gcc_cmd += self._file_name
            gcc_cmd += ' -o '
            target_file_name = self._file_name[: -2]
            gcc_cmd += target_file_name
            os.system(gcc_cmd)
            
        gcc_cmd = target_file_name
        gcc_cmd += ' '
        gcc_cmd += current_params['s']
        os.system(gcc_cmd)
        
    def get_best_params(self):
        return self._best_params