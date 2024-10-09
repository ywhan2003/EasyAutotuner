from abc import ABC, abstractmethod
import itertools
import os
import sys

class Search(ABC):
    ''' Search algorithm
    
    :attribute _file_name: The name of the targeted file
    :attribute _need_compile: Whether the file need to be compiled
    :attribute _params: All possible parameters
    :attribute _best_params: The parameters performing the best
    :attribute _best_result: The best performance
    '''
    def __init__(self, file_name: str, need_compile: bool, params: dict) -> None:
        ''' Initialize the Grid Search
        
        :param file_name: The name of the targeted file
        :param need_compile: Whether the file need to be compiled
        :param params: All possible parameters (eg: {block_size: (2, 4, 8), gcc_flag: (O1, O2, O3)})
        :param best_params: The parameters performing the best
        :param best_result: The best performance
        '''
        self._file_name = file_name
        self._need_compile = need_compile
        self._params = params
        self._best_params = {}
        self._best_result = sys.maxsize
        
    @abstractmethod
    def run(self):
        '''
        Execute the specific search algorithm to get the best parameter configuration
        '''
        pass
    
    @abstractmethod
    def _single_execution(self, current_params: dict):
        '''
        Execute the program with one specific parameter configuration
        '''
        pass
    
    def get_best_params(self):
        '''
        Return the best parameter configuration
        Should be called after the run() function
        '''
        return self._best_params
    
    def _get_and_execute_command(self, target_file_name:str, current_params: dict):
        '''
        Construct the command with specific parameters and execute the commands
        
        :param target_file_name: The file to be operated
        :param current_params: Current parameter configuration
        '''
        if self._need_compile:
            gcc_cmd = 'gcc -'
            gcc_cmd += current_params['o']
            gcc_cmd += ' '
            gcc_cmd += self._file_name
            gcc_cmd += ' -o '
            index = self._file_name.rfind('.')
            target_file_name = self._file_name[: index]
            gcc_cmd += target_file_name
            os.system(gcc_cmd)
            
        gcc_cmd = target_file_name
        gcc_cmd += ' '
        gcc_cmd += current_params['s']
        os.system(gcc_cmd)
        
    def _clear_temporary_file(self):
        assert(self._need_compile)
        index = self._file_name.rfind('.')
        delete_file_name = self._file_name[: index]
        # print(delete_file_name)
        os.system("rm -rf " + delete_file_name)
        
    def _get_all_combinations(self, dic: dict) -> list:
        '''
        Get all combinations of the dict
        '''
        keys = dic.keys()
        values = dic.values()
        combinations = itertools.product(*values)
        
        combinations_with_keys = []

        for combo in combinations:
            combo_with_keys = dict(zip(keys, combo))
            combinations_with_keys.append(combo_with_keys)
            
        return combinations_with_keys