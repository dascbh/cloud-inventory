# -*- coding: utf-8 -*-

import json
import os
import sys
import boto3
import pymongo

from html_builder import create_html

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
aws_default_region = os.environ['AWS_DEFAULT_REGION']
aws_account_name = os.environ['AWS_ACCOUNT_NAME']
env_tags_to_seek = os.environ['ENV_TAGS_TO_SEEK']

ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
response = ec2.describe_instances()

instances = []

def mongodb_insert(data):
    connection = pymongo.MongoClient("mongodb://cloud:1nv3ntory@localhost")
    database = connection.inventories
    collection = database.ec2instances
    collection.insert(data)
    connection.close()
    return

def create_inst_obj(inst_id, inst_status, inst_type, inst_tags):
	inst_obj = {}
	inst_obj["Instance Id"] = inst_id
	# inst_obj["Owner"] = "-"
	inst_obj["Status"] = inst_status
	# inst_obj["Monthly Cost"] = "U$ 0"
	inst_obj["Instance Type"] = inst_type
	# inst_obj["Reserved"] = "No"
	# inst_obj["Actions"] = "Start | Stop"
	# inst_obj["Account"] = aws_account_name

	tags = {}
	temp_values = []
	temp_k_v = {}
	for i in inst_tags:
		temp_values.append(i['Value'])
		temp_k_v[i['Key']] = i['Value']

	if temp_k_v['Ambiente'] in env_tags_to_seek:
		inst_obj["Name"] = temp_k_v['Name']

		temp_k_v.pop('Name', None)
		inst_obj["Tags"] = temp_k_v

		return inst_obj
	else:
		return None

def main():
	for i in response['Reservations']:
		# print i['Instances']
		# print i['Instances'][0]['InstanceId']
		# print i['Instances'][0]['State']['Name']
		# print i['Instances'][0]['InstanceType']
		# print i['Instances'][0]['Tags']

		obj = create_inst_obj(i['Instances'][0]['InstanceId'], i['Instances'][0]['State']['Name'], i['Instances'][0]['InstanceType'], i['Instances'][0]['Tags'])

		if obj:
			instances.append(obj)
			mongodb_insert(obj)
		else:
			pass

	# for i in instances:
	# 	print json.dumps(i)

	create_html(instances)

	return

if __name__ == "__main__":
	main()