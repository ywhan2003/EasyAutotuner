from abc import ABC, abstractmethod
import sys

class Search(ABC):
    ''' Search algorithm
    
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
        self._file_name = file_name
        self._need_compile = need_compile
        self._params = params
        self._best_params = {}
        self._best_result = sys.maxsize
        
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def _single_execution(self, current_params: dict):
        pass