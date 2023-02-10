import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def general_info(df):
    """Get all columns and total missin values of each column.
    Args:
        df(DataFrame): Pandas DataFrame.
    Returns:
        DataFrame.
    """
    print(df.info())
    print('*' * 50)
    print('Missing Values')
    print(df.isna().sum())

### Get Columns ###
    
def get_all_columns(df):
    """Get all column names.
    Args:
        df(DataFrame): Pandas DataFrame.
    Returns:
         A list of all column names.
    """
    columns = df.columns.tolist()
    return columns

def get_feature_columns(df):
    """Get feature column names 
    Args:
        df(DataFrame): Pandas DataFrame
    Returns:
        A list of feature column names.
    """
    columns = df.columns.tolist()
    feature_columns = columns[:-1]
    return feature_columns

def get_target_column(df):
    """Get a target column name
    Args:
        df(DataFrame): Pandas DataFrame
    Returns:
        A list of the target column name.
    """
    columns = df.columns.tolist()
    target_col = columns[-1]
    return target_col


#### Make Plot ####

def hist_plot_pd(df):
    """Plot histogram of a dataframe.
    Args:
        df(DataFrame): Pandas DataFrame
    Returns:
        The Pandas histogram, using underlying Matplotlib.
    """
    return df.hist(figsize=(16,12), grid=False,  edgecolor="black", alpha=0.8)

def box_plot_pd(df):
    """Plot boxplot of a dataframe.
    Args:
        df(DataFrame): Pandas DataFrame
    Returns:
        The Pandas boxplot, using underlying Matplotlib.
    """
    return df.plot(kind="box", figsize=(16,12))



