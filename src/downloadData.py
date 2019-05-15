import boto3

def load_data(args):

    s3 = boto3.resource('s3')

    bucketname = args.bucket

    copy_source1 = {'Bucket': 'jokerecommender', 'Key': 'ratings.csv'}
    copy_source2 = {'Bucket': 'jokerecommender', 'Key': 'jokes.csv'}

    bucket = s3.Bucket('bucketname')

    bucket.copy(copy_source1, 'ratings.csv')
    bucket.copy(copy_source2, 'jokes.csv')
