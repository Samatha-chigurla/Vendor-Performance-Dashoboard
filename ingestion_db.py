


import pandas as pd

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)






