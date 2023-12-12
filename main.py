#!/usr/bin/env python3

import chess
# from chess import get_data

if __name__ == "__main__":
    player = "hikaru"
    player_data_file = "player_data_hikaru_norm.plk"
    # player_data_file = chess.get_data(player)
    chess.read_stats(player, player_data_file)
    # input("\t~FINISHED!")
"""    
...        NaN
1  https://www.chess.com/game/live/692670646  ...        NaN
2  https://www.chess.com/game/live/692695595  ...        NaN
3  https://www.chess.com/game/live/692696567  ...        NaN
4  https://www.chess.com/game/live/692700868  ...        NaN
"""
