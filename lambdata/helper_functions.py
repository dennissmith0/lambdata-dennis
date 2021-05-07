# Unit 3 Sprint 1 Module 1

import numpy as np
import pandas as pd

#def null_count(df): Check a dataframe for nulls and return the 
#       number of missing values.
#   returns total sum of null values from given DataFrame
def null_count(df):
    return df.isnull().sum().sum()


def train_test_split(df, frac=0.2):
    n_df = len(df)
    if n_df == 0:
        raise ValueError('At least one array required as input')
    
    train = df.head(int(len(df)* frac))
    test = df.tail(int(len(df)* (1-frac)))
    return train, test