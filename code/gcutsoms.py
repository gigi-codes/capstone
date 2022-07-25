##### BASIC IMPORTS 
import numpy as np
import pandas as pd

# # # Function for EIA data requests
def eia_req(KEY, CATEGORY):
    url = 'https://api.eia.gov/series/?api_key=' + KEY + '&series_id=' + CATEGORY
    
    # REQUEST 
    req = requests.get(url)
    print ('Request Code:' + str(req.status_code))

    # getting data 
    data = pd.DataFrame(req.json()['series'][0]['data'])

    return (data)


# # # FUNCTION TO CONVERT DATE COLUMN INTO INDEX 
def dt_index(df_in, col_title):

	df = df_in
	df['date'] = pd.to_datetime(df[col_title])
	df = df.set_index('date')	
	df.rename(columns = {'col_title': 'd'})
	df.sort_index(inplace = True)
	
	return(df)
	
# def date_index(df): 
#     # df.dropna(inplace=True)
#     df['ds'] = df['date']
#     df['date'] = pd.to_datetime(df['date'])
#     df = df.set_index('date')
#     print(df.head(3))
#     return(df)
#     
# 	        # ensure date is datetime format, set as index
#         df.set_index('dt')
#         # pd.to_datetime(df.date)
#         
#         # df.index = pd.to_datetime(df['date'])
#         # df.sort_index(inplace=True)
#         
#         # df['date'] = pd.to_datetime(df.index)
#         # df['weekday'] = df.ds.dt.dayofweek
#         
#         # df['ds'] = df_y.index