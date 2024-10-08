import argparse
from src.programs.input_program import Program

parser = argparse.ArgumentParser()
parser.add_argument("--search", type=str, default='grid')

if __name__ == '__main__':
    args = parser.parse_args()
    program = Program('./target_programs/matrix_multiplication.c', True, 
                      {'o': ('O0', 'O1', 'O2', 'O3'), 's': ('8', '16', '32', '64', '128')}, args.search)
    program.run()
    print(program.get_best_params())