import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.configuration.tuner import Tuner

file_name = './target_programs/matrix_multiplication.c'
tuner = Tuner(file_name)

tuner.add_parameter('o', ('O0', 'O1', 'O2', 'O3'))
tuner.add_parameter('s', ('8', '16', '32', '64', '128'))

print(tuner.get_best_params())