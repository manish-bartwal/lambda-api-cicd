def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello AWS lambda build number created. THis is the second build"
    }

