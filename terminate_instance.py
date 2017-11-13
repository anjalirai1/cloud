import boto3

ec2 = boto3.resource('ec2')
ids = ['i-055fd316c82630c17']
ec2.instances.filter(InstanceIds=ids).stop()
ec2.instances.filter(InstanceIds=ids).terminate()
im