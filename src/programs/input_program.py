from ..configuration.tuner import Tuner

class Program:
    def __init__(self, file_name: str, need_compile: bool, params: dict) -> None:
        self._file_name = file_name
        self._need_compile = need_compile
        self._params = params
        self._best_configuration = {}
        print("program")
        print(self._params)
        self._tuner = Tuner(self._file_name, self._need_compile, self._params)
        
        
    def run(self):
        self._best_configuration = self._tuner.get_best_params()
    
    def get_best_params(self):
        return self._best_configuration