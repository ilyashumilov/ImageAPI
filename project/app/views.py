from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image, User
from .serializers import ImageSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
import random
import os

# Create your views here.

def auth_docorator(func):
    def wrapper(*args):
        if 'HTTP_AUTHORIZATION' not in args[1].META:
            return Response({"message": "Not authorized request"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                token = args[1].META['HTTP_AUTHORIZATION'].replace('Bearer ', '')
                user = get_object_or_404(User, token=token)
            except:
                return Response({'Messge': 'Authorization header format error' }, status=status.HTTP_400_BAD_REQUEST)
        return func(*args)
    return wrapper

class ImageView(APIView):
    @auth_docorator
    def get(self, request):

        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many=True)

        return Response(
            serializer.data,
            status=200,
        )

    @auth_docorator
    def post(self, request):
        print(request.META)

        serializer = ImageSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The new Image instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @auth_docorator
    def put(self, request):
        id = request.query_params['id']

        instance = get_object_or_404(Image.objects.all(), pk=id)
        serializer = ImageSerializer(instance, data=request.data)

        # print(serializer.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The Image instance has been updated"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @auth_docorator
    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Image.objects.get(pk=request.query_params['id'])
            path = 'images/'+ instance.image.url.replace('media/','')
            os.remove(path)
            instance.delete()
            return Response({"message": f"The Image instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'The Image instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)

class DeleteAllImages(APIView):
    @auth_docorator
    def post(self, request):
        token = request.META['HTTP_AUTHORIZATION'].replace('Bearer ', '')
        if not User.objects.get(token=token).admin:
            return Response({'error': 'No permission'}, status=status.HTTP_400_BAD_REQUEST)

        instances = Image.objects.all()

        for instance in instances:
            path = 'images/'+ instance.image.url.replace('media/','')
            os.remove(path)
            instance.delete()

        return Response({"message": f"All Image instances have been deleted"},
                        status=status.HTTP_200_OK)


class UserCreation(APIView):
    def post(self,request):
        hash = random.getrandbits(128)
        instance = User(admin=request.data['admin'], token=hash)
        instance.save()

        return Response({"Token": instance.token},
                        status=status.HTTP_200_OK)

