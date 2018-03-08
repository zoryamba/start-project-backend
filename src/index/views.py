from django.shortcuts import render
from celery_app import celery_app


# Create your views here.
from django.http import JsonResponse


def index(request):
    with celery_app.producer_or_acquire() as producer:
        with producer.connection._reraise_as_library_errors():
            producer.publish(
                {'test': 'test'},
                routing_key='websocket',
            )

    return JsonResponse({'result': 'success'})
