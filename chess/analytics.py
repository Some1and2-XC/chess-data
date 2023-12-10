#!/usr/bin/env python3

from .default_imports import *

"""
Index(['url', 'pgn', 'time_control', 'end_time', 'rated', 'accuracies', 'tcn',
       'uuid', 'initial_setup', 'fen', 'time_class', 'rules', 'white', 'black',
       'start_time', 'tournament'],
      dtype='object')
"""

def read_stats(filename: str):
    """
    Function for reading the stats of a player from a stats file
    """

    with open(filename, "rb") as f:
        df = pickle.load(f)
        f.close()

    print(df.head())
    print(df.columns)
