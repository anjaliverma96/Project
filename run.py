
import argparse
import logging.config
logging.config.fileConfig("config/logging/local.conf")
logger = logging.getLogger("run-whos-the-boss")

from src.downloadData import load_data
from config import BUCKET_NAME

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Data processes")
    subparsers = parser.add_subparsers()

    sub_process = subparsers.add_parser('loadS3')
    sub_process.add_argument("--bucket", type=str, default=BUCKET_NAME, help="Bucket to be copied to")
    sub_process.set_defaults(func=load_data)

    args = parser.parse_args()
    args.func(args)






