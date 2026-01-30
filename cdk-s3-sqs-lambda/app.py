#!/usr/bin/env python3
import aws_cdk as cdk

from cdk_s3_sqs_lambda.cdk_s3_sqs_lambda_stack import CdkS3SqsLambdaStack

app = cdk.App()

CdkS3SqsLambdaStack(app, "CdkS3SqsLambdaStack")

app.synth()
