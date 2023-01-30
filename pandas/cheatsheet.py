import pandas as pd
import datetime
from datetime import date  
from dateutil import parser

ufo = pd.read_csv("/Users/ikram/Desktop/Sequeces/pandas/data/ufo_sighting_data.csv")

#todays date 
now = pd.to_datetime(str(date.today()), format = '%Y-%m-%d')
print(now)

#dif b/w oldest and max date in dataset
ufo['Datetime'] = ufo['Date_time'].astype('datetime64[ns]')

ufo[['date','time']] = ufo['Date_time'].str.split(expand=True)
ufo['Datetime'] = (pd.to_datetime(ufo.pop('date'), format='%m/%d/%Y') + 
                  pd.to_timedelta(ufo.pop('time') + ':00'))

oldest = ufo.Datetime.min()
newest = ufo.Datetime.max()
days_between = (newest-oldest).days

#forty years
duration = datetime.timedelta(days=365*40)

subset_ufo = ufo[now - ufo['Datetime'] <= duration]

#specific period eg 1950-1960

fifties_ufo = ufo[(ufo['Datetime'] >= '1950-09-30 00:00:00') & (ufo['Datetime'] <= '1960-11-01 00:00:00')]

ufo['Year'] = ufo.Datetime.dt.year
ufo['Minute'] = ufo.Datetime.dt.minute
ufo['Weeday'] = ufo.Datetime.dt.weekday_name

ufo['Year']  = ufo['Datetime'].apply(lambda x:  "%d" % (x.year))

result = ufo.groupby(['Year','country']).size()

#unique dates
unique = ufo['Datetime'].map(lambda t : t.date()).unique()