#!/usr/bin/env python3

from .default_imports import *

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


def get_score(df, username: str, col_checked: str, col_result: str, conditions: list[str], factor: float):
    """
    Function for getting the score of a game
    col_checked is the column that is being read from
    col_result is the column that the result is being applied to
    conditions is a list of conditions to make the result happen
    factor is the amount of points the result is worth
    """

    colors = ["black", "white"]

    for color in colors:
        for result in conditions:
            df.loc[
                (df[f"{color}.{col_checked}"] == result) & \
                (df[f"{color}.username"].str.lower() == username.lower()) \
            ,col_result] += factor

    return df


def win_hist(df_wins, df_losses, df_draws, filename):
    sns.histplot(
        data=[df_wins, df_draws, df_losses],
        x="rating",
        multiple="dodge",
        discrete=True
    )
    plt.show()
    """
    plt.hist(df["black.rating"], 20, (1800, 4000), histtype="bar")
    plt.xlabel("Result Frequency")
    plt.ylabel("Amount of Games")
    plt.title("Result Frequencies")
    plt.show()
    """


def make_charts(username: str, filename: str):
    """
    Function for reading the stats of a player from a stats file
    """

    df = get_file_data(filename)

    analytics_df = get_game_subset(df, "bullet", "chess")

    # Adds Result column
    analytics_df.insert(11, "result", [0.0] * len(analytics_df))
    win_conditions = ["win"]
    draw_conditions = ["agreed", "repetition", "insufficient", "stalemate", "50move", "timevsinsufficient"]
    analytics_df = get_score(analytics_df, username, "result", "result", win_conditions, 1)
    analytics_df = get_score(analytics_df, username, "result", "result", draw_conditions, 0.5)

    # Makes Player allways white
    values_to_swap = [
        ["accuracies.white", "accuracies.black"],
        ["white.rating", "black.rating"],
        ["white.result", "black.result"],
        ["white.@id", "black.@id"],
        ["white.username", "black.username"],
        ["white.uuid", "black.uuid"]
    ]

    # Swaps white and black if the username is different
    for swap in values_to_swap:
        analytics_df.loc[ \
            analytics_df["black.username"].str.lower() == username.lower(), \
            swap \
        ] = analytics_df.loc[ \
            analytics_df["black.username"].str.lower() == username.lower(), \
        swap[::-1]].values

    games_won = analytics_df[analytics_df.result == 1]

    # Saves Graphs


    """
    win_hist(
            analytics_df.loc[analytics_df.result == 1, "black.rating"],
            analytics_df.loc[analytics_df.result == 0.5, "black.rating"],
            analytics_df.loc[analytics_df.result == 0, "black.rating"],
            "")
    with open("outfile.csv", "w") as f:
        analytics_df.head(1000).to_csv(f)
    """

    return analytics_df
