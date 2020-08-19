def myAuthorizer(event, context):
    access_ok = event['request_headers'].get('x-my-auth-key') == '---my-secret---'
    return {
        'status': 200 if access_ok else 400,
        'data': None,
    }
