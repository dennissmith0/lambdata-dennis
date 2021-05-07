""" Lambdata - A collection of data science functions"""

import pandas as pd
import numpy as np

FAVORITE_ANIMALS = ['BALD EAGLE', 'TARDIGRADE', 'MOUNTAIN LION', np.nan]

def null_count(df):
    """Cleans dataFrames"""
    return(df.isnull())


print('prime')
