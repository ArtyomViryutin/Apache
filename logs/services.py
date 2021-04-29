from .models import Log
from datetime import datetime


def create_log(**kwargs):
    kwargs['date'] = datetime.strptime(kwargs['date'], '%d/%b/%Y:%H:%M:%S %z')
    kwargs['status'] = int(kwargs['status'])
    if not kwargs['response_size']:
        kwargs['response_size'] = 0
    kwargs['response_size'] = int(kwargs['response_size'])
    Log.objects.create(**kwargs)
