from django.utils import timezone

PET_DATA = {
    'name'               : 'Smelly',
    'species'            : 'Cat',
    'owner'              : 'Owned',
    'available_credits'  : 0,
    'state'              : 0,
    'required_credits'   : 0,
}

TASK_DATA = {
    'name'        : 'Do this thing',
    'description' : 'In order to do this you should...',
    'credits'     : 300,
    'status'      : 0,
    'deadline'    : timezone.now(),
}
