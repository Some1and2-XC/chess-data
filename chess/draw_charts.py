#!/usr/bin/env python3

from .default_imports import *

def result_pie_chart(wins_count, draws_count, losses_count, chart_title):
    """
    Function for drawing pie chart of the amount of wins/losses etc
    """

    sns.set_theme()

    plt.pie(
        [wins_count, draws_count, losses_count],
        labels=["Wins", "Draws", "Losses"],
        autopct="%1.0f%%"
    )
    plt.title(chart_title)
    plt.show()


def wins_on_colors(df, username):
    """
    Function for drawing a bar chart of the wins on different colors
    """

    sns.set_theme()

    played_white = df[df.is_black == False]
    played_black = df[df.is_black]

    labels=["Wins", "Draws", "Losses"]
    x_axis = np.arange(len(labels))

    white_data = [
        sum(played_white.result == 1),
        sum(played_white.result == 0.5),
        sum(played_white.result == 0)
    ]

    black_data = [
        sum(played_black.result == 1),
        sum(played_black.result == 0.5),
        sum(played_black.result == 0),
    ]

    plt.bar(x_axis - 0.2, white_data, color="w", edgecolor="black", width=0.4, label="White")
    plt.bar(x_axis + 0.2, black_data, color="black", edgecolor="black", width=0.4, label="Black")
    plt.xticks(x_axis, labels)
    plt.show()


def result_hist(df_wins, df_losses, df_draws, filename, rating_range, username):
    """
    Function for drawing a histogram of results
    """

    fig, ax = plt.subplots()

    df_wins.rename("wins")
    df_draws.rename("draws")
    df_losses.rename("losses")

    sns.set_theme()
    ax.hist(
         [df_wins, df_draws, df_losses],
         bins=20,
         range=rating_range,
         color=["r", "g", "b"],
         alpha=.75,
         histtype="barstacked",
         label=["Wins", "Draws", "Losses"]
     )
    plt.xlabel("opponent rating")
    plt.ylabel("games count")
    plt.title(f"Result Frequency of {username.title()}")
    leg = ax.legend()
    plt.show()



