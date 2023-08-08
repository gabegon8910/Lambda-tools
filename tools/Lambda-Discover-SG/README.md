# Lambda Function: Identify Instances Using a Security Group

Welcome to the Lambda Function repository! This Lambda function is designed to help you identify Amazon EC2 instances that are associated with a specific security group. This can be useful for quickly understanding which instances have certain network configurations.

## Introduction

AWS Lambda is a serverless computing service that lets you run code without provisioning or managing servers. This Lambda function demonstrates how to use the AWS SDK (boto3) to retrieve information about EC2 instances that are using a specified security group.

## Getting Started

1. Make sure you have an AWS account and appropriate permissions to create and run Lambda functions.
2. Set up your Lambda function in the AWS Management Console or using the AWS CLI.
3. Customize the `security_group_id` variable in the code with the security group ID you want to identify instances for.
4. Configure appropriate triggers for your Lambda function (e.g., API Gateway, CloudWatch Events, etc.).
5. Test the Lambda function to observe instances using the specified security group.

## Code Explanation

- The `boto3` library is used to create an AWS EC2 client to interact with EC2 resources.
- The `describe_instances` method is called with a filter to retrieve instances associated with the specified security group.
- Instance details such as Instance ID, Instance Type, and State are collected and stored.
- The Lambda function responds with a JSON object containing the instances found, along with a status code and a message.

## Example Output

```json
{
  "statusCode": 200,
  "body": {
    "message": "Instances using security group sg-0123456789abcdef0",
    "instances": [
      {
        "InstanceId": "i-1234567890abcdef1",
        "InstanceType": "t2.micro",
        "State": "running"
      },
      {
        "InstanceId": "i-2345678901abcdef2",
        "InstanceType": "t2.small",
        "State": "stopped"
      }
    ]
  }
}
