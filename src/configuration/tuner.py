from ..search.grid_search import GridSearch

class Tuner:
    ''' Tuner
    
    @attribute _file_name: The name of the targeted file
    @attribute _need_compile: Whether the file need to be compiled
    @attribute _params: All possible parameters
    @attribute _search: The search algorithm
    @attribute _best_params: The best parameters
    '''
    def __init__(self, file_name: str, need_compile: bool, params: dict , search = 'grid_search') -> None:
        ''' Initialize the tunner
        
        @param file_name: The name of the targeted file
        @param need_compile: Whether the file need to be compiled
        @param params: All possible parameters (eg: {block_size: (2, 4, 8), gcc_flag: (O1, O2, O3)})
        '''
        self._file_name = file_name
        self._need_compile = need_compile
        self._params = params
        if search == 'grid_search':
            self._search = GridSearch(file_name, need_compile, params)
        self._best_params = {}
        
        
    def get_best_params(self):
        self._search.run()
        self._best_params = self._search.get_best_params()
        return self._best_params