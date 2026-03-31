import pandas as pd

def map_data(df, master_file):
    master = pd.read_excel(master_file)

    df = df.merge(master, on="product", how="left")

    return df