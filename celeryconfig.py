# -*- coding: utf-8 -*-

from kombu import (
    Exchange,
    Queue
)

BROKER_URL = "amqp://guest:guest@localhost:5672/zeus"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

CELERY_DEFAULT_QUEUE = 'default'


CELERY_QUEUES = (
    Queue("default", routing_key='default'),
    Queue("async_task", Exchange("async_task", type='topic'), routing_key="task.#"),
)

CELERY_ROUTES = {
    'jinjia2.add_log': {"queue": "async_task", "routing_key": "task.add_log"},
 }

CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
