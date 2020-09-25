import pandas as pd
from sqlalchemy import create_engine
import psycopg2

weather_file = 'austin_weather.csv'
crime_file = "austin_crime.csv"

weather_df = pd.read_csv(weather_file)
crime_df = pd.read_csv(crime_file)



''' Cleaned up the weather dataframe and dropped all unwanted data'''
weather_columns = weather_df[['Date','TempHighF','TempAvgF','TempLowF','Events']]
clean_weather_df = weather_columns.copy()
clean_weather_df['Date'] = pd.to_datetime(clean_weather_df['Date'])


'''==============================================================='''
crime_columns = crime_df[['timestamp','unique_key','description']]
clean_crime_df = crime_columns.copy()
clearn_crime_df = clean_crime_df.dropna(how='any',inplace=True)
clean_crime_df['timestamp'] = pd.to_datetime(clean_crime_df['timestamp'])
clean_crime_df=clean_crime_df.rename(columns={'timestamp' : 'Date'})

merged_df = pd.merge(clean_crime_df,clean_weather_df,how='inner', on = 'Date')




connection_string = "postgres: INSERT PASSWORD !@localhost:5432/ETL"
engine = create_engine(f'postgresql://{connection_string}') 

merged_df.to_sql(name='crimeByweather', con=engine, if_exists='append', index=True) 

