import boto3

def lambda_handler(event, context):
    # Specify the security group ID you want to identify instances for
    security_group_id = 'sg-0123456789abcdef0'

    ec2 = boto3.client('ec2')

    instances = []
    response = ec2.describe_instances(Filters=[{'Name': 'instance.group-id', 'Values': [security_group_id]}])
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name']
            })

    if instances:
        return {
            'statusCode': 200,
            'body': {
                'message': f'Instances using security group {security_group_id}',
                'instances': instances
            }
        }
    else:
        return {
            'statusCode': 404,
            'body': {
                'message': f'No instances found using security group {security_group_id}',
                'instances': []
            }
        }
