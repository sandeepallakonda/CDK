import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
    RemovalPolicy,
)
from constructs import Construct


class CdkS3SqsLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self,
            "YamlUploadQueue",
            visibility_timeout=cdk.Duration.seconds(300)
        )

        bucket = s3.Bucket(
            self,
            "YamlUploadBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.SqsDestination(queue),
            s3.NotificationKeyFilter(prefix="RAW/", suffix=".yaml")
        )

        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.SqsDestination(queue),
            s3.NotificationKeyFilter(prefix="RAW/", suffix=".yml")
        )

        fn = _lambda.Function(
            self,
            "YamlProcessorLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="handler.main",
            code=_lambda.Code.from_asset("lambda"),
            timeout=cdk.Duration.seconds(60)
        )

        bucket.grant_read(fn)

        fn.add_event_source(
            lambda_event_sources.SqsEventSource(queue, batch_size=1)
        )

        cdk.CfnOutput(
            self,
            "BucketName",
            value=bucket.bucket_name
        )
