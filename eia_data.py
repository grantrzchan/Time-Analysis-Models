import requests
import pandas as pd
import eia
from eia_api_key import eia_api_key

def get_series(api, series_id):
    '''Return the time series dataframe, based on API and unique Series ID'''
    df = pd.DataFrame(api.data_by_series(series=series_id))
    df.reset_index(inplace=True) #create index column, count rows from 0
    return df


api = eia.API(eia_api_key)
df = get_series(api, 'PET.MKJUPUS2.A')
df.columns = ['Year', 'Jet Fuel Supplied (kbpd)']
print(df.head(20))