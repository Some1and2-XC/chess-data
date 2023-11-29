#!/usr/bin/env python3

import requests
import pandas as pd
import pickle

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

def get_links(player_name):
    archives_url = f"https://api.chess.com/pub/player/{player_name}/games/archives/"
    responce = requests.get(archives_url, headers=headers) 
    return responce.json()["archives"]


def get_data(player_name):
    archive_links = get_links(player_name)
    df = None

    for link in archive_links:
        new_df = pd.DataFrame(
            requests.get(link, headers=headers).json()["games"]
        )

        if df is None:
            df = new_df
        else:
            df = pd.concat([df, new_df])
        print(link, end="\r")
    print("Saving Data...")
    with open(f"player_data_{player_name}.plk", "wb") as f:
        pickle.dump(df, f)
