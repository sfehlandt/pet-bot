from django.utils import timezone
from ..models import Pet

PET_DATA = {
    'name'               : 'Smelly',
    'species'            : 'Cat',
    'owner_name'         : 'Owned',
    'owner_id'           : '321642321354',
    'available_credits'  : 100,
    'state'              : Pet.SAD,
    'required_credits'   : 60,
}

TASK_DATA = {
    'name'        : 'Do this thing',
    'description' : 'In order to do this you should...',
    'credits'     : 300,
    'status'      : 1,
    'deadline'    : timezone.now(),
}

TASK_DATA_LAMBDA = lambda x : {
    'name'        : 'Do this thing' + x,
    'description' : 'In order to do this you should...' + x,
    'credits'     : 300,
    'status'      : 1,
    'deadline'    : timezone.now(),
}
