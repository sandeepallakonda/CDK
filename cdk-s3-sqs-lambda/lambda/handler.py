def main(event, context):
    print("Received event:", event)
    return {
        "statusCode": 200,
        "body": "YAML processed successfully"
    }
