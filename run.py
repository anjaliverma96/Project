

"""Enables the command line execution of multiple modules within src/
This module combines the argparsing of each module within src/ and enables the execution of the corresponding scripts
so that all module imports can be absolute with respect to the main project directory.

Command to load data into S3 bucket 
python run.py loadS3
Command to add databse schema data folder in the project repository 
python run.py createSqlite
Command to add database schema in RDS
python run.py createRDS
"""


import argparse
import logging.config
logging.config.fileConfig("config/logging/local.conf")
logger = logging.getLogger("jokerecommender")

#import necessary functions from src modules

from src.downloadData import load_data
from src.add_schema import create_sqlite_db, create_rds_db

#import necessary variables from config file

from config import BUCKET_NAME, SQLALCHEMY_DATABASE_URI, DATABASE_NAME




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Data processes")
    subparsers = parser.add_subparsers()

    sub_process = subparsers.add_parser('loadS3')
    sub_process.add_argument("--bucket", type=str, default=BUCKET_NAME, help="Bucket to be copied to")
    sub_process.set_defaults(func=load_data)

    sub_process = subparsers.add_parser('createSqlite')
    sub_process.add_argument("--engine_string", type=str, default=SQLALCHEMY_DATABASE_URI,
                             help="Connection uri for SQLALCHEMY")
    sub_process.set_defaults(func=create_sqlite_db)

    sub_process = subparsers.add_parser('createRDS')
    sub_process.add_argument("--database", type=str, default=DATABASE_NAME,
                             help="Database in RDS")
    sub_process.set_defaults(func=create_rds_db)

    args = parser.parse_args()
    args.func(args)






