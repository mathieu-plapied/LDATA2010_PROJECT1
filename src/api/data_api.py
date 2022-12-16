import pandas as pd
import pandas.core.series
from sklearn.cluster import KMeans, AgglomerativeClustering
import numpy as np
from sklearn.decomposition import PCA

PATH_TRANSCRIPTOMICS = "././data/transcriptomics_data.csv"
PATH_PCA = "././data/pca.csv"


def get_dataframe() -> pd.DataFrame:
    """

    :param path:
    :return: return a data frame to the components that ask for it.
    """

    return pd.read_csv(PATH_TRANSCRIPTOMICS)


def load_data_frame(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def get_cells_count(df: pd.DataFrame):
    """
    Count the occurence of a cell in the dataframe.
    :param df:
    :return: a dictionary
    """
    cell_type = [i for i in range(0, 133)]
    cell_series = pd.Series(cell_type)
    count_series = pd.Series(df.cell_type.value_counts())
    # Creating a dictionary by passing Series objects as values
    frame = {'cell_type': cell_series, 'count': count_series}
    # Creating DataFrame by passing Dictionary
    return pd.DataFrame(frame)


def get_heatmap():
    return "cool"


def compute_pca():
    """
    Compute pca and returns a dataframe
    :return: a data frame composed of x and y values and the cell_type associeted
    """
    df = pd.read_csv(PATH_TRANSCRIPTOMICS)
    x = df.loc[:, "gene_0":"gene_299"]
    y = df.loc[:, "cell_type"]

    pca_classifier = PCA(n_components=2)

    pca_applied = pca_classifier.fit_transform(x)
    df_pca = pd.DataFrame(pca_applied, columns=["x", "y"])
    final = pd.concat([df_pca, pd.DataFrame(y, columns=["cell_type"])], axis=1)
    return final


def compute_kmeans(n_cluster, df: pd.DataFrame):
    # x = df.loc[:, "gene_0":"gene_299"]
    # y = df.loc[:, "cell_type"]
    kmeans = KMeans(n_cluster).fit(df.loc[:, "x":"y"])
    labels = np.array(kmeans.labels_).astype("str")
    return labels


def get_current_used_df():
    print(test)
