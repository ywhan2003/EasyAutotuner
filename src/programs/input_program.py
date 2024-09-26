from ..configuration.tuner import Tuner

class Program:
    '''
    Used to handle the input programs
    
    @attribute _file_name: The name of the targeted file
    @attribute _need_compile: Whether the file need to be compiled
    @attribute _params: All possible parameters
    @attribute _best_params: The result of the tuner
    @attribute _tuner: The tunner
    '''
    def __init__(self, file_name: str, need_compile: bool, params: dict) -> None:
        ''' Initialize the input programs
        
        @param file_name: The name of the targeted file
        @param need_compile: Whether the file need to be compiled
        @param params: All possible parameters (eg: {block_size: (2, 4, 8), gcc_flag: (O1, O2, O3)})
        '''
        self._file_name = file_name
        self._need_compile = need_compile
        self._params = params
        self._best_params = {}
        self._tuner = Tuner(self._file_name, self._need_compile, self._params)
        
        
    def run(self):
        self._best_params = self._tuner.get_best_params()
    
    def get_best_params(self):
        return self._best_params