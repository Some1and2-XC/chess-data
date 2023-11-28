#!/usr/bin/env python3

from . import get_links

class Player:
    def __init__(self, name, username):

        url_strings = {
            " ": "%20"
        }

        for key, value in url_strings.items():
            name = value.join(name.split(key))

        self.name = name
        self.username = username


    def get_game_links(self):
        from re import findall as re
        from requests import get
        import lxml.html

        iteration = 1  # The iteration the while loop is on
        MAX_I = 1  # the maximum iteration the while loop will go to
        games_links = []  # a list of games to return

        while True or iteration < MAX_I:
            games_links.append(
                get(f"https://www.chess.com/games/search?p1={self.name}&page={iteration}").links
            )
            # https://www.chess.com/games/view/
            iteration += 1
            print(f"i={iteration}", end="\r")

        return games_list

        
        


def main(user_class):
    v = user_class.get_game_links()
    print(v)

