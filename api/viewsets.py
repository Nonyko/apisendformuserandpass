from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.decorators import api_view




@api_view(['POST'])
def usernameandpassword(request):
    username = None
    password = None
    if request.method == 'POST':
        username = dict(request.data).get('username')
        password = dict(request.data).get('password')
        if username!=None and password!=None:
            return Response({"message": "Got some data!", "data": request.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)
