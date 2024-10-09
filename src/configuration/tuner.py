from ..search.grid_search import GridSearch
from ..search.bandit_search import BanditSearch

class Tuner:
    ''' Tuner
    
    :attribute _file_name: The name of the targeted file
    :attribute _need_compile: Whether the file need to be compiled
    :attribute _params: All possible parameters
    :attribute _search: The search algorithm
    :attribute _best_params: The best parameters
    '''
    def __init__(self, file_name: str, params: dict = {}, search = 'grid') -> None:
        ''' Initialize the tunner
        
        :param file_name: The name of the targeted file
        :param params: All possible parameters (eg: {block_size: (2, 4, 8), gcc_flag: (O1, O2, O3)})
        '''
        self._file_name = file_name
        self._need_compile = 'o' in params
        self._params = params
        self._search = search
        self._search_alg = None
        self._set_search(search, file_name, self._need_compile, params)
        self._best_params = {}
        
    def get_best_params(self):
        '''
        Execute the search algorithm and get the best parameter configurations
        '''
        assert(self._search_alg is not None)
        self._search_alg.run()
        self._best_params = self._search_alg.get_best_params()
        return self._best_params
    
    def add_parameter(self, param_name: str, combinations: tuple):
        '''Add parameters for the tuner
        
        :param param_name: The name of the new parameters
        :param combinations: All possible value of the new parameter
        '''
        if param_name not in self._params:
            self._params[param_name] = combinations
            if param_name == 'o':
                self._need_compile = True
        else:
            prev = self._params[param_name]
            self._params[param_name] = set(prev).union(combinations)

        self._set_search(self._search, self._file_name, self._need_compile, self._params)
            
    def get_paramters(self):
        return self._params
    
    def _set_search(self, search: str, file_name: str, need_compile: bool, params: dict):
        if search == 'grid':
            self._search_alg = GridSearch(file_name, need_compile, params)
        if search == 'bandit':
            self._search_alg = BanditSearch(file_name, need_compile, params)