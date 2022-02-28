from datetime import datetime
from re import S


def myAuthorizer(event, context):
    access_ok = event['request_headers'].get('x-my-auth-key') == '---my-secret---'
    response_200 = {
        'status': 200,
        'data': {
            'user': {
                'id': 1,
                'name': 'My User',
            },
            'datetime': datetime.now().isoformat(),
        },
    }
    response_400 = {
        'status': 400,
        'data': None,
    }
    return response_200 if access_ok else response_400
