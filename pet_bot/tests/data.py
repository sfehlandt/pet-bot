from django.utils import timezone

PET_DATA = {
    'name'     : 'Smelly',
    'species'  : 'Cat',
    'owner'    : 'Owned',
    'credits'  : 300,
    'status'   : 0,
    'happiness': 0,
}

PET_DATA_2 = {
    'name'     : 'Stinky',
    'species'  : 'Cat',
    'owner'    : 'Owned',
    'credits'  : 100,
    'status'   : 0,
    'happiness': 0,
}

TASK_DATA = {
    'name'        : 'Do this thing',
    'description' : 'In order to do this you should...',
    'credits'     : 300,
    'status'      : 0,
    'deadline'    : timezone.now(),
}
