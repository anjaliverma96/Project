import boto3


class Boto:

	def download_rating(self):

		s3_resource = boto3.resource('s3')
		bucket = s3_resource.Bucket('jokerecommender')
		bucket.download_file('../data/ratings.csv','ratings.csv') #path, from

	def download_jokes(self):
		
		s3_resource = boto3.resource('s3')
		bucket = s3_resource.Bucket('jokerecommender')
		bucket.download_file('jokes.csv','jokes.csv')

		