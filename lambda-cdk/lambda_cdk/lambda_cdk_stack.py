from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam
)
from constructs import Construct

class LambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda Function
        lambda_fn = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Attach IAM policy to allow S3 access
        lambda_fn.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "s3:ListBucket",
                    "s3:GetObject"
                ],
                resources=["*"]
            )
        )
