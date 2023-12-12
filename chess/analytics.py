#!/usr/bin/env python3

from .default_imports import *

"""
Index(['url', 'pgn', 'time_control', 'end_time', 'rated', 'accuracies', 'tcn',
       'uuid', 'initial_setup', 'fen', 'time_class', 'rules', 'white', 'black',
       'start_time', 'tournament'],
      dtype='object')
"""

def get_file_data(filename: str) -> pd.DataFrame:
    """
    Function for getting the dataframe from a file
    """

    with open(filename, "rb") as f:
        df = pickle.load(f)
        f.close()
    return df


def get_game_subset(df, game_time_class: str, game_rules: str = "chess"):
    """
    Function for getting a subset of games with the specifications
        (df.time_control == game_time) & \
    """

    return df.query("(time_class==@game_time_class) & (rules==@game_rules)")


def read_stats(username: str, filename: str):
    """
    Function for reading the stats of a player from a stats file
    """

    df = get_file_data(filename)

    with open("outfile.csv", "w") as f:
        df.head(1000).to_csv(f)
    exit()
    analytics_df = get_game_subset(df, "bullet", "chess")

    
    print(pd.DataFrame.from_dict(analytics_df.white, orient="index", columns=["username", "result"]))
    exit()

    results = pd.concat([
        pd.DataFrame.from_dict(analytics_df.black),
        pd.DataFrame.from_dict(analytics_df.white)
    ])

    print(results)
    exit()

    "win timeout resigned checkmated agreed repetition"
    print(games_as_black)
    # print(games_as_white)
    """
    df_control_mode_subset = df[df
    games_as_black = df.loc([])
    games_as_white = ""
    game_elo_accuracies = ""
    performance_over_time = ""

    analytics_df = pd.DataFrame(
            df.accuracies
    )
    """

    df = get_game_subset(df, "bullet", "chess")

    print(df.head())
    print(df.columns)
