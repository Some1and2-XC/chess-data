#!/usr/bin/env python3

import chess
# from chess import get_data

if __name__ == "__main__":
    player = "hikaru"
    player_data_file = "player_data_hikaru.plk"
    # player_data_file = chess.get_data(player)
    chess.read_stats(player_data_file)
    # input("\t~FINISHED!")
