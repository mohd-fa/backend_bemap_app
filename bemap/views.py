from django.http import JsonResponse
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def day_detail(request, id):

    try:
        event = Event.objects.filter(day=id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        event_bucket=[]
        for i in event:
            serializer=EventSerializer(i)
            event_bucket.append(serializer.data)
        return Response({'events':event_bucket})

@api_view(['GET'])
def event_list(request):

    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse({'events':serializer.data}, safe=False)

@api_view(['GET'])
def event_detail(request, id):

    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)