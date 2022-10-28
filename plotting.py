from matplotlib import pyplot as plt
import pandas as pd

minimax_data = pd.read_csv('data/minimax-data.csv')
abpruning_data = pd.read_csv('data/abpruning-data.csv')

minimax_data.plot()