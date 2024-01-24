import pandas as pd
def create_dataframe(pal, df):
    pal_df = df[df[df.keys()] == pal].dropna(how="all").dropna(how="all", axis=1)
    aux = pal_df.to_dict()
    pal_tuple = []
    for i in aux:
        for j in aux[i]:
            if aux[i][j] == "Suzaku":
                pal_tuple.append((i, j))
    res = list({*map(tuple, map(sorted, pal_tuple))})
    pal_final_df = pd.DataFrame(res, columns=["Parent 1", "Parent 2"])
    return pal_final_df