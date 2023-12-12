#!/usr/bin/env python3

from .default_imports import *

from .analytics import read_stats

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

def get_links(player_name):
    archives_url = f"https://api.chess.com/pub/player/{player_name}/games/archives/"
    responce = requests.get(archives_url, headers=headers) 
    return responce.json()["archives"]


def get_data(player_name):
    archive_links = get_links(player_name)
    print(archive_links)
    df = None

    for link in archive_links:
        new_df = pd.json_normalize(
            data=requests.get(link, headers=headers).json(),
            record_path=["games"],
            max_level=5
        )

        if df is None:
            df = new_df
        else:
            df = pd.concat([df, new_df])
        print(link, end="\r")

    print("Saving Data...")
    filename = f"player_data_{player_name}_norm.plk"
    with open(filename, "wb") as f:
        pickle.dump(df, f)
    return filename
