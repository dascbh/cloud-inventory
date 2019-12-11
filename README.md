Docker image build
-build -t python-ec2-inventory .

Docker run example
-docker run -e AWS_ACCESS_KEY_ID=KEY -e AWS_SECRET_ACCESS_KEY=SECRET -e AWS_DEFAULT_REGION=us-west-2 -v $PWD:/usr/src/app python-ec2-inventory