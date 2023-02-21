import json

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView


class Login(APIView):
    def post(self, request, format=None):
        username = request.data.get('phone', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.create(user=user)
        else:
            raise AuthenticationFailed()
        return Response(json.dumps({"token": token.key}))
