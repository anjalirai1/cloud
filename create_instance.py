import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-cd0f5cb6',
    MinCount=1,
    MaxCount=1,
    #PrivateIpAddress='10.10.0.1',
    #SecurityGroupIds=sg,
    SubnetId='subnet-5432947f',#Not required
    #VpcId=SubnetId,
    InstanceType='t2.micro')

print(instance[0].id)
