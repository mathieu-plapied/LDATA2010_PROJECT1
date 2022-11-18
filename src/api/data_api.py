import pandas as pd
import pandas.core.series


def fetch_data(path: str) -> pd.DataFrame:
    """

    :param path:
    :return: return a data frame to the components that ask for it.
    """
    df = pd.read_csv(path)
    return df


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
