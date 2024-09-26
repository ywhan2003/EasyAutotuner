from ..search.grid_search import GridSearch

class Tuner:
    def __init__(self, file_name: str, need_compile: bool, params: dict , search = 'grid_search') -> None:
        self._file_name = file_name
        self._need_compile = need_compile
        self._params = params
        print("tuner")
        print(self._params)
        if search == 'grid_search':
            self._search = GridSearch(file_name, need_compile, params)
        self._best_params = {}
        
        
    def get_best_params(self):
        self._search.run()
        self._best_params = self._search.get_best_params()
        return self._best_params