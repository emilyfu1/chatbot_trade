import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import dotenv_values, find_dotenv

# this looks for your configuration file and then reads it as a dictionary
config = dotenv_values(find_dotenv())

# set path using the dictionary key for which one you want
plotsdata = os.path.abspath(config["DATA_FIGURES"]) + '\\'

def processdata(hscode, area):
    # import data
    data = pd.read_csv(plotsdata + hscode + area + '.csv', skiprows=[0], low_memory=False)[['Period', 'Commodity', 'Value ($)']]
    # drop rows where the citation is stored
    data.drop(data.tail(3).index, inplace = True)
    # create column to use for grouping
    data['HS2'] = pd.to_numeric(data['Commodity'].str[0:2])
    # convert to datetime
    data['Period'] = pd.to_datetime(data['Period'])
    # groupby to get aggregation
    if hscode == 'all':
        data = data[['Period', 'HS2', 'Value ($)']].groupby(['Period']).sum().reset_index()
    else:
        data = data[['Period', 'HS2', 'Value ($)']].groupby(['Period', 'HS2']).sum().reset_index()
    # rename the column using the HS code and which area it corresponds to
    data.rename(columns={'Value ($)': hscode + area}, inplace=True)
    # keep relevant column
    data = data[['Period', hscode + area]]
    # set date index
    data.set_index('Period', inplace=True)
    return data