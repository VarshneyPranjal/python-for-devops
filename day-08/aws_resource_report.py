import boto3
import json

class AWSUtils:

	def __init__(self):
		self.s3 = self.get_connection("s3")
		self.data = {"Buckets": []}

	def get_connection(self, service):
		return boto3.client(service) #creating a client for s3 so that it can call APIs

	def show_buckets(self):
		response = self.s3.list_buckets() 
		for bucket in response["Buckets"]:
			self.data['Buckets'].append({"name":bucket['Name']})

	def create_bucket(self, bucket_name):
		try:
			response = self.s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint' : 'us-west-2',},)
			if response["ResponseMetadata"]["HTTPStatusCode"] == 200 :
				print("Bucket created Successfully")
			else:
				print("Error while creating bucket")
		except:
			print("Error occured")

	def upload_bucket(self,file_path, bucket_name, file_name):
		try: 
			self.s3.upload_file(file_path, bucket_name, file_name)
		except:
			print("Error occured while uploading file")

	def write_data(self, output_file):
        	with open(output_file, "w") as file:
            		json.dump(self.data, file, indent=4)	

if __name__ == "__main__":
	aws =AWSUtils() 		
	aws.show_buckets()
	aws.create_bucket("bucket-pranjal")
	aws.upload_bucket("practice/app2.log","bucket-pranjal","logs.json")
	aws.write_data("aws_report.json")
	# s3 = get_connection("s3")
	# ec2 = get_connection("ec2")
	# show_buckets(s3)
	# create_bucket(s3, "bucket-pranjal3")
	# upload_bucket(s3, "practice/app2.log", "bucket-pranjal", "logs.json")


