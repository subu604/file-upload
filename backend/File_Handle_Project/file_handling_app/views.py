# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FileRevision
from .serializers import FileRevisionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# views.py
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class FileView(APIView):
    """View is for handling file related thing"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        filename = kwargs.get('filename')
        user = request.user
        latest_version = FileRevision.objects.filter(filename=filename, user=user).order_by('-version').first()
        version = latest_version.version + 1 if latest_version else 0

        data = {
            'file': file_obj,
            'version': version,
            'filename': filename
        }

        serializer = FileRevisionSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "File uploaded successfully", "version": version}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """Fetching the associated user version file"""
        filename = kwargs.get('filename')
        version = request.GET.get('version', 0)
        user = request.user
        if version is not None:
            file_revision = get_object_or_404(FileRevision, filename=filename, version=version, user=user)
        else:
            file_revision = get_object_or_404(FileRevision.objects.filter(filename=filename, user=user).order_by('-version').first())
        
        serializer = FileRevisionSerializer(file_revision)
        return Response(serializer.data)