import pandas as pd 
import psycopg2 as psy
from sqlalchemy import create_engine
db_params = {
    'host': '0.0.0.0',
    'port' : '15432',
    'database': 'youtube_data',
    'user': 'postgres',
    'password': '',

}

engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")


def load_data_and_create_tables(folder_path, folder_name):
    chart_data = pd.read_csv(f'{folder_path}/Chart data.csv')
    chart_table_name = f'{folder_name}_chart'
    chart_data.to_sql(chart_table_name, engine, index=False, if_exists='replace')

    table_data = pd.read_csv(f'{folder_path}/Table data.csv')
    table_table_name = f'{folder_name}_table'
    table_data.to_sql(table_table_name,engine, index=False, if_exists='replace')

    # Load total data
    total_data = pd.read_csv(f'{folder_path}/Totals.csv')
    total_table_name = f'{folder_name}_total'
    total_data.to_sql(total_table_name, engine, index=False, if_exists='replace')


data_folder = 'youtube-data'

folders = ['Cities', 'Content type', 'Device type', 'Geography', 'New and returning viewers',
           'Operating system', 'Sharing service', 'Subscription source', 'Subscription status',
           'Subtitles and CC', 'Traffic source']
for folder in folders:
    folder_name = folder.replace(' ', '_').lower()
    folder_path = f'{data_folder}/{folder}'
    load_data_and_create_tables(folder_path, folder_name)


print("Data loaded into the PostgreSQL database and tables created successfully.")

