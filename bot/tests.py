from django.test import TestCase

# Create your tests here.


'multiply-task-contrab': {
        'task': 'movies.tasks.mul',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },

    'multiply-every-5-seconds': {
        'task': 'movies.tasks.mul',
        'schedule': 5.0,
        'args': (16,16)
    },

    'add-every-30-seconds': {
        'task': 'movies.tasks.add',
        'schedule': 30.0,
        'args': (16,16)
    },

    'database': {
        'task': 'movies.tasks.bkup',
        'schedule': 5.0,
    },