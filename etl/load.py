import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def load_data(df, file_path, table_name=None):
    try:
        # Save DataFrame to CSV
        df.to_csv(file_path, index=False)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")

    if table_name:
        try:
            # Get database credentials from environment variables
            user = os.getenv('POSTGRES_USER')
            password = os.getenv('POSTGRES_PASSWORD')
            host = os.getenv('POSTGRES_HOST')
            port = os.getenv('POSTGRES_PORT')
            db = os.getenv('POSTGRES_DB')

            # Create a SQLAlchemy engine using environment variables
            engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')
            # Save DataFrame to PostgreSQL
            df.to_sql(table_name, engine, index=False, if_exists='replace')
            print(f"Data successfully saved to PostgreSQL table {table_name}")
        except Exception as e:
            print(f"Error saving data to PostgreSQL: {e}")
