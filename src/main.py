from .programs.input_program import Program

if __name__ == '__main__':
    program = Program('./target_programs/matrix_multiplication.c', True, {'o': ('O1', 'O2'), 's': ('4', '8')}, 'bandit_search')
    program.run()
    print(program.get_best_params())