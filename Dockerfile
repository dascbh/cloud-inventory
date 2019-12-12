FROM python:3

ENV AWS_ACCESS_KEY_ID=''
ENV AWS_SECRET_ACCESS_KEY=''
ENV AWS_DEFAULT_REGION='us-east-1'
ENV AWS_ACCOUNT_NAME='SANDBOX'
ENV ENV_TAGS_TO_SEEK=['DEV','PRJ','HML']

WORKDIR /usr/src/app
COPY . .

RUN pip install boto3
RUN pip install json2html
RUN pip install pymongo

CMD [ "python", "./ec2_inventory.py" ]