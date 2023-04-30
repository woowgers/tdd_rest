from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from puppies.models import Puppy
from puppies.serializers import PuppySerializer


@api_view(('GET', 'DELETE', 'PUT'))
def get_delete_update_puppy(request: Request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(PuppySerializer(puppy).data)
    if request.method == 'DELETE':
        return Response({})
    if request.method == 'PUT':
        return Response({})


@api_view(('GET', 'POST'))
def get_post_puppies(request: Request):
    if request.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        return Response({})
